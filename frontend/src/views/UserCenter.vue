<template>
  <Header></Header>
  <div class="container">
    <div class="sidebar">
      <el-menu
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        style="background-color: #f4f4f4; margin-top: 40px"
      >
        <el-menu-item index="1" @click="showArea('/usercenter/admin-article/')">
          <el-icon><img src="/icon-article.png" /></el-icon>
          <span class="menu-text">文章管理</span>
        </el-menu-item>

        <el-menu-item index="2" @click="showArea('/usercenter/admin-tag/')">
          <router-link to="/usercenter/admin-tag/">
            <el-icon><img src="/icon-tag.png" /></el-icon>
          </router-link>
          <span class="menu-text">标签管理</span>
        </el-menu-item>
        <el-menu-item index="3" @click="showArea('/usercenter/admin-project/')">
          <router-link to="/usercenter/admin-project/">
            <el-icon><img src="/icon-project.png" /></el-icon>
          </router-link>
          <span class="menu-text">项目管理</span>
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
  </div>
</template>


<script setup>
import { onMounted, ref } from "vue";
import Header from "@/components/Header.vue";
import router from "@/router";

const isCollapse = ref(true);
const openOrClose = () => {
  isCollapse.value = !isCollapse.value;
};

const showArea = (url) => {
  router.replace({ path: url });
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
}

.main {
  margin-top: 20px;
  margin-left: 20px;
  flex-grow: 1;
  position: relative;
  display: inline-block;
  // left: 20px;
  // bottom: 220px;
  .hello {
    position: absolute;
    font-size: 24px;
    color: #3f3f3f;
    left: 60px;
  }
}

.sidebar {
  display: inline-block;
  flex-shrink: 0;
  img {
    width: 20px;
    height: auto;
  }
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>