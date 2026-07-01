---
title: 日志
type: log
created: 2026-07-01
updated: 2026-07-02
---

# 日志

Ingest 操作记录。新条目置顶。

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
