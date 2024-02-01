<template>
  <div class="head">
    <span class="word"> 一路向前 </span>
    <span class="right">
      <RouterLink to="/" class="no-underline">首页</RouterLink>
      <RouterLink to="/Tag" class="no-underline">标签</RouterLink>
      <RouterLink to="/Timeline" class="no-underline">时间</RouterLink>
      <RouterLink to="/Project" class="no-underline">项目</RouterLink>
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
.no-underline {
  text-decoration: none;
}
.no-underline:visited {
  color: #590def;
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
  .word {
    margin-left: 40px;
  }
  .right {
    margin-right: 40px;
    width: 200px;
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