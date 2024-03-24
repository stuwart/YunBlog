<template>
  <div class="empty"></div>
  <div class="add">
    <el-button type="primary" round @click="addArticle">新增</el-button>
  </div>

  <div class="content">
    <BlogCard
      v-for="item in articles.results"
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
import { onMounted, ref, watchEffect } from "vue";
import axios from "axios";
import router from "@/router";
import getData from "@/utils/getData";

const con = ref({
  width: "500px",
  height: "300px",
  borderRadius: "40px",
});

const articles = ref({});

watchEffect(() => {
  getData(articles, "/api/article/");
});

const addArticle = () => {
  router.push("/article/edit/0/");
};

const currentPage = ref(1);
const pageSize = ref(10);
watchEffect(() => {
  getData(articles, `/api/article?page=${currentPage.value}`);
});
</script>

<style lang="scss" scoped>
.empty {
  height: 60px;
}
.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  flex-basis: 40%;
  .smallCard {
    margin: 20px;
  }
}
.pagination {
  display: flex;
  justify-content: center;
  margin: 30px;
}
</style>