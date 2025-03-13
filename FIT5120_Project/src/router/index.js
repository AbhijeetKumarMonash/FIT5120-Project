import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import FAQView from '@/views/FAQView.vue'
import trends from '@/views/trends.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'About',
    component: AboutView,
  },
  {
    path: '/FAQ',
    name: 'FAQ',
    component: FAQView,
  },
  {
    path: '/trends',
    name: 'trends',
    component: trends,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
