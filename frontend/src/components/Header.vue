<template>
  <div class="head">
    <el-row>
      <el-col :span="6"><span class="word">一路向前</span></el-col>
      <el-col :span="6"
        ><div class="grid-content ep-bg-purple-light" />
      </el-col>
      <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="6">
        <span class="func">
          <RouterLink to="/" class="no-underline">首页</RouterLink>
          <RouterLink to="/Tag" class="no-underline">标签</RouterLink>
          <RouterLink to="/Category" class="no-underline">分类</RouterLink>
          <RouterLink to="/Timeline" class="no-underline">时间</RouterLink>
        </span>
      </el-col>
    </el-row>
  </div>
</template>
  
<script setup>
import { RouterLink } from "vue-router";
import "@/assets/base.css";
</script>
  
<style lang="scss" scoped>
.no-underline{
  text-decoration: none;
}
.no-underline:visited{
  color: #590def;
}
.head {
 position: relative;
 top: 12px;
 font-size: 18px;
 color: #590def;
  .word {
    margin-left: 20px;
  }
  .func {
    display: flex;
    justify-content: space-between;
    width: 220px;
    
  }
}
</style>