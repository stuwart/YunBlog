<template>
  <div class="container">
    <div class="title">
      <p class="maintitle" @click="backToHome">秘密基地</p>
      <p class="subtitle">管理入口</p>
    </div>
    <form class="logbox">
      <div class="username">
        <span>UserName:</span>
        <input class="userbox" v-model="username" />
      </div>
      <div class="password">
        <span>PassWord:</span>
        <input class="passwordbox" type="password" v-model="password" />
      </div>
      <el-button type="primary" round @click.prevent="login">登录</el-button>
    </form>
    <p class="tip" v-if="isWrong">用户名或密码错误！</p>
  </div>
</template>

<script setup>
import router from "@/router";
import { ref } from "vue";

const username = ref("");
const password = ref("");
const isWrong = ref(false);

const login = () => {
  if (username.value === "huangyun" && password.value === "Yg171159") {
    isWrong.value = false;
    router.replace({ path: "/usercenter" });
  } else {
    isWrong.value = true;
  }
};

const backToHome = () => {
  router.push({ path: "/" });
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  .tip {
    color: red;
  }
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