<template>
  <Header></Header>
  <div class="empty" />
  <div class="intro">
    <span id="name">赟</span>
    <span id="word">很高兴遇见你</span>
  </div>
  <el-divider />
  
    <BlogCard></BlogCard>
  
</template>

<script setup>
import Header from "@/components/Header.vue";
import BlogCard from "@/components/BlogCard.vue";
import { ref } from "vue";


</script>

<style lang="scss" scoped>
.intro {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.empty {
  width: 100%;
  height: 60px;
  background-color: #f4f4f4;
}
#name {
  font-size: 60px;
  font-family: Arial;
}
#word {
  margin-top: 20px;
  font-size: 20px;
}

</style>
