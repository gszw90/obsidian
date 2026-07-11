## 单位
* **px**：像素，固定单位
* **em**：字体大小百分比，相对单位，用在font-size表示相对于父元素的字体大小，用在margin，padding等表示相对于自身的字体大小
* **rem**：字体大小百分比，相对于html的root元素的字体大小百分比
* **vw**：浏览器宽度的1%
* **vh**：浏览器高度的1%
* **vmin**：vm与vh中取最小值
* **vmax**：vm与vh取最大值
* **dvh**：动态窗口高度，解决移动端地址栏收缩时变大，展开时变小，完美解决遮挡问题
* **svh (Small VH)**：按最小视口（工具栏展开时）计算
- **lvh (Large VH)**：按最大视口（工具栏收起时）计算
## 布局
### flex 布局

#### flex
当父级的display设置为flex时，子元素就进入了flex布局。
flex的属性：`flex: <flex-grow> <flex-shrink> <flex-basis>;`
flex-grow:放大比例，默认0，表示保持原样
flex-shrink：缩小比例，默认1，表示大家等比例缩小
flex-basis：基础尺寸，默认auto，表示按照实际宽度来计算

```css
.parent {
	display: flex
}
.parent .child {
	flex: 1 1 200px
}

.parent .child {
	/* 平分剩余空间 */
	flex: 1
	/* 完整写法 flex:1 1 0% */
}

.parent .child {
	/* 不进行伸缩 */
	/* 完整写法 flex: 0 0 none */
	flex: none
}

.parent .child {
	/* 按照内容伸缩+平分剩余空间 */
	/* 完整写法 flex: 1 1 auto */
	flex: auto
}

.parent .child {
	/* 可以缩小，不可放大 */
	/* 完整写法 flex: 0 1 auto */
	flex: initial
}

```

#### grid
网格布局，能同时控制行与列
**命名布局**
```css
.parent {
	display: grid;
	grid-template-areas:
	"header header"
	"aside main"
	"footer footer";
	/* 两列，第一列宽50px，第二列自适应 */
	grid-template-columns: 50px 1fr;
	/* 第一与第三行高度由内容撑开，第二列占用剩余空间 */
	grid-template-rows: auto 1fr auto;
}

.parent .child1{
/* 指定父级template中配置的模板名 */
	grid-area: heder
}
.parent .child2{
	grid-area: aside
}
.parent .child3{
	grid-area: main
}
.parent .child4{
	grid-area: footer
}
```

#### gap
gap表示子级两个元素的间隔，只针对flex与grid布局
```css
.parent {
	display: flex;
	/* 一个值表示行与列的间隔是一样的 */
	/* 两个值：第一个表示行间距，第二个表示列间距 */
	gap: 10px;
}
```
