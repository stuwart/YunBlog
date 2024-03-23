<template>
    <BlogCard
    v-for="item in articles"
    :key="item.id"
    :name="item.title"
    :date="item.created"
    :body="item.body"
    :tags="item.tags"
    :url="item.url"
    :id="item.id"
    class="card"
    ></BlogCard>

</template>

<script setup>
import BlogCard from '@/components/BlogCard.vue';
import { ref } from 'vue';
import axios from 'axios';
const articles = ref([]);

const fetchArticles = async ()=>{
    try{
        const response = await axios.get('/api/article');
        articles.value = response.data.result;
    }catch(error){
        console.error("存在错误：",error);
    }
}

</script>

<style lang="scss" scoped>



</style>