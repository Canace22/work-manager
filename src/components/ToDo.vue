<template>
  <div class="wrap" :style="{height: height}">
    <table cellspacing="0" cellpadding="0">
      <caption>ToDo List</caption>
      <tr>
        <th v-for="(item, index) in titles" :key="index">{{item}}</th>
      </tr>
      <tr :class="{checked:item.done}" v-for="(item, index) in lists" :key="index" :id="item.id">
        <td contenteditable="true" class="item">
          <input type="checkbox" class="item-checkbox" name="item" :checked="item.done" />
          <span class="item-text">{{item.item}}</span>
        </td>
        <td contenteditable="true" style="width: 25%">{{item.solution}}</td>
        <td contenteditable="true" class="date">{{item.date}}</td>
        <td>
          <div class="editBt">
            <button @click="add(item.id)">新增</button>
            <button @click="save(item.id)">保存</button>
            <button @click="edit(item.id)">修改</button>
            <button @click="deletes(item.id)">删除</button>
          </div>
        </td>
      </tr>
    </table>
    <footer>
      <div class="pagenation">
        <!-- <span :class="{selected:selected===-1}" v-if="last" @click="selectLast()">上一页</span> -->
        <span
          :class="{selected:selected===index}"
          v-for="(item, index) in totalPage"
          :key="index"
          @click="selectPage(index)"
        >{{item}}</span>
        <!-- <span :class="{selected:selected===-2}" v-if="next" @click="selectNext()">下一页</span> -->
        <input v-model="jumpPage" />
        <span @click="selectPage(jumpPage - 1)">跳转</span>
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
      height: `${window.innerHeight}px`,
      titles: ["事项", "解决方案", "完成时间", "操作"],
      toDoList: [],
      baseUrl: "http://47.112.112.174:7777",
      // baseUrl: "http://192.168.1.247:7777",
      page: 0,
      jumpPage: 1,
      last: false,
      next: true,
      selected: 0,
      totalPage: 0,
      newId: 0,
      done: false
    };
  },
  computed: {
    lists() {
      return this.toDoList.slice(this.page * 6, this.page * 6 + 5);
    }
  },
  created() {
    this.requestList(0);
  },
  methods: {
    requestList() {
      http.get(`${this.baseUrl}/v1/work`).then(res => {
        this.toDoList = [...res.data];
        this.toDoList.forEach(element => {
          element.done = +element.done;
        });
        this.toDoList.sort((x, y) => {
          return x.done - y.done;
        });
        this.totalPage = Math.ceil(this.toDoList.length / 5);
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
      alert("修改成功");
    },
    add(id) {
      this.newId = id + 123;
      this.toDoList.forEach((element, index, self) => {
        if (element.id === id) {
          self.splice(index + 1, 0, { id: this.newId });
        }
      });
    },
    save() {
      const id = this.newId;
      const list = document.getElementById(id).childNodes;

      this.addList(
        Math.random() * Math.floor(id),
        list[0].childNodes[1].innerHTML,
        list[1].innerHTML,
        +list[0].firstChild.checked,
        list[2].innerHTML
      );
      // if (+list[0].firstChild.checked) {
      //   document.getElementById(id).style.background = "rgb(155, 155, 35)";
      // } else {
      //   document.getElementById(id).style.background = "transparent";
      // }
      alert("保存成功");
    },
    deletes(id) {
      this.deleteList(id);
      this.toDoList.forEach((element, index, self) => {
        if (element.id === id) {
          self.splice(index, 1);
        }
      });
    },
    edit(id) {
      const list = document.getElementById(id).childNodes;

      this.updateList(
        id,
        list[0].childNodes[1].innerHTML,
        list[1].innerHTML,
        +list[0].firstChild.checked,
        list[2].innerHTML
      );
      if (+list[0].firstChild.checked) {
        document.getElementById(id).style.background = "rgb(155, 155, 35)";
      } else {
        document.getElementById(id).style.background = "transparent";
      }
    },
    selectPage(index) {
      this.selected = index;
      this.page = index;
      this.jumpPage = +index + 1;
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
    width: 80%;
    height: 70%;
    caption {
      font-size: 2rem;
      font-weight: 700;
      margin: 1.25rem;
      color: rgba(24, 22, 22, 0.116);
    }
    th {
      color: rgba(10, 9, 9, 0.815);
      font-weight: 700;
      height: 10%;
    }
    td,
    th {
      border: 1px solid rgb(132, 177, 229);
      padding: 0.625rem 1.25rem;
      position: relative;
    }
  }
}

.editBt {
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  min-height: 50px;
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

.date {
  width: 12%;
  text-align: center;
}

.item {
  width: 30%;
  .item-text {
    float: left;
    margin-left: 10px;
    text-align: left;
  }
  .item-checkbox {
    float: left;
    cursor: pointer;
    width: 20px;
    height: 20px;
    position: absolute;
    left: 0;
    &:checked {
      background-color: #2196f3 !important;
    }
    &:hover {
      background-color: #ccc;
    }
  }
}
.checked {
  background: rgb(155, 155, 35);
}
</style>

