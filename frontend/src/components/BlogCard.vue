<template>
  <el-space wrap direction="vertical" style="width: 100%" :fill-ratio="120">
    <el-card
      v-for="i in 5"
      :key="i"
      class="box-card"
      style="border-radius: 40px"
      shadow="hover"
    >
      <template #header>
        <div
          class="card-header"
          style="display: flex; justify-content: space-between"
        >
          <span>
            <span>Card name</span>
            <span style="margin-left: 20px">biaoqian</span>
          </span>
          <span style="margin-right: 20px">Date</span>
        </div>
      </template>
      <div v-for="o in 3" :key="o" class="text item">
        {{ "List item " + o }}
      </div>
    </el-card>
  </el-space>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.el-card {
  width: 800px;
  height: 300px;
  margin-top: 16px;
}
</style>
