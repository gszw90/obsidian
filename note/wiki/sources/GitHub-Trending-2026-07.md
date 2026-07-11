---
title: GitHub Trending 月榜 2026-07
aliases: [GitHub Trending 月榜 2026-07]
type: source
created: 2026-07-11
updated: 2026-07-11
tags: [GitHub, trending, 趋势, 月度, AI-agent, 来源]
---

# GitHub Trending 月榜 2026-07

2026-07 月度 GitHub trending 分析。原始数据：[[GitHub Trending 月度追踪]] 机制，本月快照存 `note/Github/Trending/2026-07.md` + `2026-07-raw.jsonl`。

> [!note] 采集方式
> `firecrawl scrape "github.com/trending?since=monthly"` 拿 stars/月 → `gh api repos/<o>/<r>` 富化（描述/语言/topics/license）。

## 月度主题：AI Agent 基础设施爆发

20 席中 **13 席 AI 相关（65%）**，agent 基础设施独占近半。核心信号：agent 层正从单工具向**舰队 / 多路复用 / 网关**基础设施演化——三个抽象同时上榜：

- **并行舰队**：stablyai/orca（agent fleet ADE）
- **多路复用**：ogulcancelik/herdr（终端 agent multiplexer）
- **统一网关**：diegosouzapw/OmniRoute（231+ provider 一个端点）

## Top 5（按 stars/月）

| # | Stars/月 | 仓库 | 领域 | 一句话 |
|---|---------:|------|------|--------|
| 1 | 32,095 | calesthio/OpenMontage | AI 内容生产 | agentic 视频生产系统 |
| 2 | 28,774 | Panniantong/Agent-Reach | Agent 基建 | agent 全网搜索（含 B 站/小红书） |
| 3 | 26,480 | DeusData/codebase-memory-mcp | Agent 基建 | 代码库→知识图谱 MCP（同本 vault codegraph 思路） |
| 4 | 19,234 | [[Apple Container]] | 容器 | Apple 官方 Mac Linux 容器（Swift） |
| 5 | 14,876 | iptv-org/iptv | 媒体资源 | 全球 IPTV m3u 合集 |

## 领域分布

| 领域 | 数 | 备注 |
|------|---:|------|
| AI Agent 基础设施 | 9 | 占近半，本月最强信号 |
| AI 安全 / 红队 | 3 | strix + SkillSpector + hiring-agent，AI 红队工具化 |
| AI 资源 | 1 | system_prompts_leaks（含 Claude Fable 5 / Opus 4.8 / GPT-5.6 prompt） |
| 容器 / 云原生 | 1 | apple/container |
| P2P / 网络 | 1 | iroh（QUIC + NAT） |
| 隐私通讯 | 1 | simplex-chat |
| 媒体 / 开发工具 / 自托管 | 3 | iptv / no-mistakes / TREK |

## 语言分布

`TypeScript 6` · `Python 6` · `Rust 3` · `C/Swift/Haskell/Go/JavaScript 各 1`

> [!key-insight] TS + Python 主导 agent 工具链；Rust 占性能敏感位（转录/多路复用/P2P）。

## 仓库年龄观察

多为 **2026 H1 新建**（2–5 月龄冲榜）：orca/herdr/iptv 新版（2026-03）、Agent-Reach/codebase-memory-mcp（2026-02）。老牌仅 iptv-org（2018）、simplex-chat（2019）、iroh（2022）。

> [!key-insight] 月度 trending 已成 AI agent 新项目冷启动主战场——新仓库 2–3 个月可冲万星。

## 与本 vault 的关联

- [[Apple Container]] ↔ [[OrbStack]] / [[开发容器]]：Apple 官方入场，容器赛道新选项
- DeusData/codebase-memory-mcp ↔ 本 vault 实际在用的 codegraph MCP：**同思路（代码→图）**，可作 codegraph 替代/对比候选
- diegosouzapw/OmniRoute：AI 网关，与 [[Headroom]]（上下文压缩）、[[技能自进化闭环]]（SkillOpt）同属 agent 效率谱系
- system_prompts_leaks 含 Claude Code / Fable 5 / Opus 4.8 系统 prompt——研究 agent 行为的一手资料

## 关联

- 追踪机制：[[GitHub Trending 月度追踪]]
- 原始数据：`note/Github/Trending/2026-07.md`（含完整 20 表 + 领域/语言分布）
