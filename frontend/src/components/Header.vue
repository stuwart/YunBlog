<template>
  <div class="head">
    <RouterLink to="/login" class="word no-underline"> 一路向前 </RouterLink>
    <span class="right">
      <div class="search">
        <Transition>
          <div class="sbox" v-if="showbox">
            <input type="text" v-model="searchText" />
          </div>
        </Transition>
        <img src="/search.png" alt="搜索" class="searchicon" @click="search" />
      </div>
      <RouterLink to="/" class="no-underline">首页</RouterLink>
      <RouterLink to="/tag" class="no-underline">标签</RouterLink>
      <RouterLink to="/timeline" class="no-underline">归档</RouterLink>
      <RouterLink to="/project" class="no-underline">关于</RouterLink>
    </span>
  </div>
  <div class="empty" />
  <div class="intro">
    <span id="name">赟</span>
    <span id="word">很高兴遇见你</span>
  </div>
  <el-divider />
</template>
  
<script setup>
import { Transition } from "vue";
import { RouterLink } from "vue-router";
import "@/assets/base.css";
import { ref } from "vue";
let showbox = ref(false);

const searchText = ref("");
const search = () => {
  if (!showbox.value) {
    showbox.value = true;
  } else {
    //搜索
    const text = searchText.value.trim();
    // console.log(text);
    // if (text.charAt(0)!='')
  }
};
</script>
  
<style lang="scss" scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
.search {
  margin-right: 40px;
  display: flex; /* 添加flexbox布局 */
  align-items: center; /* 在交叉轴（此处为垂直轴）上居中对齐子项 */
  justify-content: center; /* 可选：在主轴（此处为水平轴）上居中对齐子项，如果你也想水平居中的话 */
  .searchicon {
    cursor: pointer;
    z-index: 2;
    position: relative;
    left: 40px;
  }
  .sbox {
    width: 120px;
    height: 30px;
    position: absolute;
    border: 1px solid #999;
    border-radius: 12px;
    z-index: 1;
    background-color: #f9f9f9;
    padding: 2px;

    input {
      border: 0px;
      width: 90px;
      font-size: 16px;
      &:focus {
        outline: none;
      }
    }
  }
}

.no-underline {
  text-decoration: none;
  border-radius: 4px;
  &:hover {
    background-color: rgb(180, 180, 180);
  }
  &:visited {
    color: #590def;
  }
  &:active {
    filter: brightness(1.2);
  }
}

.head {
  position: relative;
  top: 12px;
  font-size: 18px;
  color: #590def;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  img {
    width: 24px;
    height: 24px;
  }
  .word {
    margin-left: 40px;
    &:visited {
      color: #590def;
    }
  }
  .right {
    margin-right: 40px;
    width: 300px;
    display: flex;
    justify-content: space-around;
  }
}
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