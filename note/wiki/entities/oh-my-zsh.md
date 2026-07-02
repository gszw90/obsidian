---
title: oh-my-zsh
type: entity
category: 工具
created: 2026-07-03
updated: 2026-07-03
tags: [entity, tool, zsh, terminal, framework]
---

# oh-my-zsh

社区驱动的 **zsh 配置框架**。管理主题、插件、补全，简化 zsh 定制。

## 安装

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

插件目录：`${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/`。

## 注意

> [!warning] 不继承 bashrc
> 切到 zsh 后 `~/.bashrc` 的环境变量不再加载，已装命令可能 `command not found`（如 `claude`）。需手动把环境变量（含 `~/.local/bin`）补进 `~/.zshrc`。

## 相关

- 概念：[[zsh 终端配置]]
- 源笔记：[[WSL zsh 终端配置]]
- 仓库：https://github.com/ohmyzsh/ohmyzsh
