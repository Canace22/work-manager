<template>
	<div class="calendar">
		<p class="item">{{ day.month + day.date }}</p>
	</div>
</template>

<script>
	export default {
		name: "today",
		data() {
			return {
				day: {}
			};
		},
		created() {
			const date = new Date();
			this.day = {
				month: `${date.getMonth() + 1}月`,
				date: `${date.getDate()}日`
			};
		}
	};
</script>

<style lang="scss" scoped>
	.calendar {
		position: absolute;
		bottom: 40%;
		right: 10px;
		display: flex;
		justify-content: center;
		align-items: flex-end;
		width: 128px;
		height: 128px;
		background: url("../../../public/img/calendar.png") no-repeat;
		background-size: 100% 100%;
		.item {
			color: #14aef0;
			font-weight: 700;
			font-size: 28px;
		}
	}
</style>