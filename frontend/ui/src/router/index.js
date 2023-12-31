import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import NotFound from '../views/NotFound.vue'
import Cars from '../views/cars/Cars.vue'
import CarDetail from '../views/cars/CarDetail.vue'




const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/cars',
    name: 'Cars',
    component: Cars
  },
  {
    path: '/car/:id',
    name: 'CarDetail',
    component: CarDetail,
    props: true
  },
    // redirect
  {
    path: '/car-list',
    redirect: '/cars'
  },
  // 404
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
