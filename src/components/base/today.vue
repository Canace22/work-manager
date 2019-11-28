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
		top: 10%;
		right: 6%;
		display: flex;
		justify-content: center;
		align-items: flex-end;
		width: 128px;
		height: 128px;
		background: url("../../../public/img/calendar.png") no-repeat;
		background-size: 100% 100%;
		transform: scale(0.5);
		.item {
			color: #14aef0;
			font-weight: 700;
			font-size: 28px;
		}
	}
</style>