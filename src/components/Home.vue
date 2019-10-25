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
    <div class="pet"></div>
    <!-- <img class="pet" :src="pet" draggable="false" /> -->
  </div>
</template>

<script>
const Navigate = () => import("./base/nav.vue");
export default {
  name: "Home",
  components: { Navigate },
  data() {
    return {
      pet: "./img/pet.png",
      list: [
        {
          title: "工具",
          icon: "./img/work.svg",
          item: [
            { text: "to-do", icon: "./img/to-do.svg", id: 0 },
            { text: "json-parse", icon: "./img/json.svg", id: 1 }
          ]
        },
        {
          title: "资料",
          icon: "./img/data.svg",
          item: [
            { text: "博客", icon: "./img/blog.svg", id: 2 }
            // { text: "lodash", icon: "./img/mdn.svg", id: 3 }
          ]
        },
        {
          title: "减压",
          icon: "./img/find.svg",
          item: [
            { text: "猜拳大战", icon: "./img/mora.svg", id: 3 },
            { text: "计算器", icon: "./img/cal.svg", id: 4 }
          ]
        }
      ],
      tools: [
        "http://mubu.com/edit/ajxMpEmB-V",
        "http://www.json.cn/",
        "https://canace.site/",
        "https://canace22.github.io/mora/",
        "https://canace22.github.io/calculate/"
      ],
      pageType: 0,
      height: `${window.innerHeight}px`,
      day: 0,
      hour: 0,
      minute: 0,
      second: 0
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

