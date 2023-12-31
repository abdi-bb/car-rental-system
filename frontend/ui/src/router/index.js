import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import NotFound from '../views/NotFound.vue'

import CarsList from '../components/cars/CarsList.vue';
import CarDetail from '../components/cars/CarDetail.vue';
import CarReviews from '../components/cars/CarReviews.vue';
import CarReviewDetail from '../components/cars/CarReviewDetail.vue';
import CustomersList from '../components/customers/CustomersList.vue';
import CustomerDetail from '../components/customers/CustomerDetail.vue';
import BookingsList from '../components/bookings/BookingsList.vue';
import BookingDetail from '../components/bookings/BookingDetail.vue';



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
    name: 'CarsList',
    component: CarsList
  },
  {
    path: '/car/:id',
    name: 'CarDetail',
    component: CarDetail,
    props: true
  },
  {
    path: '/car/:carId/reviews',
    name: 'CarReviews', // This is the new route for reviews
    component: CarReviews,
  },
  {
    path: '/car/:carId/review/:reviewId',
    name: 'CarReviewDetail',
    component: CarReviewDetail,
  },
  {
    path: '/customers',
    name: 'CustomersList',
    component: CustomersList
  },
  {
    path: '/customer/:id',
    name: 'CustomerDetail',
    component: CustomerDetail,
  },
  {
    path: '/bookings',
    name: 'BookingsList',
    component: BookingsList
  },
  {
    path: '/booking/:id',
    name: 'BookingDetail',
    component: BookingDetail,
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