<template>
  <div class="left">
    <div class="title">标签</div>
    <div v-for="item in tags" :key="item.id">
      <div class="tagname">
        <a href="#">{{ item.name }}({{ item.num }})</a>
      </div>
    </div>
    <el-divider direction="vertical" />
  </div>
</template>

<script setup>
import { ref } from "vue";

const tags = [
  {
    name: "1111",
    url: "http:111",
    num: 4,
  },
  {
    name: "1111",
    url: "http:111",
    num: 3,
  },
  {
    name: "1111",
    url: "http:111",
    num: 2,
  },
  {
    name: "1111",
    url: "http:111",
    num: 6,
  },
];

let len = tags.length;
</script>

<style lang="scss" scoped>
.title {
  display: flex;
  justify-content: center;
  font-size: 24px;
}
.left {
  position: absolute;
  left: 20%;
  margin-top: 20px;
}

.tagname {
  margin: 16px;
  font-size: 16px;
}

a {
  text-decoration-line: none;
  transition: all 0.3s ease;
  display: inline-block;
}
a:hover {
  // 变大
  font-size: 20px;
  background-color: grey;
  padding: 5px; /* 添加一些内边距以便观察到阴影效果 */
  
}
</style>