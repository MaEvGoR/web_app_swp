import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    surveyName: '',
    surveyList: {},
    id: '',
    year: '',
    idCourse: '',
    courses: [],
  },
  mutations: {
    changeStatus (state, newStatus) {
      state.status = newStatus;
    },
    changeSurveyName (state, newName) {
      state.surveyName = newName;
    },
    changeId(state, id){
      state.id = id;
    },
    changeYear(state, year){
      state.year = year;
    },
    changeIdCourse(state, idCourse){
      state.idCourse = idCourse;
    },
    changeCourses(state, courses){
      state.courses = courses;
    },
    changeSurveyList (state, newSurveylist) { 
      state.surveyList = newSurveylist;
    },
  },
  getters: {
    getSurveyList: state => {
      return state.surveyList;
    },
    getId: state =>{
      return state.id;
    }
  },
  actions: {
  },
  modules: {
  }
})
