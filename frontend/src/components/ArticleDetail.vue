<template>
  <div class="common-layout">
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
          <h1></h1>
        </div>

        <div id="body">
          {{ body }}
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import router from "@/router";
import { onMounted, ref } from "vue";
import Footer from "./Footer.vue";
import { useRoute } from "vue-router";
import axios from "axios";

const article = ref("");
const route = useRoute();
const articleId = ref(route.params.id);

const url = "/api/article/" + articleId.value + "/";

const fetchArticleDetail = async () => {
  try {
    const response = axios.get(url);
    article.value = response.data;
    console.log(response);
  } catch (error) {
    console.error("存在错误：", error);
  }
};

onMounted(fetchArticleDetail);
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
  width: 100%;
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