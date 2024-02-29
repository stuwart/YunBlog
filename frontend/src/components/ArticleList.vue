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
    class="card"
  ></BlogCard>
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import getData from "@/utils/getData";
import { ref, onMounted } from "vue";
const articles = ref([]);
const url = "/api/article/";
onMounted(() => {
  getData(articles, url);
});
</script>

<style lang="scss" scoped>
.card{
  margin: 10px;
}
</style>