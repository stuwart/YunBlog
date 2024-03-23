<template>
  <el-space wrap direction="vertical" :fill-ratio="120">
    <el-card
      class="box-card"
      shadow="hover"
      @click="handle"
      :style="styleObject"
    >
      <template #header>
        <div
          class="card-header"
          style="display: flex; justify-content: space-between"
        >
          <span>
            <span class="titleName" style="font-size: 18px">{{ name }}</span>
            <span v-for="tag in tags" :key="tag" class="tagName"
              >#{{ tag }}</span
            >
          </span>
          <span style="margin-right: 20px">upd: {{ date }}</span>
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
const props = defineProps([
  "name",
  "tags",
  "date",
  "body",
  "url",
  "id",
  "opt",
  "con",
]);
const styleObject = {
  width: props.con.width,
  height: props.con.height,
  borderRadius: props.con.borderRadius,
};
const openArticle = () => {
  const toUrl = "/article/" + props.id + "/";
  router.push(toUrl);
};

const openEdit = () => {
  const toUrl = "/article/edit/" + props.id + "/";
  router.push(toUrl);
};
const handle = () => {
  if (props.opt === "openEdit") {
    openEdit();
  } else {
    openArticle();
  }
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
  cursor: pointer;
}
.text-item {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>
