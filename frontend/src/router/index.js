import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/Home.vue"
import Tag from "@/views/Tag.vue"
import Project from '@/views/Project.vue'
import Timeline from '@/views/Timeline.vue'
import TagArticleVue from '@/components/TagArticle.vue'
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
    path: "/Tag",
    component: Tag,
    children: [
      {
        path: '/:id',
        component: TagArticleVue
      }
    ]
  },
  {
    path: "/Timeline",
    component: Timeline,
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
