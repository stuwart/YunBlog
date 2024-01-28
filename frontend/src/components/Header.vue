<template>
  <div class="head">
    <span class="word"> 一路向前 </span>
    <span class="right">
      <RouterLink to="/" class="no-underline">首页</RouterLink>
      <RouterLink to="/Tag" class="no-underline">标签</RouterLink>
      <RouterLink to="/Category" class="no-underline">分类</RouterLink>
      <RouterLink to="/Timeline" class="no-underline">时间</RouterLink>
    </span>
  </div>
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
  .right{
    margin-right: 40px;
    width: 200px;
    display: flex;
    justify-content: space-around;
  }
}
</style>