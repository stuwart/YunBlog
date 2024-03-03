<template>
  <!-- <BlogCard v-for="item in art"> </BlogCard> -->
  <Header @search="handleSearch"></Header>
  <ArticleList :url="url"></ArticleList>
</template>

<script setup>
import Header from "@/components/Header.vue";
import ArticleList from "@/components/ArticleList.vue";
import { ref } from "vue";

const url = ref("/api/article/");
const searchQuery = ref("");
const handleSearch = (query) => {
  searchQuery.value = query;
  url.value = `/api/article/?search=${searchQuery.value}`;
  console.log(url.value);
};
</script>

<style lang="scss" scoped>
</style>
