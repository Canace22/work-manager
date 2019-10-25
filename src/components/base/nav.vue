<template>
  <aside class="aside">
    <header class="header">
      <img class="logo" :src="`${baseUrl}img/home.svg`" />LYP - OA
    </header>
    <ul class="list">
      <li class="list-item" v-for="(item, index) in list" :key="index">
        <div class="list-header">
          <img class="icon" :src="item.icon" />
          {{ item.title }}
        </div>
        <ul class="work-list">
          <li
            class="work-list-item"
            v-for="(value, num) in item.item"
            :key="num"
            @click="$emit('selectPage', value.id)"
          >
            <img class="icon" :src="value.icon" />
            <span>{{ value.text }}</span>
          </li>
        </ul>
      </li>
    </ul>
    <footer class="footer">
      本周剩余
      <span class="day">{{ day }}</span>
      天
    </footer>
  </aside>
</template>

<script>
export default {
  name: "navigate",
  props: {
    list: Array
  },
  data() {
    return {
      baseUrl: "./",
      day: 0,
      hour: 0,
      min: 0,
      second: 0
    };
  },
  // computed: {
  //   time() {
  //     return `${this.day} 天 ${this.hour} 小时 ${this.min} 分 ${this.second} 秒`;
  //   }
  // },
  created() {
    this.timer();
  },
  methods: {
    timer() {
      const date = new Date();

      this.day = 7 - date.getDay();
    }
  }
};
</script>

<style lang="scss" scoped>
.aside {
  position: relative;
  float: left;
  width: 21.875rem;
  height: 100%;
  background: #14aef0;
  .header {
    display: flex;
    align-items: center;
    color: #fff;
    font-weight: 700;
    font-size: 2rem;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    padding: 10px;
    padding-left: 20px;
    opacity: 0.8;
    .logo {
      margin-right: 10px;
    }
  }
  .list {
    padding: 0;
    .list-header {
      display: flex;
      align-items: center;
      .icon {
        width: 28px;
        height: 28px;
        padding-right: 10px;
        opacity: 0.8;
      }
    }
    .list-item {
      line-height: 2.5rem;
      color: rgb(235, 220, 220);
      font-weight: 500;
      font-size: 1.125rem;
      margin: 5px 0;
      padding-left: 20px;
      cursor: pointer;
      .work-list {
        padding-left: 1.25rem;
        .work-list-item {
          display: flex;
          align-items: center;
          .icon {
            margin-right: 10px;
          }
          &:hover {
            background: rgb(13, 109, 165);
            opacity: 0.8;
          }
        }
      }
    }
    .tool:hover {
      background: rgb(13, 109, 165);
      opacity: 0.8;
    }
  }
  .footer {
    position: absolute;
    bottom: 0;
    color: #fff;
    margin: auto;
    padding: 20px;
    .day {
      font-size: 20px;
      color: yellow;
      padding: 2px 10px;
      margin: 0 5px;
      border: 1px solid rgb(235, 220, 220);
    }
  }
}
</style>
<style scoped>
ul,
li {
  list-style: none;
}
</style>
