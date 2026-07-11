---
title: HTML CSS 基础
aliases: [HTML CSS 基础]
type: source
created: 2026-07-11
updated: 2026-07-11
tags: [前端, CSS, 布局, 来源]
---

# HTML CSS 基础

源笔记：`Develop/前端/html + css.md`。CSS 单位与布局速查。

## 摘要

CSS 基础两块：**单位**（尺寸度量）+ **布局**（flex / grid）。

## 关键点

### 单位

- **px**：绝对像素
- **em**：相对——`font-size` 上相对父元素字体，`margin`/`padding` 上相对自身字体
- **rem**：相对 html root 字体
- **vw / vh**：视口宽 / 高的 1%
- **vmin / vmax**：vw 与 vh 取小 / 取大
- **dvh**：动态视口高，解决移动端地址栏伸缩遮挡
- **svh / lvh**：最小 / 最大视口（工具栏展开 / 收起）

### 布局

- **flex**：一维。`flex: <grow> <shrink> <basis>`。简写 `flex:1`（平分）/ `none` / `auto` / `initial`
- **grid**：二维。`grid-template-areas` 命名布局 + `grid-template-columns/rows`
- **gap**：子元素间隔，仅 flex / grid 生效

详见 [[CSS 布局与单位]]。

## 源笔记纠错

> [!warning] 源笔记拼写错误
> - `grid-area: heder` → 应为 `header`（template 中写的是 `header`，子元素引用拼错会匹配失败）
> - `vmin/vmax` 注释 `vm与vh` → 应为 `vw与vh`
