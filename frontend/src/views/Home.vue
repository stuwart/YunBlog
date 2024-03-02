<template>
  <!-- <BlogCard v-for="item in art"> </BlogCard> -->
  <Header></Header>
  <ArticleList :url="url"></ArticleList>
</template>

<script setup>
import Header from "@/components/Header.vue";
import ArticleList from "@/components/ArticleList.vue";
import { ref } from "vue";

const url = ref("/api/article/");

</script>

<style lang="scss" scoped>
</style>
