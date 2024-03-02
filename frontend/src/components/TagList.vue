<template>
  <div class="container">
    <div class="left">
      <div class="title">标签</div>
      <div v-for="tag in tags.results" :key="tag.id">
        <a href="#" class="tagname" @click.prevent="showarticles(tag.id)"
          >{{ tag.name }}({{ tag.cnt }})
        </a>
      </div>
      <el-divider direction="vertical" class="divider" />
    </div>
    <div class="detail">
      <ArticleList :url="url"></ArticleList>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import ArticleList from "./ArticleList.vue";
import getData from "@/utils/getData";

const url = ref("/api/article/");
const tags = ref([]);

const fetchTags = async () => {
  try {
    const response = await axios.get("/api/tag/");
    tags.value = response.data;
  } catch (error) {
    console.error("There was an error fetching the tags:", error);
  }
};

// 在组件挂载后调用fetchTags方法
onMounted(fetchTags);

const showarticles = (id) => {
  url.value = `/api/tag-article/${id}/`;
  // console.log("URLVALUE:",url.value);
}

</script>

<style lang="scss" scoped>
.detail {
  position: relative;
  left: 500px;
  width: 800px;
  height: auto;
}

.title {
  display: flex;
  justify-content: center;
  font-size: 24px;
}
.left {
  display: inline-block;
  position: absolute;
  left: 20%;
  margin-top: 20px;
  width: 8%;
}

.tagname {
  margin: 16px;
  font-size: 16px;
  color: #590def;
  text-decoration-line: none;
  transition: all 0.3s ease;

  border-radius: 12px;
  display: flex;
  justify-content: center;

  &:hover {
    // 变大
    font-size: 18px;

    background-color: rgb(220, 192, 220);
    padding: 5px; /* 添加一些内边距以便观察到阴影效果 */
  }
}

.divider {
  position: absolute;
  left: 150px;
  top: 10px;
  height: 200px;
}
</style>