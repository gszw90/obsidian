#!/usr/bin/env python3
"""Fetch GitHub monthly trending into vault raw data.

Deterministic collector for the `github-trending` skill:
  firecrawl scrape (stars/month) + gh api (metadata) -> note/Github/Trending/<YYYY-MM>.{md,jsonl}

The LLM-judgment half (wiki source page, entity pages, meta updates) lives in SKILL.md.

Usage:
  python3 fetch_trending.py [YYYY-MM] [--dry-run] [--force]

Gotchas baked in (learned the hard way, see SKILL.md):
  - zsh does not word-split unquoted $vars -> never shell-loop over a var; this is python.
  - CJK + WSL can silently drop dirs -> all paths absolute, no cd into CJK dirs.
  - firecrawl markdown has nav noise -> repo descriptions come from gh api, not page parse.
"""
import argparse, json, os, re, subprocess, sys, datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))  # .../note
VAULT = os.path.join(REPO_ROOT, "note")
DATA_DIR = os.path.join(VAULT, "Github", "Trending")
TRENDING_URL = "https://github.com/trending?since=monthly"

# Order matters: specific domains first, agent/mcp catchall LAST.
# Keywords matched as whole tokens (+plural), never as substring ("nat" won't hit "natural").
DOMAIN_RULES = [
    (("iptv", "m3u"), "媒体资源"),
    (("meeting", "transcription", "whisper", "parakeet"), "AI 会议"),
    (("encryption", "e2ee", "double-ratchet", "messaging", "simplex"), "隐私通讯"),
    (("security", "pentest", "penetration", "vulnerability", "bug-bounty", "ai-security"), "AI 安全/红队"),
    (("container", "kubernetes", "k8s", "docker"), "容器/云原生"),
    (("p2p", "quic", "holepunch"), "P2P/网络"),
    (("ffmpeg", "video", "image-generation", "remotion", "video-production"), "AI 内容生产"),
    (("prompt", "system-prompt", "awesome", "dataset"), "AI 资源/数据"),
    (("travel", "trip", "self-hosted", "packing", "budget"), "自托管应用"),
    (("agent", "mcp", "coding-agent", "orchestration", "gateway", "browser-automation", "multiplexer", "cloner"), "AI Agent 基础设施"),
]


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, shell=True)


def _variants(kw):
    """kw + plural forms for token matching."""
    v = {kw, kw + "s"}
    if kw.endswith("y"):
        v.add(kw[:-1] + "ies")
    return v


def classify(meta):
    blob = " ".join((meta.get("topics") or [])).lower() + " " + (meta.get("desc") or "").lower()
    tokens = set(re.split(r"[\W_]+", blob))  # split on non-word incl hyphen/underscore
    for kws, dom in DOMAIN_RULES:
        for kw in kws:
            if tokens & _variants(kw):
                return dom
    return "其他"


def scrape_trending(tmp_path):
    """firecrawl scrape -> markdown path. Returns text."""
    r = sh(f'firecrawl scrape "{TRENDING_URL}" --output "{tmp_path}"')
    if not os.path.exists(tmp_path):
        sys.exit(f"firecrawl scrape failed:\n{r.stderr}\n{r.stdout}")
    with open(tmp_path, encoding="utf-8") as f:
        return f.read()


def parse_trending(md):
    """Extract [{slug, stars_month, total, forks}] from firecrawl markdown."""
    cards, prev = [], 0
    for m in re.finditer(r"([\d,]+) stars this month", md):
        block = md[prev:m.start()]
        prev = m.end()
        sm = int(m.group(1).replace(",", ""))
        um = re.search(r"github\.com/([A-Za-z0-9_-]+/[A-Za-z0-9_.-]+)/(?:stargazers|forks)", block)
        if not um:
            continue
        slug = um.group(1)
        tot = fork = None
        tm = re.search(r"\[([\d,]+)\]\(https://github\.com/[^)]+/stargazers\)", block)
        fm = re.search(r"\[([\d,]+)\]\(https://github\.com/[^)]+/forks\)", block)
        if tm: tot = int(tm.group(1).replace(",", ""))
        if fm: fork = int(fm.group(1).replace(",", ""))
        cards.append({"slug": slug, "stars_month": sm, "total": tot, "forks": fork})
    best = {}
    for c in cards:
        s = c["slug"]
        if s not in best or c["stars_month"] > best[s]["stars_month"]:
            best[s] = c
    return sorted(best.values(), key=lambda c: -c["stars_month"])


