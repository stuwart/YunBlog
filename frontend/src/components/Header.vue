<template>
  <div class="head">
    <RouterLink to="/login" class="word no-underline"> 一路向前 </RouterLink>
    <span class="right">
      <div class="search">
        <Transition>
          <div class="sbox" v-if="isSearch">
            <input
              type="text"
              v-model="searchText"
              @keyup.enter="clicksearch"
            />
          </div>
        </Transition>
        <img
          src="/search.png"
          alt="搜索"
          class="searchicon"
          @click.prevent="clicksearch"
        />
      </div>
      <RouterLink to="/" class="no-underline" @click="backToHome"
        >首页</RouterLink
      >
      <RouterLink to="/tag" class="no-underline">标签</RouterLink>
      <RouterLink to="/timeline" class="no-underline">时间线</RouterLink>
      <RouterLink to="/project" class="no-underline">关于</RouterLink>
    </span>
  </div>
  
</template>
  
<script setup>
import { Transition } from "vue";
import { RouterLink } from "vue-router";
import "@/assets/base.css";
import { ref } from "vue";

const emits = defineEmits(["search"]);

const isSearch = ref(false);
const searchText = ref("");

const clicksearch = () => {
  if (!isSearch.value) {
    isSearch.value = true;
  } else {
   
    const text = searchText.value.trim();
    emits("search", text);
  }
};

const backToHome = () => {
  emits("search", "");
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
    left: 45px;
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


</style>