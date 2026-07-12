---
title: GitHub Trending 月度追踪
aliases: [GitHub Trending 月度追踪]
type: concept
created: 2026-07-11
updated: 2026-07-12
tags: [GitHub, trending, 趋势, 追踪, 概念]
---

# GitHub Trending 月度追踪

按月抓取 [github.com/trending](https://github.com/trending?since=monthly) 全量榜，记录仓库 / 领域 / 语言 / stars，跨月对比看技术趋势演化。

## 机制

**采集**（每月初手动触发——对 agent 说「拉本月 github trending 入 wiki」；可选系统 crontab 见下）：

1. `firecrawl scrape "https://github.com/trending?since=monthly"` → 拿 25 个仓库 + **stars/月** + 总 stars/forks
2. `gh api repos/<owner>/<repo>` → 富化描述 / 语言 / topics / license / 创建时间（已 auth，5000/hr 额度）
3. 写原始数据 → `note/Github/Trending/<YYYY-MM>.md`（人读表）+ `<YYYY-MM>-raw.jsonl`（机读）
4. wiki-ingest → 建本月分析 source 页（`sources/GitHub-Trending-<YYYY-MM>.md`）

> [!warning] CronCreate 撑不到月度
> Claude Code 的 CronCreate 对 recurring 任务 **7 天自动过期**，月度循环跑不到下月。要真自动化：系统 crontab 调 `claude -p "拉本月 github trending 入 wiki"`（每月 1 日）。否则每月手动触发即可。

**字段**：仓库 · 语言 · stars/月 · 总 stars · forks · license · 领域 · 描述 · 创建时间。

> [!note] firecrawl 在场前必经 `defuddle` 去噪
> trending 页 nav 严重，直接抓描述噪声大——富化走 GitHub API 而非页面解析，描述才可靠。

## 月度索引

| 月份 | source 页 | 原始数据 | 主题 |
|------|-----------|----------|------|
| 2026-07 | [[GitHub Trending 月榜 2026-07]] | `note/Github/Trending/2026-07.md` | AI agent 基础设施爆发（65% AI 相关） |

> 新月 cron 触发后追加行。手工补：让 agent 「拉本月 github trending 入 wiki」。

## 领域分类法（统一标签，便于跨月对比）

- **AI Agent 基础设施** — agent 编排 / MCP / 网关 / 多路复用 / 浏览器 agent
- **AI 安全 / 红队** — 渗透测试 / skill 扫描 / 评估 agent
- **AI 资源 / 数据** — prompt 集 / 数据集 / awesome 列表
- **AI 内容生产** — 视频 / 图像 / 写作
- **容器 / 云原生** — 容器运行时 / K8s
- **P2P / 网络** — QUIC / NAT / sync
- **隐私 / 安全** — 加密通讯 / 隐私工具
- **开发者工具** — git / 构建包管理（非 AI）
- **自托管应用** — 个人/团队自部署
- **媒体资源** — IPTV / 资源聚合

## 跨月观察点（积累后填）

- 领域此消彼长（agent 基建是否持续统治？AI 安全何时登顶？）
- 语言分布漂移（Rust 份额？Go 回潮？）
- 仓库年龄趋势（新项目冲榜速度是否继续加快？）
- Apple/Alibaba/NVIDIA 等大厂官方仓库入场节奏

## 关联

- 采集工具：firecrawl（页面）+ `gh` CLI（API 富化）
- 入库流程：wiki-ingest skill
- 本月：[[GitHub Trending 月榜 2026-07]]

## 待扩展

- 累积 3+ 月后建趋势对比 source 页（领域热力图 / 语言堆叠 / 新老仓库比）
- 历史 backfill（若需）：手动指定历史月份也可抓，但 GitHub trending 仅给当前快照，历史需 archive
