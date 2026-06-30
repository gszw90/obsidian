---
title: SkillOpt
type: entity
entity_kind: software
category: ai-plugin
repo: https://github.com/microsoft/SkillOpt
created: 2026-07-01
updated: 2026-07-01
tags:
  - ai
  - plugin
  - claude-code
  - entity
---

# SkillOpt

微软开源的 Claude Code 插件。离线「睡眠」自进化：重放历史会话，迭代优化 skill 与 memory（`CLAUDE.md` / `SKILL.md`），门控保证只采纳有效改动。

## 关键点

- **形态**：Claude Code plugin（marketplace 可装）
- **机制**：Harvest → Mine → Replay → Reflect → Gate → Stage & Adopt（见 [[技能自进化闭环]]）
- **安全**：改动先进 staging，`adopt` 才写线上文件（自动备份）
- **后端**：`mock`（无 API 消耗）/ `claude` / `codex`

## 实践备忘

本机已装于 `/home/zeng/projects/python/SkillOpt`，需 `export SKILLOPT_SLEEP_REPO=...`。
实测陷阱：`--scope all` 会把 `~/.claude-mem/observer-sessions` 噪声纳入 harvest，挖出垃圾规则 —— 需过滤。

## 关联

- 概念：[[技能自进化闭环]]
- 来源：[[SkillOpt - 技能自进化插件]]
