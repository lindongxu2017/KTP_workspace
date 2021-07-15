import { createRouter, createWebHistory } from "vue-router"
import * as subRouters from './route.json'

const router =  createRouter({
  history: createWebHistory(),
  routes: []
})

function _import (file) {
  return () => import('../views/' + file + '.vue')
}

router.addRoute({ name: 'index', path: '/', redirect: 'ktpColor', component: () => import("@/views/index.vue") })
subRouters.default.map(item => {
  item.component = _import(item.component)
  router.addRoute('index', {...item, meta: {title: item.title, desc: item.desc}})
})

// console.log(router.getRoutes())

export default router