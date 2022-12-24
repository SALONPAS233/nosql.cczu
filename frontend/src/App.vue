<template>
	<div>
		<div class="body">
			<router-view />
		</div>
		<div class="footer">
			<p></p>
			<p></p>
		</div>
	</div>
</template>

<style lang="less">
* {
	margin: 0;
	padding: 0;
	// 设置是多少就是多少，不会因为内边距的宽高而撑大
	box-sizing: border-box;
	font-family: "微软雅黑";
}
.footer {
	text-align: center;
	color: #999;
	margin-bottom: 0.1rem;
}
.body {
	min-height: calc(100vh - 0.62rem);;
}
</style>
