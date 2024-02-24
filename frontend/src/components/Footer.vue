<template>
  <div class="foot">
    <div class="icon">
      <a href="https://space.bilibili.com/50961403?spm_id_from=333.999.0.0">
        <img src="../../public/bilibili.png" alt="bilibili"
      /></a>
        
      <img src="../../public/social-weibo.png" alt="微博" />
      <img src="../../public/xiaohongshu.png" alt="小红书" />
      <img src="../../public/zhihu.png" alt="知乎" />
    </div>
    <div class="info">
      <span>
        <span>Powered by </span>
        <a href="https://beian.miit.gov.cn/" target="_blank" class="beian"
          >浙ICP备2024065601号</a
        >
      </span>
    </div>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.icon,
.info {
  display: flex;
  justify-content: center;
  margin: 20px;
}

img {
  width: 24px;
  height: 24px;
  margin: 0 20px 0 20px;
}
</style>