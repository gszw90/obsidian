---
name: github-trending
description: Use when the user wants to record this month's GitHub trending repos into the wiki — triggers like "拉本月/这个月 github trending", "记录 github 热门仓库", "github trending 月度", "更新 trending 快照". Collects monthly snapshot + enriches via GitHub API + ingests analysis into wiki.
---

# github-trending

Monthly GitHub trending snapshot → vault. Deterministic collection is scripted (`fetch_trending.py`); wiki-ingest judgment is this skill's body.

## Preconditions (verify first)

```bash
firecrawl --status 2>&1 | grep -q Authenticated && echo "firecrawl OK" || echo "firecrawl 未认证 → firecrawl login --api-key fc-..."
gh auth status 2>&1 | grep -q 'Logged in' && echo "gh OK" || echo "gh 未认证 → gh auth login"
```

Either fails → stop, tell user to auth. No auth = no scrape/enrich.

## Flow

### 1. Collect (scripted)

```bash
python3 .claude/skills/github-trending/fetch_trending.py [YYYY-MM] [--force]
```

- Default period = current month. Pass `2026-08` etc. for specific month.
- Writes `note/Github/Trending/<YYYY-MM>.md` (human table + 领域/语言分布) + `<YYYY-MM>-raw.jsonl`.
- **Delta guard**: if `<YYYY-MM>.md` exists, exits unless `--force`. Re-pulling same month → `--force`.
- Domain column = keyword first-pass; you refine it in the source page.
- `--dry-run` to preview without writing (costs 1 firecrawl scrape + N gh calls).

If script reports "解析出 0 仓库" → firecrawl markdown format changed. Inspect `note/Github/Trending/.<period>-scrape.md`, fix `parse_trending` regex.

### 2. Ingest into wiki (judgment)

**Idempotency**: if `wiki/sources/GitHub-Trending-<YYYY-MM>.md` already exists, this month is already ingested — skip to Verify (only re-do if `--force` re-pulled and data materially changed).

Read the generated `<YYYY-MM>.md`. Then create/update:

- **Source page** `wiki/sources/GitHub-Trending-<YYYY-MM>.md` — analysis: 月度主题 (1-2句), Top 5 table, 领域分布, 语言分布, 仓库年龄观察, 与本 vault 关联, key-insight callouts. frontmatter: `type: source`, `aliases: [GitHub Trending 月榜 YYYY-MM]`, `tags: [GitHub, trending, 月度, 来源]`.
- **Concept page** `wiki/concepts/GitHub-Trending-月度追踪.md` — append a row to the "月度索引" table: `| YYYY-MM | [[GitHub Trending 月榜 YYYY-MM]] | note/Github/Trending/YYYY-MM.md | 主题 |`. Bump `updated:`.
- **Entity pages** (editorial — NOT one per repo): only create entity pages for repos with a **strong existing-vault tie** (e.g. apple/container ↔ [[OrbStack]]/[[开发容器]]). Most repos stay in the source-page table. Default: 0-2 entities/month.
- **Meta**: `index.md` (+source, +entity if any), `hot.md` (new block top), `log.md` (`## YYYY-MM-DD ingest | GitHub Trending <YYYY-MM>` top), `overview.md` (no change unless new domain). Bump `updated:` on each.
- **Manifest** `.raw/.manifest.json`: add source keyed `Github/Trending/<YYYY-MM>.md` with hash `trending-snapshot-<YYYY-MM>`, pages_created/updated.

### 3. Verify (read-only)

```bash
python3 -c "
import json,glob,re,os
json.load(open('note/.raw/.manifest.json'))
files=glob.glob('note/wiki/**/*.md',recursive=True)
res=set(os.path.splitext(os.path.basename(f))[0] for f in files)
for f in files:
    am=re.search(r'^aliases:\s*\[(.*?)\]',open(f,encoding='utf-8').read(),re.M|re.S)
    if am: res|={a.strip() for a in re.findall(r'[^\[\],]+',am.group(1))}
dead=[l.strip() for f in files for l in re.findall(r'\[\[([^\]|#]+)',open(f,encoding='utf-8').read()) if l.strip() and l.strip() not in res]
print('manifest OK | dead:', dead or 'NONE')
"
```

Vault invariant: 0 dead links, valid manifest JSON.

## Scheduling caveat

CronCreate recurring tasks **expire after 7 days** — can't hold a monthly cadence. Two options for the user:
- **Manual** (default): each month say "拉本月 github trending 入 wiki" → this skill fires.
- **System crontab** (true auto): `7 3 1 * * cd /mnt/d/Projects/Go/note && claude -p "拉本月 github trending 入 wiki"` — needs `claude -p` runnable non-interactively.

## Gotchas (already handled in script, documented for awareness)

- **zsh no word-split**: `for r in $repos` runs once with the whole string. Script loops in python — never shell-loop a repo-list var.
- **CJK + WSL path flakiness**: dirs can vanish between calls. All paths in script are absolute; never `cd` into a CJK dir.
- **firecrawl markdown noise**: nav/sidebar dominate raw output. Repo descriptions come from `gh api`, NOT page parse — page text is only used for `stars/月` extraction.
- **gh api 404**: renamed/deleted repos 404. Script logs + skips them.
