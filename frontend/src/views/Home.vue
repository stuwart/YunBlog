<template>
  <!-- <BlogCard v-for="item in art"> </BlogCard> -->
  <Header></Header>
  <ArticleList></ArticleList>
</template>

<script setup>
import Header from "@/components/Header.vue";
import ArticleList from "@/components/ArticleList.vue";

</script>

<style lang="scss" scoped>
.card {
  margin-top: 20px;
}
</style>
