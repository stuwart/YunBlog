<template>
  <div class="empty"></div>
  <div class="content">
    <BlogCard
      v-for="item in articles"
      :key="item.id"
      :name="item.title"
      :date="item.created"
      :body="item.body"
      :tags="item.tags"
      :url="item.url"
      :id="item.id"
      :con="con"
      opt="openEdit"
      class="smallCard"
    ></BlogCard>
  </div>
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import { onMounted, ref } from "vue";
import axios from "axios";
const con = ref({
  width: "360px",
  height: "200px",
  borderRadius: "30px",
});

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
.empty {
  height: 60px;
}
.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

  .smallCard {
    margin: 20px;
  }
}
</style>