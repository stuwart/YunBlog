<template>
  <div class="empty" />
  <div class="intro">
    <span id="name">云 想</span>
    <span id="word">很高兴遇见你</span>
  </div>
  <el-divider />
</template>

<script setup>
</script>

<style lang="scss" scoped>
.intro {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100px;
}
.empty {
  width: 100%;
  height: 60px;
  background-color: #f4f4f4;
}
#name {
  font-size: 40px;
  font-family: Arial;
  margin: auto;
}
#word {
  font-size: 16px;
  margin: auto;
  color: #999;
}
</style>