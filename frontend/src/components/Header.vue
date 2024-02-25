<template>
  <div class="head">
    <span class="word"> 一路向前 </span>
    <span class="right">
      <div class="m-4 search">
        <el-cascader class="searchbox" placeholder="请搜索关键词" :options="options" filterable />
      </div>

      <RouterLink to="/" class="no-underline">首页</RouterLink>
      <RouterLink to="/tag" class="no-underline">标签</RouterLink>
      <RouterLink to="/timeline" class="no-underline">归档</RouterLink>
      <RouterLink to="/project" class="no-underline">项目</RouterLink>
    </span>
  </div>
  <div class="empty" />
  <div class="intro">
    <span id="name">赟</span>
    <span id="word">很高兴遇见你</span>
  </div>
  <el-divider />
</template>
  
<script setup>
import { RouterLink } from "vue-router";
import "@/assets/base.css";
</script>
  
<style lang="scss" scoped>
.search {
  display: flex; /* 添加flexbox布局 */
  align-items: center; /* 在交叉轴（此处为垂直轴）上居中对齐子项 */
  justify-content: center; /* 可选：在主轴（此处为水平轴）上居中对齐子项，如果你也想水平居中的话 */
  /* 你可能需要设置一个高度，除非它已经通过内容或其他方式隐式设置 */
}
.el-cascader{
  border-radius: 12px;
}
.no-underline {
  text-decoration: none;
  border-radius: 4px;
}
.no-underline:hover {
  background-color: rgb(180, 180, 180);
}
.no-underline:visited {
  color: #590def;
}
.no-underline:active {
  filter: brightness(1.2);
}
.head {
  position: relative;
  top: 12px;
  font-size: 18px;
  color: #590def;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  img {
    width: 24px;
    height: 24px;
  }
  .word {
    margin-left: 40px;
  }
  .right {
    margin-right: 40px;
    width: 500px;
    display: flex;
    justify-content: space-around;
  }
}
.intro {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.empty {
  width: 100%;
  height: 60px;
  background-color: #f4f4f4;
}
#name {
  font-size: 40px;
  font-family: Arial;
  margin: auto;
}
#word {
  margin-top: 20px;
  font-size: 20px;
  margin: auto;
}
</style>