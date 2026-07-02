---
title: Headroom
type: entity
category: 工具
created: 2026-07-03
updated: 2026-07-03
tags: [entity, tool, ai, llm, open-source]
---

# Headroom

开源 **AI 上下文压缩层**。部署在 Agent/应用与 LLM 提供商之间，拦截每条消息在抵达模型前压缩 60%–95%，本地运行，可逆。

## 形态

- Python 库
- 即插即用代理（`headroom proxy`）
- MCP 服务器
- TypeScript SDK

## 定位

解决 `claude code` / `codex` 等工具输出冗余导致的 token 紧张、费用上升、上下文填满。拦截 API → 压缩 → 调用 → 度量入库 → 原样返回。

## 安装

```bash
uv tool install "headroom-ai[all]"   # 依赖 [[uv]]
```

## 用法

| 场景 | 命令 |
|---|---|
| 包裹官方模型 | `headroom wrap claude` / `headroom wrap codex` |
| 取消包裹 | `headroom unwrap claude` |
| 第三方端点（如 glm） | `headroom proxy --port 8787 --anthropic-api-url <url>` + 改 `ANTHROPIC_BASE_URL` |

## 相关

- 概念：[[上下文压缩]]
- 源笔记：[[Headroom - 上下文压缩代理]]
- 同主题工具：[[技能自进化闭环]]（SkillOpt）
- 仓库：https://github.com/headroomlabs-ai/headroom
