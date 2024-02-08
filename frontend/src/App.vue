<script setup>
import { RouterLink, RouterView } from "vue-router";
import Header from "./components/Header.vue";
</script>

<template>
  <RouterView />
</template>

<style>
@font-face {
  font-family: alibaba;
  src: url("@/assets/font/AlibabaPuHuiTi-3-55-Regular.ttf");
}
@font-face {
  font-family: enalibaba;
  src: url("@/assets/font/AlibabaSans-Regular.ttf");
}

html,
body,
#app {
  width: 100%;
  height: auto;
  margin: 0;
  padding: 0;
  font-family: enalibaba,alibaba;
}
html {
  background-color: #f4f4f4;
}
</style>
