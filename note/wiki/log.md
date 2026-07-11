---
title: 日志
type: log
created: 2026-07-01
updated: 2026-07-11
---

# 日志

Ingest 操作记录。新条目置顶。

## 2026-07-11 ingest | GitHub Trending 月度追踪启动

- 触发：用户要求每月拉取 github trending 记录趋势，原始数据存 `note/Github/Trending/`，按月文件
- 采集：`firecrawl scrape "github.com/trending?since=monthly"`（stars/月）+ `gh api repos/<o>/<r>` × 20（描述/语言/topics/license）→ `gh` 已 auth（gszw90）
- 原始数据：`note/Github/Trending/2026-07.md`（20 仓库表 + 领域/语言分布）+ `2026-07-raw.jsonl`
- 新建：[[GitHub Trending 月榜 2026-07]]（source）、[[GitHub Trending 月度追踪]]（concept，追踪机制 + 月度索引 + 分类法）、[[Apple Container]]（entity）
- 主题：**AI agent 基础设施爆发**——20 席 65% AI，agent 编排/MCP/网关/多路复用占近半
- 编辑判断：20 仓库仅建 1 实体（apple/container，强关联 [[OrbStack]]/[[开发容器]]）；其余折入表，避免月月 ×N 实体维护负担
- 自动化：durable cron `7 3 1 * *`（每月 1 日 3:07），prompt 复跑采集+ingest 流程
- 结构性：新增第 4 数据根 `note/Github/Trending/`（外部自动采集，区别于 Develop/Mac/Resource 个人笔记）
- 路径教训：zsh 不做 `$VAR` 词分割（`for r in $repos` 失败）→ 显式列表；CJK 路径 + WSL 偶发丢目录 → 全用绝对路径

## 2026-07-11 ingest | 第 5 批：HTML+CSS + 两本参考书 stub

- 来源：`Develop/前端/html + css.md`、`Resource/pdf/Python学习手册（原书第4版）.pdf`、`Resource/pdf/kubernetes-book-jimmysong-v20250804.pdf`
- 新建来源页：[[HTML CSS 基础]]、[[Python 学习手册（第4版）]]、[[Kubernetes book（Jimmy Song）]]
- 新建概念页：[[CSS 布局与单位]]
- 主题扩展：**前端 / CSS**（首次入 vault）、**参考书籍**存根
- 编辑判断：
  - HTML/CSS 折入 1 概念页（[[CSS 布局与单位]]），不单独建实体（基线设施，同 pip/zsh 折叠惯例）
  - 两本 PDF 教材做**书籍参考 stub**（仅书目存根，不做概念抽取）——书太厚全量 ingest 不经济，按需再抽
- 关键洞察：
  - 移动端用 dvh/svh/lvh 替代 vh，规避地址栏伸缩遮挡
  - Kubernetes（编排）在 OrbStack（单机容器）之上一层的抽象层次
- 路径波折：源 PDF 初始在 `Develop/资源/`，ingest 中途被移至 `Resource/pdf/`（用户整理）；CJK 路径 zsh 下需 Python glob 探测
- 源笔记纠错：`grid-area: heder`→`header`、`vmin/vmax` 注释 `vm`→`vw`

## 2026-07-03 update | SkillOpt-Sleep rule judge 假阳性实证

- 触发：用户要求「真正得到验证」night 6 的 0.050→0.550 accept 结果
- 调查：`replay.py:50-54` 显示 `reference_kind="rule"` 任务走本地 `judges.py`（regex/contains/section_present，**不调 LLM**）；`--backend claude` 只改 `backend.attempt` 生成，不改判分
- 矿工 `llm_miner.py:36-46` prompt 偏向程序化 checks → 几乎所有任务成 rule judge → 默认无法真验证
- 真验证路径：`--tasks-file` 注入手写 `reference_kind="rubric"` 任务 → `replay.py` 改走 `backend.judge()` = `ClaudeBackend.judge()` 真 LLM 打分
- 实测 night 7：held-out 0.017 → 0.017，**reject**。对比 night 6 的假阳性 accept
- 更新：[[技能自进化闭环]] 陷阱节扩展（陷阱 3 + A/B 表）+ 新增「正确验证方法」节（含可复现命令）
- 暂存两份（night6 `20260703-022027` / night7 `20260703-023236`）均未 adopt，线上 CLAUDE.md/SKILL.md 未动

