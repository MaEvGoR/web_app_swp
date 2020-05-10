import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Student from '../views/Student.vue'
import DOE from '../views/DOE.vue'
import NewSurvey from '../views/NewSurvey.vue'
import Survey from '../views/Survey.vue'
import Years from '../views/Years.vue'
import Courses from '../views/Courses.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/template',
    name: 'NewSurvey',
    component: NewSurvey
  },
  {
    path: '/student',
    name: 'Student',
    component: Student
  },
  {
    path: '/doe',
    name: 'DOE',
    component: DOE
  },
  {
    path: '/survey',
    name: 'Survey',
    component: Survey
  },
  {
    path: '/years',
    name: 'Years',
    component: Years
  },
  {
    path: '/courses',
    name: 'Courses',
    component: Courses
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
