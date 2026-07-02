---
title: uv
type: entity
category: 工具
created: 2026-07-03
updated: 2026-07-03
tags: [entity, tool, python, rust, package-manager]
---

# uv

Rust 编写的极速、全能型 **Python 包与项目管理工具**。安装与依赖解析比 pip 快 10–100×。一个工具替代 pip + pipx + venv + pyenv。

## 替代映射

| 替代对象 | uv 命令 |
|---|---|
| pip | `uv pip install requests` |
| pipx | `uv tool install black` |
| venv | `uv venv` |
| pyenv | `uv python install 3.12` |

## 典型用法

```bash
uv pip install -r requirement.txt   # 项目依赖
uv tool install ruff                # 全局 CLI 工具（自带 venv）
uv run --with requests script.py    # 一次性脚本，自动装依赖
```

## 相关

- 概念：[[Python 包管理]]
- 对比：[[Python 包管理工具对比]]
- 被依赖实例：[[Headroom]] —— `uv tool install "headroom-ai[all]"`
