import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: ''
  },
  mutations: {
    changeStatus (state, newStatus) { 
      state.status = newStatus;
    }
  },
  actions: {
  },
  modules: {
  }
})
