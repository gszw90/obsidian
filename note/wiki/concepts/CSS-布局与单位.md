---
title: CSS 布局与单位
aliases: [CSS 布局与单位]
type: concept
created: 2026-07-11
updated: 2026-07-11
tags: [前端, CSS, 布局, 概念]
---

# CSS 布局与单位

CSS 页面构建两大支柱：**尺寸单位** + **布局模式**。

## 单位

| 单位 | 含义 | 相对基准 |
|------|------|----------|
| px | 绝对像素 | — |
| em | 相对字体 | font-size→父元素；margin/padding→自身字体 |
| rem | root em | html root 字体 |
| vw / vh | 视口 1% | 视口宽 / 高 |
| vmin / vmax | vw/vh 取小 / 取大 | 视口 |
| dvh | 动态视口高 | 视口（动态） |
| svh / lvh | 最小 / 最大视口高 | 工具栏展开 / 收起 |

> [!key-insight] 移动端优先 dvh / svh / lvh，规避地址栏伸缩遮挡——`100vh` 在移动端常超出可见区，导致底部内容被地址栏盖住。

## 布局

### flex（一维）

`display:flex` 让子元素进入 flex 布局。核心 `flex: <grow> <shrink> <basis>`：

- `flex: 1` → `1 1 0%`：平分剩余空间
- `flex: none` → `0 0 none`：不伸缩
- `flex: auto` → `1 1 auto`：按内容伸缩 + 平分剩余
- `flex: initial` → `0 1 auto`：可缩不可放（默认行为）

### grid（二维）

`display:grid` 同时控制行与列。命名布局：

```css
.parent { display: grid;
  grid-template-areas:
    "header header"
    "aside main"
    "footer footer";
  grid-template-columns: 50px 1fr;
  grid-template-rows: auto 1fr auto;
}
.parent .child1 { grid-area: header; }  /* 命名须与 template 完全一致 */
```

### gap

子元素间隔，**仅 flex / grid 生效**。单值同行列间距；双值 `gap: <行间距> <列间距>`。

## 关联

- 来源：[[HTML CSS 基础]]
- 待扩展：响应式断点、CSS 变量、容器查询（container queries）
