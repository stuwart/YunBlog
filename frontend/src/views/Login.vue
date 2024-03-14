<template>
  <div class="container">
    <div class="title">
      <p class="maintitle" @click="backToHome">秘密基地</p>
      <p class="subtitle">管理入口</p>
    </div>
    <div class="logbox">
      <div class="username">
        <span>UserName:</span>
        <input class="userbox" />
      </div>
      <div class="password">
        <span>PassWord:</span>
        <input class="passwordbox" type="password" />
      </div>
      <el-button type="primary" round @click="login">登录</el-button>
    </div>
  </div>
</template>

<script setup>
import router from "@/router";


const login = () => {
  router.replace({ path: "/usercenter" });
};

const backToHome = () => {
  router.push({path:"/"});
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    .maintitle {
      font-size: 48px;
      cursor: pointer;
    }
    .subtitle {
      font-size: 24px;
      color: #999;
      position: relative;
      bottom: 60px;
    }
  }
  input {
    border-radius: 8px;
    height: 24px;
    width: 180px;
    padding: 4px; /* 设置内边距 */
    border: 1px solid #ccc; /* 设置边框颜色和粗细 */
    font-size: 14px;
    color: #333;
    text-align: left; /* 文本对齐方式 */
  }
  .logbox {
    width: 280px;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .username {
    display: flex;
    justify-content: space-between;
  }
  .password {
    display: flex;
    justify-content: space-between;
  }
}
</style>