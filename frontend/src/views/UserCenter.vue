<template>
  <Header></Header>
  <div class="main">
    <div class="hello">Hello , 赟！</div>
    <div class="tab">
      <router-link to="/usercenter/dashbord">总览</router-link>
      <router-link to="/usercenter/dashbord">文章</router-link> 
      <span>标签</span>
      <span>项目</span>
    </div>
    <router-view></router-view>

  </div>
</template>


<script setup>
import Header from '@/components/Header.vue';


</script>

<style lang="scss" scoped>
.main{
  .hello{
    font-size: 24px;
    margin: 60px 120px;
    color: #3f3f3f;
  }
  .tab{
    margin: auto;
    display: flex;
    width: 400px;
    font-size: 18px;
    justify-content: space-around;

  }

}

</style>