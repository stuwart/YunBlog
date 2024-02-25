<template>
  <div class="icon">
    <img src="/bilibili.png" alt="bilibili" id="bilibili" />

    <img src="/social-weibo.png" alt="微博" id="weibo" />

    <img src="/xiaohongshu.png" alt="小红书" id="xiaohongshu" />
    <img src="/zhihu.png" alt="知乎" id="zhihu" />
  </div>
  <div class="info">
    <span>Copyright © 2024 云想 All Rights Reserved</span>
    <span>
      <span>Powered by </span>
      <a href="https://beian.miit.gov.cn/" target="_blank" class="beian"
        >浙ICP备2024065601号</a
      >
    </span>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
onMounted(() => {
  document.getElementById("bilibili").addEventListener("click", () => {
    window.open(
      "https://space.bilibili.com/50961403?spm_id_from=333.999.0.0",
       "_blank"
    );
  });
  document.getElementById("weibo").addEventListener("click", () => {
    window.open(
      "https://weibo.com/u/5536620715",
       "_blank"
    );
  });
  document.getElementById("xiaohongshu").addEventListener("click", () => {
    window.open(
      "https://www.xiaohongshu.com/user/profile/62ac72b600000000190288a1",
      "_blank"
    );
  });
  document.getElementById("zhihu").addEventListener("click", () => {
    window.open(
      "https://www.zhihu.com/people/huang-yun-29-98",
       "_blank"
    );
  });
});
</script>

<style lang="scss" scoped>
.icon {
  display: flex;
  justify-content: center;
  margin: 0 20px 0 20px;
  height: 20px;
}
.info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px;
}

img {
  width: 24px;
  height: 24px;
  margin: 0 20px 0 20px;
  cursor: pointer;
}
</style>