<template>
	<div class="container" :style="{ height: height }">
		<navigate :list="list" @selectPage="selectPage"></navigate>
		<main class="main">
			<iframe
				class="to-do"
				v-for="(item, index) in tools"
				:key="index"
				v-show="index === pageType"
				:src="item"
				:height="height"
				:scrolling="index === 2 ? 'auto' : 'no'"
			></iframe>
		</main>
		<today></today>
		<div class="pet"></div>
	</div>
</template>

<script>
	import Navigate from "components/base/nav";
	import Today from "components/base/today";
	import list from "common/js/side-bar-config";
	export default {
		name: "Home",
		components: { Navigate, Today },
		data() {
			return {
				pet: "./img/pet.png",
				list,
				tools: [
					"http://mubu.com/edit/ajxMpEmB-V",
					"http://www.json.cn/",
					"https://canace.site/",
					"https://canace22.github.io/mora/",
					"https://canace22.github.io/calculate/"
				],
				pageType: 0,
				height: `${window.innerHeight}px`
			};
		},
		methods: {
			selectPage(type) {
				this.pageType = type;
			}
		}
	};
</script>

<style lang="scss" scoped>
	.container {
		position: relative;
		margin: 0;
		padding: 0;
		width: 100%;
		.main {
			display: flex;
			justify-content: center;
			align-items: center;
		}
		.pet {
			position: fixed;
			bottom: 10px;
			width: 300px;
			height: 300px;
			background: url(../../public/img/pet.png);
			background-size: 100% 100%;
			animation: playX 2s steps(3) infinite;
		}
	}

	.to-do {
		width: 100%;
		border: none;
	}

	@keyframes playX {
		from {
			background-position-y: 0px;
			// background: url(../../public/img/pet.png) !important;
		}
		20% {
			background-position-y: 5px;
		}
		30% {
			background-position-y: 8px;
		}
		50% {
			background-position-y: 10px;
		}
		60% {
			background-position-y: 8px;
		}
		80% {
			background-position-y: 5px;
		}
		to {
			background-position-y: 0px;
			// background: url(../../public/img/pet1.png) !important;
		}
	}
</style>
