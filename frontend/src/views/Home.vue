<template>
  <Header @search="handleSearch"></Header>
  <BigTitle></BigTitle>
  <ArticleList :url="url"></ArticleList>
</template>

<script setup>
import Header from "@/components/Header.vue";
import ArticleList from "@/components/ArticleList.vue";

import { ref } from "vue";
import BigTitle from "@/components/BigTitle.vue";

const url = ref("/api/article/");
const searchQuery = ref("");
const handleSearch = (query) => {
  searchQuery.value = query;
  url.value = `/api/article/?search=${searchQuery.value}`;
};
</script>

<style lang="scss" scoped>
</style>
