<template>
  <!-- <BlogCard v-for="item in art"> </BlogCard> -->
  <Header></Header>
  <BlogCard
    v-for="item in articles"
    :key="item.id"
    :name="item.title"
    :date="item.created"
    :body="item.body"
    :tags="item.tags"
    :url="item.url"
    :id="item.id"
    class="card"
  ></BlogCard>
</template>

<script setup>
import Header from "@/components/Header.vue";
import BlogCard from "@/components/BlogCard.vue";
import { onMounted, ref } from "vue";
import axios from "axios";
const articles = ref([]);
const fetcharticles = async () => {
  try {
    const response = await axios.get("/api/article/");
    articles.value = await response.data.results;
    console.log(articles);
  } catch (error) {
    console.error("There is an error:", error);
  }
};
onMounted(fetcharticles);
</script>

<style lang="scss" scoped>
.card {
  margin-top: 20px;
}
</style>
