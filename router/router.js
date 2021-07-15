import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {path: '/', name: 'index', component: () => import('../src/view/index.vue')}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router