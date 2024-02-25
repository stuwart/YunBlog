import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/Home.vue"
import Tag from "@/views/Tag.vue"
import Project from '@/views/Project.vue'
import Timeline from '@/views/Timeline.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import Login from '@/views/Login.vue'
import UserCenter from '@/views/UserCenter.vue'


const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: "/project",
    component: Project,
  },
  {
    path: "/tag",
    component: Tag,
  },
  {
    path: "/timeline",
    component: Timeline,
  },
  {
    path:"/article/:id",
    component:ArticleDetail,
    props:true
  },
  {
    path:"/login",
    component:Login,
  },
  {
    path:"/center",
    component:UserCenter,
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
