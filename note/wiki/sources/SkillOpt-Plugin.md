---
title: SkillOpt - 技能自进化插件
aliases: [SkillOpt - 技能自进化插件]
type: source
source_path: Develop/Ai/Plugin/SkillOpt.md
created: 2026-07-01
updated: 2026-07-01
tags:
  - ai
  - plugin
  - skillopt
  - source
---

# SkillOpt - 技能自进化插件

> 来源：`Develop/Ai/Plugin/SkillOpt.md`

## 摘要

[[SkillOpt]] — 微软开源的 Claude Code 插件。**像训练模型一样训练 skill**：通过离线重放历史会话迭代优化 skill / memory，门控保证只保留有效改动。

- 仓库：https://github.com/microsoft/SkillOpt
- 安装文档：https://github.com/microsoft/SkillOpt/blob/main/docs/sleep/README.md

## 核心工作流程

六步闭环（详见 [[技能自进化闭环]]）：

1. **Harvest 收割** — 收集过去会话记录
2. **Mine 挖掘** — 发现反复做/反复出错的任务
3. **Replay 重放** — 离线重跑任务
4. **Reflect 反思** — 分析失败，提出规则修改
5. **Gate 门控** — 只在留出集分数确实提升时保留
6. **Stage & Adopt** — 生成提案，人工审核后采纳

## 安装

```bash
git clone git@github.com:microsoft/SkillOpt.git
cd SkillOpt
claude
# 在 claude 内：
/plugin marketplace add ./plugins/claude-code
/plugin install skillopt-sleep
/reload plugins
```

> [!warning] 源笔记拼写错误
> 原文 `instll`（应为 `install`）、`havest`（应为 `harvest`）、`alcude`（应为 `claude`）。已在此订正。

## 命令

```
/skillopt-sleep:skillopt-sleep [ run | dry-run | status | adopt | harvest | schedule | unschedule ]
```

| 命令 | 作用 |
|---|---|
| status | 历史运行次数 + 最新暂存提案（只读） |
| dry-run | 完整 harvest→mine→replay→report，**不暂存** |
| run | 完整执行并**暂存**提案，不改线上文件 |
| adopt | 暂存提案写入 `CLAUDE.md` / `SKILL.md`（自动备份） |
| harvest | 调试：打印挖掘到的重复任务 |
| schedule | 设置夜间定时任务 |
| unschedule | 移除定时任务 |

## 关联

- 实体：[[SkillOpt]]
- 概念：[[技能自进化闭环]]
- 实践记录：本 vault 已运行过 skillopt-sleep（见 `~/.skillopt-sleep/`），因 observer-session 噪声产出无效规则，已 discard
