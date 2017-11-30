import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import public_page from '@/components/public_page'
import micro from '@/components/micro/micro'
import news from '@/components/news/news'
import course from '@/components/course/course'
import coursedetail from '@/components/course/coursedetail'
import register from '@/components/register'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'public_page',
      component: public_page
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/news',
      name: 'news',
      component: news
    },
    {
      path: '/micro',
      name: 'micro',
      component: micro
    },
    {
      path: '/course',
      name: 'course',
      component: course
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/course/detail/:id',
      name: 'courseDetail',
      component: coursedetail
    },

  ]
})
