import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/Home.vue"
import Tag from "@/views/Tag.vue"
import Project from '@/views/Project.vue'
import Timeline from '@/views/Timeline.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import Login from '@/views/Login.vue'
import UserCenter from '@/views/UserCenter.vue'
import AdminArticle from '@/views/AdminArticle.vue'
import AdminProject from '@/views/AdminProject.vue'
import AdminTag from '@/views/AdminTag.vue'


const coreroutes = [
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
    path: "/usercenter",
    component: UserCenter,
    children: [
      {
        path: 'admin-article',
        component:AdminArticle,
      },
      {
        path: 'admin-tag',
        component:AdminTag,
      },
      {
        path:'admin-project',
        component:AdminProject,
      }
    ]
},
]
const routes = [
  ...coreroutes
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
