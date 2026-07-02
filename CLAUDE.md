# Project: note — Obsidian Knowledge Vault

Personal knowledge base ("second brain"). Obsidian vault fed by structured ingest pipeline (`claude-obsidian` plugin). Raw personal notes read, extracted into **sources / entities / concepts**, cross-referenced, indexed. **Vault language: Chinese.** Write all wiki page content in Chinese.

---

## Layout

```
/mnt/d/Projects/Go/note/          ← git repo root (cwd for Claude sessions)
├── CLAUDE.md                     ← this file
├── .gitignore                    ← ignores workspace state, etc.
├── note/                         ← VAULT ROOT (Obsidian opens this folder)
│   ├── .obsidian/                ← Obsidian config (spellcheck OFF)
│   ├── .vault-meta/              ← transport.json + mode.json (ingest config)
│   ├── .raw/
│   │   └── .manifest.json        ← DELTA TRACKER (md5 per source) — edit carefully
│   ├── Develop/  Mac/  Resource/ ← SOURCE notes (raw personal notes, immutable inputs)
│   ├── wiki/                     ← INGESTED knowledge base
│   │   ├── sources/              ← one summary page per source note
│   │   ├── entities/             ← one page per product / org / repo / person
│   │   ├── concepts/             ← one page per idea / framework / category
│   │   ├── domains/  folds/      ← (unused so far)
│   │   ├── index.md              ← master page index — update on every ingest
│   │   ├── overview.md           ← vault scope/big picture — update when scope shifts
│   │   ├── hot.md                ← hot cache: most-recent ingest context (read first)
│   │   └── log.md                ← append-only ingest log (newest entry at TOP)
│   └── 欢迎.md                   ← Obsidian default stub, NOT ingested
```

**Two roots matter:** git root (`.`) where Claude runs; vault root (`note/`) where every wiki path lives. Wiki paths here vault-relative (e.g. `wiki/sources/Foo.md` = `note/wiki/sources/Foo.md` from git root).

---

## The ingest workflow

Add content via **`claude-obsidian:wiki-ingest`** skill (or dispatch `wiki-ingest` / `claude-obsidian:wiki-ingest` agent for batches). Flow per source:

1. **Delta check** — compute `md5sum` of source, compare against `.raw/.manifest.json`. Hash matches existing entry → skip (unless `force`).
2. **Read fully**, extract entities + concepts.
3. **Create** 1 source page + N entity pages + N concept pages (typical source touches 8–15 pages total).
4. **Assign addresses?** No — DragonScale OFF (no `scripts/allocate-address.sh`). Pages have no `address:` field. Don't add one.
5. **Update meta pages:** `wiki/index.md`, `wiki/hot.md` (newest top), `wiki/log.md` (newest top), `wiki/overview.md` (only if scope changed), `.raw/.manifest.json` (record hash + pages_created/updated).
6. **Cross-reference** — link related pages; flag contradictions with `> [!contradiction]` callouts on both pages (never silently overwrite).

Delta re-ingest: source note changes (hash differs) → update pages it already produced, don't create new ones. Bump `updated:` dates, log `re-ingest` entry.

---

## CRITICAL — wikilink convention (read before editing any wiki page)

**Filenames use dashes; link text uses spaces; `aliases:` bridges them.**

Obsidian resolves `[[Target]]` against file **basename** or **`aliases:`** frontmatter — NOT `title:`. This vault names files with dashes (`Mac-快捷键.md`) but links with spaces (`[[Mac 快捷键]]`). Space form resolves only because each page declares it as alias.

**Rule for every new wiki page whose title contains spaces or separators:** add `aliases:` line equal to readable (space/dash-with-spaces) title:

```yaml
---
title: Mac 快捷键          # title can be anything
aliases: [Mac 快捷键]       # MUST match the form used in [[...]] links
type: concept
---
```

Multi-word titles like `Headroom - 上下文压缩代理` → set `aliases: [Headroom - 上下文压缩代理]` exactly as links spell it.

Rename a page → also repoint `aliases:` of new file to cover old name (or update inbound links). Prior `[[开发网页工具]]` → `常用网址导航` rename left dangling links until alias added — don't repeat.

**Verify link integrity after structural edits** with quick resolver check (basename + `aliases:` must cover every `[[link]]` target). Vault always at 0 dead links.

---

## Transport & mode

From `note/.vault-meta/`:
- **Transport = `filesystem`** — no Obsidian CLI binary, no MCP server. All vault writes via Claude's `Write`/`Edit` tools with absolute vault-rooted paths. Floor; always works.
- **Mode = `generic`** — flat structure. New pages file directly under `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`. No MOCs, no date-prefix IDs, no PARA `incoming/` staging.

No `scripts/wiki-lock.sh` — **single-writer assumed**. Don't run parallel ingests writing same file. PostToolUse hook auto-commits `wiki/` + `.raw/`; if you stage manual commits, expect hook to also fire.

---

## Meta-page editing rules

- **`index.md`** — add every new page under type section (来源 / 概念 / 实体). Bump `updated:`.
- **`hot.md`** — newest ingest block at TOP. One block per ingest batch. Fast-path context for next session — keep tight.
- **`log.md`** — newest entry at TOP. Use `## YYYY-MM-DD ingest | …` or `## YYYY-MM-DD re-ingest | …` headers. Record pages created/updated + key findings.
- **`overview.md`** — only when vault's scope/big-picture changes (new domain added), not per-ingest.
- **`.raw/.manifest.json`** — source keys vault-relative (`Develop/Ai/Plugin/headroom.md`, NOT `note/` prefixed). After editing, JSON must stay valid.

---

## Page frontmatter (required fields)

Every content page (source / entity / concept):
```yaml
---
title: <readable name>
aliases: [<space form of the name>]   # required if title has spaces/separators
type: source | entity | concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [...]
---
```
`status:` field optional (lint flags missing but not enforced).

---

## Skills & agents available (claude-obsidian plugin)

- **`claude-obsidian:wiki-ingest`** — ingest source / batch of sources.
- **`claude-obsidian:wiki-lint`** (agent) — health check: dead links, orphans, stale claims, frontmatter gaps. Read-only report; apply fixes manually.
- **`claude-obsidian:wiki`** — bootstrap / scaffold / hot-cache management.
- **`claude-obsidian:save`** — file current conversation/insight as note.
- **`claude-obsidian:wiki-cli`** — transport reference (filesystem fallback here).

---

## Gotchas

- **WSL + CJK paths** — `find`/`ls` output for Chinese filenames can render garbled in shell. Use Python (`glob`) via `ctx_execute` for reliable listing, or `git status --porcelain` (quotes non-ASCII paths).
- **Source notes immutable inputs.** Never edit files under `Develop/`, `Mac/`, `Resource/` during ingest (source of truth wiki mirrors). Only `.raw/` file ingest mutates: `.manifest.json`.
- **Editorial judgment expected.** Not every mentioned tool needs entity page — fold baseline infra (e.g. `pip`, `pipx`, `zsh`) into concept comparison pages. One page per *entity-worthy* product.
- **No build / no tests.** Docs project. "Verification" = link integrity check + valid manifest JSON, not running test suite.