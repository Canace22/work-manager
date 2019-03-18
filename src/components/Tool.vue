<template>
  <div class="wrap" :style="{height: h}">
    <h1>TOOL</h1>
    <section class="urlMap">
      <a
        v-for="(item, index) in urlMap"
        :key="index"
        :href="item.url"
        target="“_blank”"
      >{{item.name}}</a>
    </section>
    <footer></footer>
  </div>
</template>
<script>
import http from "@/common/serve.js";

export default {
  name: "ToDo",
  data() {
    return {
      h: `${window.innerHeight}px`,
      urlMap: [
        { name: "幕布", url: "https://mubu.com/list" },
        { name: "个人博客", url: "https://canace.site/" },
        { name: "阿里icon", url: "https://www.iconfont.cn" }
      ]
    };
  },
  created() {},
  methods: {}
};
</script>
<style lang="scss" scoped>
.wrap {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  background: rgb(216, 215, 213);
  h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 1.25rem;
    color: rgba(24, 22, 22, 0.116);
  }
  .urlMap {
    width: 80%;
    height: 100%;
    a {
      display: inline-block;
      margin: 1.25rem;
      text-decoration: none;
      color: #fff;
      background: rgb(84, 149, 235);
      padding: 0.625rem;
      border-radius: 0.5rem;
      opacity: 0.8;
      &:hover {
        filter: brightness(0.8);
      }
    }
  }
}
</style>

