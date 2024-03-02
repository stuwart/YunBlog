<template>
  <el-space wrap direction="vertical" style="width: 100%" :fill-ratio="120">
    <el-card
      class="box-card"
      style="border-radius: 40px"
      shadow="hover"
      @click="openArticle"
    >
      <template #header>
        <div
          class="card-header"
          style="display: flex; justify-content: space-between"
        >
          <span>
            <span class="titleName">{{ name }}</span>
            <span v-for="tag in tags" :key="tag" class="tagName"
              >#{{ tag }}</span
            >
          </span>
          <span style="margin-right: 20px">{{ date }}</span>
        </div>
      </template>
      <div class="text-item">
        {{ body }}
      </div>
    </el-card>
  </el-space>
</template>

<script setup>
import router from "@/router";
const props = defineProps(["name", "tags", "date", "body", "url", "id"]);
const openArticle = () => {
  const toUrl = "/article/" + props.id + "/";
  router.push(toUrl);
};
</script>

<style lang="scss" scoped>
.titleName {
  margin-right: 20px;
  font-weight: bold;
}
.tagName {
  margin: 10px;
}
.box-card {
  width: 800px;
  height: 300px;
  cursor: pointer;
}
.text-item {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>
