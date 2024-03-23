<template>
  <BlogCard
    v-for="item in articles"
    :key="item.id"
    :name="item.title"
    :date="item.created"
    :body="item.body"
    :tags="item.tags"
    :url="item.url"
    :id="item.id"
    opt="openEdit"
    class="card"
  ></BlogCard>
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import { onMounted, ref } from "vue";
import axios from "axios";
const articles = ref([]);

const fetchArticles = async () => {
  try {
    const response = await axios.get("/api/article");
    const { next, results } = response.data;

    articles.value = results;
    if (next) {
      const nextUrlObj = new URL(next);
      const nextRelativePath = nextUrlObj.pathname + nextUrlObj.search;
      await fetchAllArticles(nextRelativePath);
    }
  } catch (error) {
    console.error("存在错误：", error);
  }
  console.log(articles.value);
};

onMounted(fetchArticles);
</script>

<style lang="scss" scoped>
.card {
  width: 100px;
  height: 60px;
}
</style>