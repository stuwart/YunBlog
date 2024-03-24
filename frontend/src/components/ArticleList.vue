<template>
  <div class="content">
    <BlogCard
      v-for="item in articles.results"
      :key="item.id"
      :name="item.title"
      :date="item.updated"
      :body="item.body"
      :tags="item.tags"
      :url="item.url"
      :id="item.id"
      :con="con"
      class="card"
    ></BlogCard>
  </div>

  <div class="demo-pagination-block pagination">
    <el-pagination
      v-model:current-page="currentPage"
      v-model:page-size="pageSize"
      layout="prev, pager, next, jumper"
      :total="articles.count"
      :hide-on-single-page="true"
    />
  </div>
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import getData from "@/utils/getData";
import { ref, watchEffect } from "vue";

const props = defineProps(["url"]);
const articles = ref({});

const con = ref({
  width: "800px",
  height: "300px",
  borderRadius: "40px",
});

watchEffect(() => {
  getData(articles, props.url);
});

const currentPage = ref(1);
const pageSize = ref(10);
watchEffect(() => {
  getData(articles, `/api/article?page=${currentPage.value}`);
});
</script>

<style lang="scss" scoped>
.content {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  .card {
    margin: 20px;
  }
 
}
.pagination {
    display: flex;
    justify-content: center;
  }
</style>