import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    authorised: false,
    surveyName: '',
    surveyList: {},
    id: '',
    year: '',
    idCourse: '',
    idSurvey: '',
    courseName: '',
    surveyName: '',
    pressedButton: '',
    courses: [],
    questoins: {},
    courseid: '',
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
    changeIdSurvey(state, idSurvey){
      state.idSurvey = idSurvey;
    },
    changeButton(state, pressedButton){
      state.pressedButton = pressedButton;
    },
    changeCourses(state, courses){
      state.courses = courses;
    },
    changeSurveyList (state, newSurveylist) { 
      state.surveyList = newSurveylist;
    },
    changeQuestion (state, newQuestion) { 
      state.questions = newQuestion;
    },
    changeCourseid (state, newid) { 
      state.courseid = newid;
    },
    changeCourseName(state, courseName){
      state.courseName = courseName;
    },
    changeSurveyName(state, surveyName){
      state.surveyName = surveyName;
    },
    changeAuthorised(state, authorised){
      state.authorised = authorised;
    }
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
