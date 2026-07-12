---
title: 热缓存
type: hot
created: 2026-07-01
updated: 2026-07-12
---

# 热缓存

最近 ingest 上下文。下次会话先读这里，避免重读全页。

## 2026-07-12 re-ingest | GitHub Trending 2026-07 二次抓取（最新）

- 触发：`fetch_trending.py 2026-07 --force` —— 核验脚本修复（gh_enrich 加重试+并行）
- **修复**：gh api 在 WSL2 下并行握手 TLS timeout（原版 1/19 成功）→ 5 次重试 + 指数退避 + ThreadPool x3 → 连续两次 19/19
- 数据：19 repos（首抓 20，当日榜单波动 -1），主题稳定——AI Agent 基础设施仍占 8 席（68% AI 相关）
- 更新：[[GitHub Trending 月榜 2026-07]]（Top5/分布/年龄数字刷新）+ [[Apple Container]]（#4 16,789 stars/月）+ manifest `ingested_at`
- 编辑判断：re-fetch 数字微动，叙事主题不变 → 只刷新数字 + bump updated，不新建页

## 2026-07-11 ingest | GitHub Trending 月度追踪启动（最新）

- 新管线：每月 1 日 durable cron 拉 github trending → 富化 → 入 wiki
- 本月（2026-07）：[[GitHub Trending 月榜 2026-07]] + [[GitHub Trending 月度追踪]]（机制/索引）+ [[Apple Container]] 实体
- 原始数据新根目录：`note/Github/Trending/`（`2026-07.md` + `2026-07-raw.jsonl`）
- 采集：firecrawl scrape 拿 stars/月 + `gh api` 富化描述/语言/topics/license
- 关键洞察：
  - **AI agent 基础设施爆发**：20 席 65% AI，agent 基建占近半（orca 舰队 / herdr 多路复用 / OmniRoute 网关同时上榜 = agent 层抽象成熟）
  - DeusData/codebase-memory-mcp 与本 vault 在用的 codegraph MCP **同思路**，可对比候选
  - apple/container 官方入场，对标 [[OrbStack]]
  - system_prompts_leaks 含 Claude Fable 5 / Opus 4.8 / Claude Code 系统 prompt
- 编辑判断：20 仓库只建 1 实体（apple/container，强 vault 关联），其余入表

## 2026-07-11 ingest | 第 5 批：HTML+CSS + 参考书 stub

- 新源：[[HTML CSS 基础]]、[[Python 学习手册（第4版）]]、[[Kubernetes book（Jimmy Song）]]
- 新概念：[[CSS 布局与单位]]
- 主题扩展：**前端 / CSS**（首次）、**参考书籍**存根机制
- 关键洞察：
  - 移动端 dvh/svh/lvh 替代 vh，规避地址栏伸缩遮挡
  - flex 简写：`flex:1`=平分、`none`=不伸缩、`auto`=按内容伸缩、`initial`=可缩不可放
  - Kubernetes（多节点编排）vs OrbStack（单机容器）：抽象层次差
- 编辑判断：HTML/CSS 折入 1 概念页；两本 PDF 教材做**书籍参考 stub**（不抽概念，按需补）
- 源笔记纠错：`grid-area: heder`→`header`、`vm`→`vw`

## 2026-07-03 实证 | SkillOpt-Sleep rule judge 假阳性

- 跑 `/skillopt-sleep run --backend claude` → night 6 报 0.050→0.550 accept，但 `replay: mock` + rule judge（regex/contains）→ **假阳性**
- 候选规则全是格式过拟合（强制 `## Pages created` 表 / 字面 `Cross-reference`），`_why` 自承「满足 evaluator grep 串」
- 真验证：手写 rubric 任务 `--tasks-file` + `--backend claude` → `ClaudeBackend.judge()` 真 LLM 打分 → night 7 **0.017→0.017 reject**
- 结论写回 [[技能自进化闭环]]（陷阱 3 + 正确验证方法）
- 关键：`--backend claude` 只改生成不改判分；rule judge 走本地 `judges.py` 不调 LLM。真验证必须 rubric 任务 + tasks-file

## 2026-07-03 ingest | 第 4 批：Headroom + Python 包管理 + WSL/zsh

