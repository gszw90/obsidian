---
title: 热缓存
type: hot
created: 2026-07-01
updated: 2026-07-02
---

# 热缓存

最近 ingest 上下文。下次会话先读这里，避免重读全页。

## 2026-07-02 re-ingest | 网页 + 软件源更新（最新）

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