## 2026-07-03 re-ingest | delta：技巧.md 增 Spotlight

- 触发：`mac/技巧.md` hash 变更（`89cf3e40…` → `d6b8ad15…`），+3 行
- 新增：`# 搜索` section，`command + space`（Spotlight）
- 更新：[[Mac 快捷键]]（表格 +1 行，待补充 Spotlight→Launchpad）、[[Mac 技巧 - 快捷键]]（表格 +1 行，新增「搜索」小节）
- 无新建页；无矛盾

## 2026-07-03 ingest | 第 4 批：Headroom + Python 包管理 + WSL/zsh

- Source 7: `Develop/Ai/Plugin/headroom.md` → [[Headroom - 上下文压缩代理]]
  - 创建：[[Headroom]]（实体）、[[上下文压缩]]（概念）
  - AI 上下文压缩代理：拦截 LLM API 调用，压缩 60%–95%，本地可逆；Python 库 / 代理 / MCP / TS SDK
- Source 8: `Develop/Python/包管理工具.md` → [[Python 包管理工具对比]]
  - 创建：[[uv]]（实体）、[[Python 包管理]]（概念）
  - pip / pipx / uv 三层对比；uv（Rust）10–100× pip，替代 pip+pipx+venv+pyenv
- Source 9: `Develop/环境/wsl.md` → [[WSL zsh 终端配置]]
  - 创建：[[oh-my-zsh]]（实体）、[[zsh 终端配置]]（概念）
  - zsh + oh-my-zsh + autosuggestions/syntax-highlighting + Nerd Fonts
- 新建页：9（3 source + 3 entity + 3 concept）；更新页：5（index/overview/hot/log/manifest）
- 编辑判断（ACCEPT）：pip / pipx / zsh 为基线设施，折入概念页对比，未单独建实体
- 关键发现 / 交叉引用：
  - [[Headroom]] 安装 `uv tool install "headroom-ai[all]"` 直接依赖 [[uv]] —— 两源强交叉
  - [[上下文压缩]]（Headroom）↔ [[技能自进化闭环]]（SkillOpt）同属 agent 效率谱系：压缩省输入带宽，固化省重复推理，互补可叠加
  - oh-my-zsh 不继承 `~/.bashrc` → 切换后已装命令 `command not found`，需补环境变量（含 `~/.local/bin`）到 `~/.zshrc`

## 2026-07-02 re-ingest | 源笔记 delta：网页 + 软件

- 触发：`.raw/.manifest.json` hash 校验发现两源变更
- Source `Resource/网页.md`（hash `533eacfd…` → `d7b07fdb…`）：
  - 内容由 1 项（zread）扩展为三类导航：开发（zread / 千问 / ChatGPT）、娱乐（age 动漫 / 次元城 / 稀饭动漫）、资讯（HelloGitHub / 科技爱好者周刊 / infinitum）
  - 源页重命名：`开发网页工具.md` → **`常用网址导航.md`**（git mv 保留历史）
  - 新建实体：[[千问]]、[[ChatGPT]]、[[HelloGitHub]]、[[科技爱好者周刊]]
  - 新建概念：[[AI 对话网页]]、[[技术资讯订阅]]
  - 娱乐站点（动漫）体量小且灰度，仅入源表未建实体（ACCEPT 编辑判断）
- Source `Resource/软件.md`（hash `4ac1af9a…` → `574f21e6…`）：
  - OrbStack 链接拼写错误 `downloa`→`download` 已被用户修正
  - 更新 [[跨平台软件清单]]：`!warning` 转为 `!note` 已修正提示
