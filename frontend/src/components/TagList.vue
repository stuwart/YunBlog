<template>
  <div class="container">
    <div class="left">
      <div class="title">标签</div>
      <div v-for="tag in tags.results" :key="tag.id">
        <a
          href="#"
          class="tagname"
          @click.prevent="showarticles(tag.id)"
          >{{ tag.name }}({{ tag.cnt }})
        </a>
      </div>
      <el-divider direction="vertical" class="divider" />
    </div>
    <div class="detail">
      <BlogCard
        v-for="item in articles.articles"
        :key="item.id"
        :name="item.title"
        :date="item.created"
        :body="item.body"
        :tags="item.tags"
        :url="item.url"
        :id = "item.id"
        class="card"
      ></BlogCard>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import BlogCard from "./BlogCard.vue";
// 定义一个响应式变量来存储标签列表
const tags = ref([]);

// 定义获取标签列表的方法
const fetchTags = async () => {
  try {
    const response = await axios.get("/api/tag/");
    tags.value = response.data;
    console.log(tags);
  } catch (error) {
    console.error("There was an error fetching the tags:", error);
  }
};

// 在组件挂载后调用fetchTags方法
onMounted(fetchTags);

//点击tag后，获取对应url
// function showarticles(event) {
//   const url = event.target.href;
//   console.log("url:", url);
// }
const articles = ref([]);
const showarticles = async (id) => {
  try {
    const response = await axios.get(`/api/tag/${id}/`);
    articles.value = response.data;
    console.log('url:',id);
  } catch {
    console.error("存在错误：", error);
  }
};
</script>

<style lang="scss" scoped>
.card{
  margin-top: 20px;
}
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
}

.tagname:hover {
  // 变大
  font-size: 18px;

  background-color: rgb(220, 192, 220);
  padding: 5px; /* 添加一些内边距以便观察到阴影效果 */
}

.divider {
  position: absolute;
  left: 150px;
  top: 10px;
  height: 200px;
}
</style>