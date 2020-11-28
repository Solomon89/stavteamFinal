import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Login from '@/components/Login'
import Pacient from '@/components/pacient/Pacient'

Vue.use(Router)

let router = new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        guest: true,
        requiresAuth: false
      }
    },
    {
      path: '/pacient/:id',
      name: 'Pacient',
      component: Pacient,
      meta: {
        requiresAuth: true
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  to.matched.some(record => {
    if(record.meta.requiresAuth) {
      if (sessionStorage.getItem('sessionId') === "null" || sessionStorage.getItem('sessionId') === null) {
        next({
          path: '/login'
        });
      } else {
        next();
      }
    } else {
      next();
    }
  })
});

export default router;