import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookie'

Vue.use(Vuex);

export default new Vuex.Store({

  state:{
    username:Cookie.get('user'),
    token:Cookie.get('token'),
    apiList:{
      auth:'http://127.0.0.1:8033/api/v1/login/',
      course:'http://127.0.0.1:8033/api/v1/course/',
      coursedetail:'http://127.0.0.1:8033/api/v1/course/detail/',


    }
  },
  mutations:{
    saveToken:function (state, user, token) {
      state.username = user;
      Cookie.set('user', user, '60min');
      Cookie.set('token', token, '60min');
    },
    clearToken:function (state) {
      state.username = null;
      Cookie.delete('user');
      Cookie.delete('token');

    }
  }
})
