<template>
  <Header />
  <div class="main">
    <el-timeline>
      <el-timeline-item
        v-for="item in events"
        :key="item.id"
        :timestamp="item.created"
        placement="top"
        class="node"
      >
        <h3>#{{ item.title }}</h3>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>
    
<script setup>
import Header from "@/components/Header.vue";
import axios from "axios";
import { onMounted, ref } from "vue";

const events = ref([]);

const getEvents = async () => {
  try {
    const response = await axios.get("/api/article/");
    events.value = response.data.results;
  } catch (error) {
    console.log("存在错误：", error);
  }
};

onMounted(getEvents);
</script>
    
<style lang ="scss" scoped>
.node{
  color:purple;
}


.main {
  position: relative;
  top: 60px;
  left: 25%;
}
</style>