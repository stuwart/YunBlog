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
    <img src="../../public/back.png" class="back" @click="backTo" style="width: 20px;" alt="后退">
    <div class="contain">
      <div class="toc">
        <h3>目录</h3>
        <div v-html="article.toc_html"></div>
      </div>
      <div class="content">
        <div class="title">{{ article.title }}</div>
        <div class="time">{{ article.created }}</div>
        <div class="tag">{{ article.tags }}</div>
        <div v-html="article.body_html" class="zhengwen"></div>
      </div>
    </div>
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

console.log(url);

const fetchArticleDetail = async () => {
  try {
    const response = await axios.get(url);
    article.value = response.data;
    console.log(article);
  } catch (error) {
    console.error("存在错误：", error);
  }
};

onMounted(fetchArticleDetail);

const backTo = () => {
  router.go(-1);
};
</script>


<style lang="scss" scoped>
.contain{
  display: flex;
}
.toc{
  width: 20%;
  margin-left: 100px;
}

.content{
  width: 80%;
  margin-left: 100px;
  .title{
    font-size: 24px;
  }
  .time{
    font-size: 18px;
  }
  .tag{
    font-size: 16px;
  }
  .zhengwen{
    font-size: 16px;;
  }
}




.back{
  cursor: pointer;
  background-color: antiquewhite;
  padding: 10px;
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