- 新源：[[Headroom - 上下文压缩代理]]、[[Python 包管理工具对比]]、[[WSL zsh 终端配置]]
- 新建实体：[[Headroom]]、[[uv]]、[[oh-my-zsh]]
- 新建概念：[[上下文压缩]]、[[Python 包管理]]、[[zsh 终端配置]]
- 主题扩展：**AI 上下文压缩**、**Python 工具链**、**终端环境**
- 关键洞察：
  - [[Headroom]] 安装命令 `uv tool install "headroom-ai[all]"` 直接依赖 [[uv]] —— 两源交叉
  - Headroom（压缩）与 [[技能自进化闭环]]（SkillOpt，固化）同属 agent 效率谱系，互补可叠加
  - uv 一个工具替代 pip + pipx + venv + pyenv，Rust 实现 10–100× 速度
  - oh-my-zsh 装完不继承 `~/.bashrc` → 已装命令 `command not found`，需手动补环境变量到 `~/.zshrc`
- 编辑判断：pip / pipx / zsh 为基线设施，折入概念页未单独建实体
- delta（同日）：`mac/技巧.md` +Spotlight（`⌘+空格`），更新 [[Mac 快捷键]]

## 2026-07-02 re-ingest | 网页 + 软件源更新

- 源笔记 delta 触发再 ingest：
  - `Resource/网页.md` 大幅扩展（1 项 → 三类导航：开发 / 娱乐 / 资讯）
  - `Resource/软件.md` OrbStack 链接拼写错误 `downloa`→`download` 已修正
- 重命名：`[[开发网页工具]]` → **[[常用网址导航]]**（反映扩展后范围）
- 新建实体：[[千问]]、[[ChatGPT]]、[[HelloGitHub]]、[[科技爱好者周刊]]
- 新建概念：[[AI 对话网页]]、[[技术资讯订阅]]
- 关键洞察：
  - 千问网页账号 ≠ App 账号（源笔记明确）
  - ChatGPT 免费版每日限额体验最新模型，超额降级
  - OrbStack 拼写错误已被用户修正 → `!warning` 转为 `!note` 已修正提示

## 2026-07-02 第 3 批 ingest

- 新源：[[浏览器插件清单]]、[[跨平台软件清单]]
- 核心新页：[[暴力猴]]、[[沉浸式翻译]]、[[AdGuard]]、[[gopeed]]、[[v2rayN]]、[[clash-verge]]、[[legado]]、[[浏览器扩展]]、[[翻墙代理工具]]
- 主题扩展：**浏览器扩展**（Edge 侧）+ **跨平台软件**（下载 / 代理 / 阅读）
- 关键洞察：
  - 暴力猴无账号同步 → 换机需重装脚本
  - legado（开源阅读）原仓库因法律纠纷清空，当前用社区 fork `legado-with-MD3`
  - v2rayN vs clash-verge：核心引擎不同（V2Ray/Xray vs mihomo），clash-verge 颜值优
  - OrbStack 链接 `downloa` 拼写错误在第二份源笔记中重现，已交叉引用 [[Mac 开发软件 - 容器]] 首次记录（后于本次 re-ingest 修正）

## 2026-07-01 第 2 批 ingest

- 新源：[[SkillOpt - 技能自进化插件]]、[[常用网址导航]]（原名「开发网页工具」）
- 核心新页：[[SkillOpt]]、[[技能自进化闭环]]、[[zread]]
- 主题扩展：**AI 插件**（技能自进化）+ **开发网页工具**
- 关键洞察：SkillOpt 即本 vault 实测工具；闭环陷阱（observer 噪声、mock 无改进）已写入 [[技能自进化闭环]]
- 源笔记多处拼写错误（instll/havest/alcude）已用 `!warning` 标注

## 2026-07-01 初始 bootstrap + 第 1 批 ingest

- Vault scaffold：`.vault-meta/`（transport=**filesystem**, mode=**generic**）、`.raw/`、`wiki/`
- 第 1 批源：[[Mac 技巧 - 快捷键]]、[[Mac 开发软件 - 容器]]
- 核心页：[[Mac 快捷键]]、[[OrbStack]]、[[开发容器]]
- 跳过 `欢迎.md`（Obsidian 样板）
- OrbStack 下载链接源笔记拼错，已标注
