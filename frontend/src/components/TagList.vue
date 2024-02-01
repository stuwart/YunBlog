<template>
  <div class="left">
    <div v-for = "item in tags" :key="item.id">
        <a href="#">{{ item.name }}({{item.num }})</a>
    </div>
  </div>
</template>

<script setup>
const tags = [
    {
        name : '1111',
        url : 'http:111',
        num: 4
    },
    {
        name : '1111',
        url : 'http:111',
        num:3
    },
    {
        name : '1111',
        url : 'http:111',
        num:2
    },
    {
        name : '1111',
        url : 'http:111',
        num:6
    }
];
</script>

<style lang="scss" scoped>
.left{

}
</style>