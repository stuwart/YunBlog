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

  <!-- <div class="demo-pagination-block" v-if="isSearch">
    <el-pagination
      v-model:current-page="currentPage"
      v-model:page-size="pageSize"
      :small="small"
      :disabled="disabled"
      :background="background"
      layout="prev, pager, next, jumper"
      :total="totalPage"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div> -->
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import getData from "@/utils/getData";
import { ref, watch, watchEffect } from "vue";
import { useRoute } from "vue-router";

const background = "#f4f4f4";

const isSearch = ref(true);
const totalPage = ref();
const props = defineProps(["url"]);
const articles = ref([]);
const kwargs = ref({ page: 1, searchText: "" });
const currentPage = ref(1);
const pageSize = ref(5);

watchEffect(() => {
  console.log("ArticleList:", props.url);
  getData(articles, props.url, kwargs, totalPage);
});
</script>

<style lang="scss" scoped>
.card {
  margin: 10px;
}
</style>