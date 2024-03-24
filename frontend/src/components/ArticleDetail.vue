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

    <div class="contain">
      <div class="toc">
        <img
          src="/back.png"
          class="back"
          @click="backTo"
          style="width: 20px"
          alt="后退"
        />
        <h3>目录</h3>
        <div v-html="article.toc_html" class="tocItem"></div>
      </div>
      <el-divider direction="vertical" class="divider" />
      <div class="content">
        <div class="title">{{ article.title }}</div>
        <div class="tag">{{ article.tags }}</div>
        <div class="time">更新于：{{ article.updated }}</div>
        <div v-html="mdBody" class="zhengwen"></div>
        <div class="date">创建于：{{ article.created }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from "@/router";
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { marked } from "marked";

const article = ref({});

const route = useRoute();
const articleId = ref(route.params.id);

const url = "/api/article/" + articleId.value + "/";
const mdBody = computed(() => {
  // 确保article.value.body存在，否则返回空字符串
  return article.value.body ? marked(article.value.body) : "";
});

const fetchArticleDetail = async () => {
  try {
    const response = await axios.get(url);
    article.value = response.data;
    // console.log(article.value.body);

    console.log("111", mdBody);
  } catch (error) {
    console.error("存在错误：", error);
  }
};

const backTo = () => {
  router.go(-1);
};
onMounted(fetchArticleDetail);
</script>


<style lang="scss" scoped>
.divider {
  position: absolute;
  left: 360px;
  top: 100px;
  height: 600px;
}
.date {
  position: relative;
  color: grey;
  margin-top: 60px;
  margin-bottom: 30px;
}
.contain {
  display: flex;
  position: relative;
  top: 30px;

  .toc {
    width: 20%;
    margin-left: 200px;
    h3 {
      display: inline-block;
      position: relative;
      right: 80px;
    }
    .back {
      display: inline-block;
      cursor: pointer;
      background-color: #f4f4f4;
      padding: 10px;
      border-radius: 12px;
      position: relative;
      top: 14px;
      right: 120px;
      color: #590def;
    }
    .tocItem{
      position: relative;
      right:100px;
    }
  }
  .content {
    width: 80%;
    margin-left: 20px;
    display: flex;
    flex-direction: column;

    .title {
      font-size: 24px;
      margin: auto;
      justify-content: center;
    }

    .tag {
      margin-top: 20px;
      font-size: 16px;
      margin: auto;
      justify-content: center;
    }
    .time {
      font-size: 18px;
      margin-left: auto;
      margin-right: 100px;
    }

    .zhengwen {
      font-size: 16px;
    }
  }
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
    .no-underline {
      text-decoration: none;
      border-radius: 4px;
      &:hover {
        background-color: rgb(180, 180, 180);
      }
      &:visited {
        color: #590def;
      }
      &:active {
        filter: brightness(1.2);
      }
    }
  }
}
</style>