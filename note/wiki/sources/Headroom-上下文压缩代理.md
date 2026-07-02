---
title: Headroom - 上下文压缩代理
aliases: [Headroom - 上下文压缩代理]
type: source
source: Develop/Ai/Plugin/headroom.md
created: 2026-07-03
updated: 2026-07-03
tags: [source, ai, llm, context-compression]
---

# Headroom - 上下文压缩代理

源笔记：`Develop/Ai/Plugin/headroom.md`

## 摘要

[[Headroom]] 是部署在 Agent/应用与 LLM 提供商之间的**上下文压缩层**。拦截每一条 prompt、工具输出、日志、文件、对话片段，在抵达模型前**压缩 60%–95%**，且保持回答准确率。本地运行，支持按需检索的**可逆**压缩。

交付形态：Python 库、即插即用代理、MCP 服务器、TypeScript SDK。

## 痛点

`claude code`、`codex` 等工具输出庞大，冗余数据多 → token 紧张、费用上升、上下文填满。Headroom 拦截 API 调用，跑变换流水线压缩消息，度量入库，原样返回响应。

## 安装

```bash
uv tool install "headroom-ai[all]"
```

> [!key-insight] 依赖 [[uv]]
> 安装命令用 `uv tool install` —— 与 [[Python 包管理]] 中 uv 取代 pipx 的定位一致。

## 启动模式

**原生 wrap（claude code / codex 直连官方模型）**
```bash
headroom wrap claude
headroom wrap codex
headroom unwrap claude   # 取消
```

**组装：claude code + glm 第三方模型**
1. 起代理：
```bash
headroom proxy --port 8787 --anthropic-api-url https://open.bigmodel.cn/api/anthropic
```
2. 改 `~/.claude/settings.json`：
```json
{ "env": { "ANTHROPIC_BASE_URL": "127.0.0.1:8787" } }
```
3. 直接 `claude` 启动。

## 相关

- 概念：[[上下文压缩]]
- 实体：[[Headroom]]、[[uv]]
- 同主题：[[技能自进化闭环]]（SkillOpt —— 同为 AI agent 效率工具，压缩 vs 技能固化互补）
- 文档：[GitHub](https://github.com/headroomlabs-ai/headroom)、[简介](https://headroomlabs-ai.github.io/headroom/)、[原理](https://headroomlabs-ai.github.io/headroom/ARCHITECTURE/)
