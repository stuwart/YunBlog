<template>
  <div class="left">
    <div class="title">标签</div>
    <div v-for="tag in tags.results" :key="tag.id">
      {{ tag.name }}
    </div>
    <el-divider direction="vertical" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// 定义一个响应式变量来存储标签列表
const tags = ref([]);

// 定义获取标签列表的方法
const fetchTags = async () => {
  try {
    const response = await axios.get('/api/tag/');
    tags.value = response.data;
    console.log(tags);

    for(let i = 0;i<tags.results.length;i++){
      let url = '/api/tag/'+tags.results[i].id+'/';
      
    }
  } catch (error) {
    console.error('There was an error fetching the tags:', error);
  }
};

// 在组件挂载后调用fetchTags方法
onMounted(fetchTags);

</script>

<style lang="scss" scoped>
.title {
  display: flex;
  justify-content: center;
  font-size: 24px;
}
.left {
  position: absolute;
  left: 20%;
  margin-top: 20px;
}

.tagname {
  margin: 16px;
  font-size: 16px;
}

a {
  text-decoration-line: none;
  transition: all 0.3s ease;
  display: inline-block;
}
a:hover {
  // 变大
  font-size: 20px;
  background-color: grey;
  padding: 5px; /* 添加一些内边距以便观察到阴影效果 */
}
</style>