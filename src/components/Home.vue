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
        <li class="list-item tool" @click="selectPage(6)">
          <img :src="`${baseUrl}img/tool.png`">
          工具
        </li>
      </ul>
    </aside>
    <main>
      <to-do v-if="pageType === 0"></to-do>
      <tool v-if="pageType === 6"></tool>
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
            { text: "简历", icon: "./img/page.png", id: 1 },
            { text: "周报", icon: "./img/week.png", id: 2 }
          ]
        },
        {
          title: "个人",
          icon: "./img/user.png",
          item: [
            { text: "to-do", icon: "./img/to-do.png", id: 3 },
            { text: "随笔", icon: "./img/article.png", id: 4 },
            { text: "111", icon: "./img/private.png", id: 5 }
          ]
        }
      ],
      pageType: 0
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
</style>
