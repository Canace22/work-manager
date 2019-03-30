<template>
  <div class="container" :style="{height: h}">
    <aside>
      <header>
        <img class="logo" :src="`${baseUrl}img/home.png`">LYP - OA
      </header>
      <ul class="list">
        <li class="list-item" v-for="(item, index) in list" :key="index">
          <img :src="item.icon">
          {{item.title}}
          <ul class="work-list">
            <li
              class="work-list-item"
              v-for="(value, num) in item.item"
              :key="num"
              @click="selectPage(value.id)"
            >
              <img :src="value.icon">
              {{value.text}}
            </li>
          </ul>
        </li>
      </ul>
    </aside>
    <main>
      <iframe
        class="to-do"
        v-for="(item,index) in tools"
        :key="index"
        v-show="index===pageType"
        :src="item"
        :height="h"
        :scrolling="index===2?'auto':'no'"
      ></iframe>
    </main>
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {
    ToDo: () => import("./ToDo.vue"),
    Tool: () => import("./Tool.vue")
  },
  data() {
    return {
      baseUrl: "./",
      h: `${window.innerHeight}px`,
      list: [
        {
          title: "工作",
          icon: "./img/work.png",
          item: [
            { text: "to-do", icon: "./img/to-do.png", id: 0 },
            { text: "笔记", icon: "./img/article.png", id: 1 }
          ]
        },
        {
          title: "个人",
          icon: "./img/user.png",
          item: [{ text: "博客", icon: "./img/article.png", id: 2 }]
        }
      ],
      pageType: 0,
      h: `${window.innerHeight}px`,
      tools: [
        "https://mubu.com/edit/ajxMpEmB-V",
        "https://dillinger.io/",
        "https://canace.site/"
      ]
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
ul,
li {
  list-style: none;
}
.container {
  position: relative;
  margin: 0;
  padding: 0;
  width: 100%;
  aside {
    position: relative;
    width: 20%;
    height: 100%;
    float: left;
    background: rgb(79, 145, 231);
    header {
      .logo {
        margin-right: 0.625rem;
      }
      color: #fff;
      font-weight: 700;
      font-size: 2rem;
      font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
      opacity: 0.5;
      padding: 10px;
    }
    .list {
      padding: 0;
      .list-item {
        cursor: pointer;
        line-height: 2.5rem;
        padding-left: 20px;
        margin: 5px 0;
        font-weight: 500;
        font-size: 1.125rem;
        color: rgb(235, 220, 220);
      }
      .tool:hover {
        background: rgb(13, 109, 165);
        opacity: 0.8;
      }
    }
  }
  main {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

.list-item {
  .work-list {
    padding-left: 1.25rem;
    .work-list-item {
      &:hover {
        background: rgb(13, 109, 165);
        opacity: 0.8;
      }
    }
  }
}
.to-do {
  width: 100%;
  border: none;
}
</style>
