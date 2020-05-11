import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Student from '../views/Student.vue'
import DOE from '../views/DOE.vue'
import NewSurvey from '../views/NewSurvey.vue'
import Survey from '../views/Survey.vue'
import Years from '../views/Years.vue'
import Courses from '../views/Courses.vue'
import SurveyList from '../views/SurveyList.vue'
import Fillsurvey from '../views/Fillsurvey.vue'
import Result from '../views/Result.vue'
import SurveyResults from '../views/SurveyResults'

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
  {
    path: '/surveylist',
    name: '/SurveyList',
    component: SurveyList
  },
  {
    path: '/fillsurvey',
    name: 'Fillsurvey',
    component: Fillsurvey
  },
  {
    path: '/result',
    name: 'Result',
    component: Result
  },
  {
    path: '/results',
    name: 'SurveyResults',
    component: SurveyResults
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
