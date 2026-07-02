---
title: Python 包管理
aliases: [Python 包管理]
type: concept
created: 2026-07-03
updated: 2026-07-03
tags: [concept, python, tooling]
---

# Python 包管理

Python 生态的依赖 / 工具 / 解释器版本管理。三大工具分层：项目依赖、全局 CLI 应用、全能型。

## 工具谱

- **pip** —— 官方项目依赖（慢、不隔离）
- **pipx** —— 全局 CLI 应用（隔离、仅限可执行工具）
- [[uv]] —— Rust 全能型，替代上述全部 + venv + pyenv（推荐）

详见 [[Python 包管理工具对比]]。

## 关键判断

- 装项目依赖 → `uv pip install` 或 `pip`
- 装终端工具（black/ruff）→ `uv tool install` 或 `pipx`
- 建 venv → `uv venv`
- 管 Python 版本 → `uv python install 3.12`

> [!key-insight] 隔离是核心
> 不隔离直接全局装包 → 项目间依赖冲突（A 要 requests==2.0，B 要 3.0）。venv / pipx / uv tool 都为隔离而生。

## 相关

- [[Python 包管理工具对比]]、[[uv]]
- 应用实例：[[Headroom]]（`uv tool install`）
