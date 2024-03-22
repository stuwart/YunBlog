<template>
  <Header></Header>
  <div class="sidebar">
    <el-menu
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      style="background-color: #f4f4f4; margin-top: 40px"
    >
      <el-menu-item index="1">
        <el-icon><img src="/icon-article.png" /></el-icon>
        <span><router-link to="admin-article">文章管理</router-link></span>
      </el-menu-item>
      <el-menu-item index="2">
        <el-icon><img src="/icon-tag.png" /></el-icon>
        <span>标签管理</span>
      </el-menu-item>
      <el-menu-item index="3">
        <el-icon><img src="/icon-project.png" /></el-icon>

        <span><router-link to="admin-project">项目管理</router-link></span>
      </el-menu-item>
      <el-menu-item index="4" @click="openOrClose">
        <el-icon><img src="/open.png" /></el-icon>

        <span>展开/缩小</span>
      </el-menu-item>
    </el-menu>
  </div>
  <div class="main">
    <div class="hello">Hello , 赟！</div>
    <router-view></router-view>
  </div>
</template>


<script setup>
import { onMounted, ref } from "vue";
import Header from "@/components/Header.vue";

const isCollapse = ref(true);
const openOrClose = () => {
  isCollapse.value = !isCollapse.value;
};
</script>

<style lang="scss" scoped>
.sidebar {
  display: inline-block;
  img {
    width: 20px;
    height: auto;
  }
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.main {
  display: inline-block;
  .hello {
    position: relative;
    font-size: 24px;
    color: #3f3f3f;
    bottom:180px;
    left:40px;
  }
}
</style>