<template>
  <div class="foot">
    <div class="icon">
      <a href="https://space.bilibili.com/50961403?spm_id_from=333.999.0.0" target="_blank">
        <img src="/bilibili.png" alt="bilibili"
      /></a>

      <a href="https://weibo.com/u/5536620715" target="_blank"
        ><img src="/social-weibo.png" alt="微博"
      /></a>
      <a
        href="https://www.xiaohongshu.com/user/profile/62ac72b600000000190288a1"
        target="_blank"
      >
        <img src="/xiaohongshu.png" alt="小红书" />
      </a>
      <a href="https://www.zhihu.com/people/huang-yun-29-98" target="_blank">
        <img src="/zhihu.png" alt="知乎" />
      </a>
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