- 新建页：6（4 entity + 2 concept）；重命名 1；更新页：7（源页 + zread + 浏览器扩展 + 浏览器插件清单 + index/overview/hot/log）
- 反向链接迁移：`[[开发网页工具]]` → `[[常用网址导航]]`（全 wiki 6 处）
- 关键发现：
  - 千问网页账号与 App 不相通（源笔记明确）
  - ChatGPT 免费版每日限额体验最新模型，超额降级到低版本
  - 用户已自行修正 OrbStack 拼写错误 → wiki 内嵌警告转为「已修正」状态

## 2026-07-02 ingest | 第 3 批：浏览器插件 + 跨平台软件

- Source 5: `Resource/浏览器插件.md` → [[浏览器插件清单]]
  - 创建：[[暴力猴]]、[[沉浸式翻译]]、[[AdGuard]]（实体）、[[浏览器扩展]]（概念）
  - Infinity / JSON 格式化工具体量小，仅入源表未单独建实体（ACCEPT 编辑判断）
- Source 6: `Resource/软件.md` → [[跨平台软件清单]]
  - 创建：[[gopeed]]、[[v2rayN]]、[[clash-verge]]、[[legado]]（实体）、[[翻墙代理工具]]（概念）
  - 更新：[[OrbStack]]（追加来源交叉引用）
- 新建页：11（2 source + 7 entity + 2 concept）；更新页：5（OrbStack + index/overview/hot/log）
- 关键发现：
  - legado 原仓库因法律纠纷被作者清空，当前链接为社区 fork `HapeLee/legado-with-MD3`
  - 暴力猴无账号同步功能（源笔记明确标注）
  - OrbStack `downloa` 拼写错误在第二份源笔记重现，交叉引用首次记录而非重复标注
- 交叉引用：[[浏览器扩展]] ↔ [[常用网址导航]]（同为浏览器侧工具）；[[翻墙代理工具]] 串联 [[v2rayN]]↔[[clash-verge]]

## 2026-07-01 ingest | 第 2 批：SkillOpt + 网页工具

- Source 3: `Develop/Ai/Plugin/SkillOpt.md` → [[SkillOpt - 技能自进化插件]]
  - 创建：[[SkillOpt]]（实体）、[[技能自进化闭环]]（概念）
  - 修正源笔记拼写：instll/havest/alcude
- Source 4: `Resource/网页.md` → [[常用网址导航]]（原名「开发网页工具」，后因源扩展重命名）
  - 创建：[[zread]]（实体）
- 新建页：5（2 source + 2 entity + 1 concept）
- 关联：开发工具域串联（[[OrbStack]] ↔ [[zread]]）；SkillOpt 即本 vault 实测工具，闭环陷阱已记录

## 2026-07-01 ingest | 批量 ingest 现有笔记

- Source 1: `mac/技巧.md` → [[Mac 技巧 - 快捷键]]
  - 创建：[[Mac 快捷键]]（概念）
- Source 2: `mac/软件.md` → [[Mac 开发软件 - 容器]]
  - 创建：[[OrbStack]]（实体）、[[开发容器]]（概念）
- 跳过：`欢迎.md`（Obsidian 默认样板，无价值）
- 交叉引用：mac 开发工具主题串联（[[Mac 快捷键]] ↔ [[OrbStack]]）
- 关键发现：源笔记 OrbStack 链接有拼写错误（`downloa` → `download`），已在 source 页用 `!warning` 标注
- 新建页：5（2 source + 2 concept + 1 entity）；更新页：0

## 2026-07-01 bootstrap | 初始化 wiki scaffold

- 创建 `.vault-meta/`（transport.json = filesystem, mode.json = generic）
- 创建 `wiki/` 结构：sources / entities / concepts / domains / folds
- 创建元页面：overview, index, hot, log
- 创建 `.raw/.manifest.json`（delta 跟踪）
- 备注：`欢迎.md` 为 Obsidian 默认样板，未 ingest
