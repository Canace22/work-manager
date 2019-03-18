<template>
  <div class="wrap" :style="{height: h}">
    <table cellspacing="0" cellpadding="0">
      <caption>ToDo List</caption>
      <tr>
        <th v-for="(item, index) in titles" :key="index">{{item}}</th>
      </tr>
      <tr v-for="(item, index) in toDoList" :key="index" :id="item.id">
        <td contenteditable="true">{{item.item}}</td>
        <td contenteditable="true">{{item.solution}}</td>
        <td contenteditable="true">{{item.done}}</td>
        <td contenteditable="true">{{item.date}}</td>
        <td class="editBt">
          <button @click="add(item.id)">新增</button>
          <button @click="save(item.id)">保存</button>
          <button @click="edit(item.id)">修改</button>
          <button @click="deletes(item.id)">删除</button>
        </td>
      </tr>
    </table>
    <footer>
      <div class="pagenation">
        <span :class="{selected:selected===-1}" v-if="last" @click="selectLast()">上一页</span>
        <span
          :class="{selected:selected===index}"
          v-for="(item, index) in 5"
          :key="index"
          @click="selectPage(index)"
        >{{item}}</span>
        <span :class="{selected:selected===-2}" v-if="next" @click="selectNext()">下一页</span>
        <input v-model="jumpPage">
        <span @click="selectPage(jumpPage-1)">跳转</span>
      </div>
    </footer>
  </div>
</template>
<script>
import http from "@/common/serve.js";

export default {
  name: "ToDo",
  data() {
    return {
      h: `${window.innerHeight}px`,
      titles: ["事项", "解决方案", "进度", "完成时间", "操作"],
      toDoList: [],
      baseUrl: "http://127.0.0.1:7777",
      page: 0,
      jumpPage: 1,
      last: false,
      next: true,
      selected: 0
    };
  },
  computed: {
    lists() {
      return this.toDoList.slice(this.page, this.page + 5);
    }
  },
  created() {
    this.requestList(0);
  },
  methods: {
    requestList(page) {
      let params = { page: page };
      http.get(`${this.baseUrl}/v1/work`, params).then(res => {
        this.toDoList = [...res.data];
      });
    },
    addList(id, item, solution, done, date) {
      const temp = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      const params = {
        id: id,
        item: item,
        solution: solution,
        done: done,
        date: date
      };
      http.post(`${this.baseUrl}/v1/addWork`, params, temp);
    },
    deleteList(id) {
      const temp = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      const params = {
        id: id
      };
      console.log(params);
      http.post(`${this.baseUrl}/v1/deletework`, params, temp);
    },
    updateList(id, item, solution, done, date) {
      const temp = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      const params = {
        id: id,
        item: item,
        solution: solution,
        done: done,
        date: date
      };
      http.post(`${this.baseUrl}/v1/updateWork`, params, temp);
    },
    add(id) {
      this.toDoList.push({ id: id + 123 });
    },
    save() {
      const id = this.toDoList.slice(-1)[0].id;
      const list = document.getElementById(id).childNodes;

      this.addList(
        Math.random() * Math.floor(id),
        list[0].innerHTML,
        list[1].innerHTML,
        list[2].innerHTML,
        list[3].innerHTML
      );
    },
    deletes(id) {
      this.deleteList(id);
    },
    edit(id) {
      const list = document.getElementById(id).childNodes;

      this.updateList(
        id,
        list[0].innerHTML,
        list[1].innerHTML,
        list[2].innerHTML,
        list[3].innerHTML
      );
    },
    selectLast() {
      this.selected = -1;
      this.requestList(this.jumpPage - 2);
      if (this.jumpPage - 2 === 0) {
        this.last = false;
        this.jumpPage = this.jumpPage - 1;
        this.selected = this.jumpPage - 1;
      }
    },
    selectPage(index) {
      this.selected = index;
      this.requestList(index);
      this.jumpPage = index + 1;
      if (index > 0) {
        this.last = true;
      } else {
        this.last = false;
      }
      if (index > 5) {
        this.next = false;
      } else {
        this.next = true;
      }
    },
    selectNext() {
      this.selected = -2;
      this.requestList(this.jumpPage);
      this.jumpPage = this.jumpPage + 1;
      this.selected = this.jumpPage - 1;
    }
  }
};
</script>
<style lang="scss" scoped>
.wrap {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  background: rgb(216, 215, 213);
  table {
    border: none;
    caption {
      font-size: 2rem;
      font-weight: 700;
      margin: 1.25rem;
      color: rgba(24, 22, 22, 0.116);
    }
    th {
      color: rgba(0, 0, 0, 0.637);
    }
    td,
    th {
      border: 1px solid rgb(132, 177, 229);
      padding: 0.625rem 1.25rem;
    }
  }
}

.editBt {
  display: flex;
  justify-content: space-around;
  align-items: center;
  button {
    background: rgb(84, 149, 235);
    border: none;
    padding: 0.625rem;
    margin: 0.3125rem;
    color: #fff;
    opacity: 0.8;
    border-radius: 0.5rem;
    outline: none;
    cursor: pointer;
    &:hover {
      filter: brightness(0.8);
    }
  }
}
footer {
  position: fixed;
  bottom: 0;
  .pagenation {
    margin: 20px;
    span {
      margin: 10px;
      cursor: pointer;
      border-radius: 12px;
      padding: 10px;
      color: rgb(84, 149, 235);
    }
    input {
      background: transparent;
      border: 1px solid rgb(84, 149, 235);
      width: 40px;
      text-align: center;
    }
  }
  .selected {
    background: rgb(84, 149, 235);
    color: #fff !important;
  }
}
</style>