def gh_enrich(slug):
    """gh api repos/SLUG -> dict or None on 404."""
    jq = '{repo:.full_name, desc:.description, lang:.language, stars:.stargazers_count, forks:.forks_count, topics:.topics, home:.homepage, license:(.license.spdx_id // "None"), created:.created_at, pushed:.pushed_at, archived:.archived}'
    r = sh(f'gh api "repos/{slug}" --jq {json.dumps(jq)}')
    if r.returncode != 0 or not r.stdout.strip():
        print(f"  gh api FAIL {slug}: {r.stderr.strip()[:120]}", file=sys.stderr)
        return None
    try:
        return json.loads(r.stdout.strip())
    except json.JSONDecodeError:
        return None


def build_md(period, rows):
    lines = [
        "---",
        f"title: GitHub Trending 月榜 · {period}",
        "type: source-data",
        f"period: {period}",
        f"source_url: {TRENDING_URL}",
        f"fetched: {datetime.date.today().isoformat()}",
        "transport: firecrawl(scrape) + gh api(metadata)",
        "---",
        "",
        f"# GitHub Trending 月榜 · {period}",
        "",
        f"抓取自 `{TRENDING_URL}`（{datetime.date.today().isoformat()}）。",
        f"原始结构化数据：`{period}-raw.jsonl`（同目录）。wiki 分析页：`sources/GitHub-Trending-{period}.md`。",
        "",
        "> [!note] 字段来源",
        "> `stars/月` = trending 页「stars this month」；其余 = GitHub API（`gh api`）。领域为关键词初分，agent 在 source 页可修正。",
        "",
        "## 仓库清单（按 stars/月排序）",
        "",
        "| # | Stars/月 | 总 Stars | Forks | 仓库 | 语言 | License | 领域 | 一句话 |",
        "|---|---------:|---------:|------:|------|------|---------|------|--------|",
    ]
    lang_count, dom_count, new_repo = {}, {}, 0
    for i, r in enumerate(rows, 1):
        m = r["meta"]
        lang = m.get("lang") or "?"
        lang_count[lang] = lang_count.get(lang, 0) + 1
        dom = r["domain"]
        dom_count[dom] = dom_count.get(dom, 0) + 1
        try:
            age_months = (datetime.date.today() - datetime.date.fromisoformat(m["created"][:10])).days / 30
            if age_months < 6:
                new_repo += 1
        except Exception:
            pass
        desc = (m.get("desc") or "")[:60].replace("|", "/")
        slug = m["repo"]
        lines.append(
            f"| {i} | {r['stars_month']:,} | {m.get('stars',0):,} | {m.get('forks',0):,} | "
            f"[{slug}](https://github.com/{slug}) | {lang} | {m.get('license','None')} | {dom} | {desc} |"
        )
    lines += ["", "## 领域分布", ""]
    for dom, n in sorted(dom_count.items(), key=lambda x: -x[1]):
        lines.append(f"- **{dom}**：{n}")
    lines += ["", "## 语言分布", ""]
    lines.append(" · ".join(f"{k} {v}" for k, v in sorted(lang_count.items(), key=lambda x: -x[1])))
    lines += ["", f"> 仓库年龄：约 {new_repo}/{len(rows)} 个创建于 6 个月内（新项目冲榜）。", ""]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("period", nargs="?", default=datetime.date.today().strftime("%Y-%m"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    out_md = os.path.join(DATA_DIR, f"{args.period}.md")
    if os.path.exists(out_md) and not args.force and not args.dry_run:
        sys.exit(f"已存在 {out_md}。用 --force 覆盖，或换 period。")

    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = os.path.join(DATA_DIR, f".{args.period}-scrape.md")

    print(f"[1/3] firecrawl scrape {TRENDING_URL} ...")
    md = scrape_trending(tmp)
    cards = parse_trending(md)
    if not cards:
        sys.exit(f"解析出 0 仓库——firecrawl 输出格式可能变了，检查 {tmp}")
    print(f"      {len(cards)} repos from trending page")

    print(f"[2/3] gh api enrich ...")
    rows = []
    for c in cards:
        meta = gh_enrich(c["slug"])
        if not meta:
            continue
        meta["stars_month"] = c["stars_month"]
        rows.append({"slug": c["slug"], "stars_month": c["stars_month"], "meta": meta, "domain": classify(meta)})
    print(f"      {len(rows)} enriched")

    print(f"[3/3] write outputs ...")
    md_text = build_md(args.period, rows)
    if args.dry_run:
        print("=== DRY RUN (first 30 lines) ===")
        print("\n".join(md_text.splitlines()[:30]))
        return
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(md_text)
    with open(os.path.join(DATA_DIR, f"{args.period}-raw.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r["meta"], ensure_ascii=False) + "\n")
    try:
        os.remove(tmp)
    except OSError:
        pass
    print(f"done -> {out_md}")
    print(f"      {os.path.join(DATA_DIR, args.period + '-raw.jsonl')}")


if __name__ == "__main__":
    main()
