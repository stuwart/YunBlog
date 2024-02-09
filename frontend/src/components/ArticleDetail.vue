<template>
  <div class="common-layout">
    <el-container>
      <div class="head">
        <span class="word"> 一路向前 </span>
        <span class="right">
          <RouterLink to="/" class="no-underline">首页</RouterLink>
          <RouterLink to="/tag" class="no-underline">标签</RouterLink>
          <RouterLink to="/timeline" class="no-underline">归档</RouterLink>
          <RouterLink to="/project" class="no-underline">项目</RouterLink>
        </span>
      </div>
      <el-container>
        <el-aside width="200px">{{ tags }}</el-aside>
        <el-main>
          <div id="title">
            {{ title }}
          </div>

          <div id="body">
            {{ body }}
          </div>
        </el-main>
      </el-container>
      <Footer></Footer>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Footer from "./Footer.vue";
defineProps("id");
const title = ref("");
const body = ref("");
const date = ref("");
const tags = ref([]);
</script>



<style lang="scss" scoped>
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
</style>