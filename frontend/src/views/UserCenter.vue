<template>
  <Header></Header>
  <div class="main">
    <div class="hello">Hello,赟！</div>
    <div class="tab">
      <span>总览</span>
      <span>文章</span> 
      <span>标签</span>
      <span>项目</span>
    </div>
    


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