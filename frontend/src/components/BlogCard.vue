<template>
  <el-space wrap direction="vertical" style="width: 100%" :fill-ratio="120" >
    <el-card class="box-card" style="border-radius: 40px" shadow="hover">
      <template #header>
        <div
          class="card-header"
          style="display: flex; justify-content: space-between"
        >
          <span>
            <span>{{ name }}</span>
            <span style="margin-left: 20px">{{ tags }}</span>
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
defineProps(["name", "tags", "date", "body"]);


</script>

<style lang="scss" scoped>
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
