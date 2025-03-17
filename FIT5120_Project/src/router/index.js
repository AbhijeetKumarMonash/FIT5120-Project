import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import FAQView from '@/views/FAQView.vue'
import trends from '@/views/trends.vue'
import SkinCancerTrends from '@/views/SkinCancerTrends.vue'
import UVIndexView from '@/views/UVIndexView.vue'

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
  {
    path: '/SkinCancerTrends',
    name: 'SkinCancerTrends',
    component: SkinCancerTrends,
  },
  {
    path: '/UVIndex',
    name: 'UVIndex',
    component: UVIndexView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
