---
title: Python 包管理工具对比
aliases: [Python 包管理工具对比]
type: source
source: Develop/Python/包管理工具.md
created: 2026-07-03
updated: 2026-07-03
tags: [source, python, package-management]
---

# Python 包管理工具对比

源笔记：`Develop/Python/包管理工具.md`

## 三者定位

| 工具 | 定位 | 隔离 | 速度 |
|---|---|---|---|
| **pip** | 项目依赖安装 | 无（靠 venv） | 慢（纯 Python） |
| **pipx** | 全局 CLI 应用 | 每应用独立 venv | 中 |
| [[uv]] | 全能型（包+项目+版本） | 内建 | 极快（Rust，10–100× pip） |

## pip

官方依赖管理。装到当前激活 venv 或全局。
- 痛点：慢、不隔离（不配 venv 易冲突）、只管装包不管建环境。
```bash
pip install requests
```

## pipx

专装终端全局 CLI 工具（`black`、`ruff`、`httpie`）。每应用独立 venv，可执行文件链到 `~/.local/bin`，解决全局冲突。**仅限可执行工具，不管理项目依赖。**
```bash
pipx install httpie
```

## uv

Rust 写的全能工具，10–100× pip 速度。一个工具替代 pip + pipx + venv + pyenv：

| 替代 | 命令 |
|---|---|
| pip | `uv pip install requests` |
| pipx | `uv tool install black`（自带 venv） |
| venv | `uv venv`（秒建） |
| pyenv | `uv python install 3.12`（管版本） |

```bash
uv pip install -r requirement.txt   # 项目依赖
uv tool install ruff                # 全局工具
uv run --with requests script.py    # 一次性脚本，自动处理依赖
```

> [!key-insight] uv 是当前首选
> pip 与 pipx 的所有场景 uv 都覆盖且更快。新项目直接用 uv。

## 相关

- 概念：[[Python 包管理]]
- 实体：[[uv]]
- 交叉：[[Headroom]] 安装即 `uv tool install "headroom-ai[all]"`
