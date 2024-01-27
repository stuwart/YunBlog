import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/Home.vue"
import Tag from "@/views/Tag.vue"
import Category from '@/views/Category.vue'
import Timeline from '@/views/Timeline.vue'

const routes = [
  {
    path: '/',
    component:Home,
  },
  {
    path: "/category",
    component: Category
  },
  {
    path:"/Tag",
    component:Tag
  },
  {
    path:"/Timeline",
    component:Timeline
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes:routes
})

export default router
