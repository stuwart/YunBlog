<template>
  <div class="content">
    <BlogCard
      v-for="item in articles"
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

  <!-- <div class="demo-pagination-block" v-if="isSearch">
    <el-pagination
      v-model:current-page="currentPage"
      v-model:page-size="pageSize"
      :small="small"
      :disabled="disabled"
      :background="background"
      layout="prev, pager, next, jumper"
      :total="totalPage"
      :default-page-size:10
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div> -->
</template>

<script setup>
import BlogCard from "@/components/BlogCard.vue";
import getData from "@/utils/getData";
import { ref, watchEffect } from "vue";

const isSearch = ref(true);
const totalPage = ref();
const props = defineProps(["url"]);
const articles = ref([]);
const kwargs = ref({ page: 1, searchText: "" });
const currentPage = ref(1);
const pageSize = ref(10);

const con = ref({
  width: "800px",
  height: "300px",
  borderRadius: "40px",
});

watchEffect(() => {
  getData(articles, props.url, kwargs, totalPage);
});
</script>

<style lang="scss" scoped>
.content {
  display: flex;
  justify-content: center;
  flex-direction: column;
  .card {
    margin: 10px;
  }
}
</style>