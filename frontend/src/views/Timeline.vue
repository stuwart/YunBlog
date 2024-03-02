<template>
  <Header></Header>
  <div class="main">
    <el-timeline>
      <el-timeline-item
        v-for="(articles, date) in groupedArticles"
        :key="date"
        :timestamp="date"
        placement="top"
      >
        <div v-for="article in articles" :key="article.id">
          <h3>{{ article.title }}</h3>
          <span>{{ article.tags }}</span>
        </div>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>
    
<script setup>
import Header from "@/components/Header.vue";

import axios from "axios";
import { onMounted, ref } from "vue";

const groupedArticles = ref({});

const fetchAllArticles = async (url) => {
  try {
    const response = await axios.get(url);
    const { next, results } = response.data;
    // 处理当前页的数据
    results.forEach((article) => {
      const date = article.created; // 使用创建日期作为键
      if (!groupedArticles.value[date]) {
        groupedArticles.value[date] = [];
      }
      groupedArticles.value[date].push(article);
    });
    // 如果有下一页，递归获取
    if (next) {
      const nextUrlObj = new URL(next);
      const nextRelativePath = nextUrlObj.pathname + nextUrlObj.search;
      await fetchAllArticles(nextRelativePath);
    }
  } catch (error) {
    console.error("获取文章列表失败:", error);
  }
};

onMounted(() => fetchAllArticles("/api/article/"));
</script>
    
<style lang ="scss" scoped>
h3 {
  display: inline-block;
}
.main {
  position: relative;
  top: 60px;
  left: 25%;
}
</style>