---
title: WSL zsh 终端配置
aliases: [WSL zsh 终端配置]
type: source
source: Develop/环境/wsl.md
created: 2026-07-03
updated: 2026-07-03
tags: [source, wsl, zsh, terminal]
---

# WSL zsh 终端配置

源笔记：`Develop/环境/wsl.md`

## 流程

1. 装 zsh + git：`sudo apt install zsh git -y`
2. 装 [[oh-my-zsh]]：
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
3. 装插件（克隆到 `${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/`）：
   - **zsh-autosuggestions** —— 自动提示
   - **zsh-syntax-highlighting** —— 语法高亮
4. 启用：编辑 `~/.zshrc`，`plugins=(git zsh-autosuggestions zsh-syntax-highlighting)`，`source ~/.zshrc`。

## 字体

[Nerd Fonts](https://www.nerdfonts.com/font-downloads) 防乱码。下载 → 解压 → 装 `.ttf` → Windows Terminal 设置 → 配置文件 → Ubuntu → 外观 → 字体改之。

## 坑

> [!warning] oh-my-zsh 装完部分命令丢失
> 现象：`zsh: command not found: claude` 等。
> 原因：oh-my-zsh 不继承 `~/.bashrc` 的环境变量。
> 解决：在 `~/.zshrc` 末尾补回 bashrc 中的环境变量，并把 `/home/<user>/.local/bin` 加入 PATH。

## 相关

- 概念：[[zsh 终端配置]]
- 实体：[[oh-my-zsh]]
