import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    surveyName: '',
    id: '',
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
    }
  },
  actions: {
  },
  modules: {
  }
})
