---
title: zsh 终端配置
aliases: [zsh 终端配置]
type: concept
created: 2026-07-03
updated: 2026-07-03
tags: [concept, terminal, zsh, wsl]
---

# zsh 终端配置

WSL/Linux 下用 [[oh-my-zsh]] + 插件打造高效终端。核心三件套：自动提示、语法高亮、Nerd Font。

## 组件

- [[oh-my-zsh]] —— zsh 配置框架
- **zsh-autosuggestions** —— 历史命令灰色提示
- **zsh-syntax-highlighting** —— 实时语法着色
- **Nerd Fonts** —— 图标字体，防乱码

## 配置点

`~/.zshrc`：
```text
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

> [!warning] 环境变量断层
> oh-my-zsh 不读 `~/.bashrc`。装完若 `command not found`，把 bashrc 的环境变量（含 `~/.local/bin`）补进 `~/.zshrc` 末尾。

## 相关

- 源笔记：[[WSL zsh 终端配置]]
- 实体：[[oh-my-zsh]]
