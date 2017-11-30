<template>
  <div class="container">
    <div class="col-md-1"><img src="../../assets/luffy_logo.png" class="luffy_logo"></div>
    <div class="col-md-7 col-lg-offset-2">
      <router-link to="/">首页</router-link>
      <router-link to="/course">课程</router-link>
      <router-link to="/micro">Luffy学位</router-link>
      <router-link to="/news">深科技</router-link>
    </div>
    <div class="account col-md-2">
      <div>
            <div class="pull-left login" v-if="this.$store.state.username">
              <san >欢迎您&nbsp;{{ this.$store.state.username }}</san>
              <a @click="logout">注销</a>
            </div>
            <router-link v-else :to="{name:'login',query:{backurl:this.$route.path}}">登录&nbsp;</router-link>
            <router-link to="/register">|&nbsp;注册</router-link>
    </div>
      </div>

  </div>
</template>

<script>
  export default {
    name: 'head',
    methods:{
      logout:function () {
//        console.log(111111111,this.$store.state.token);
        this.$store.commit('clearToken');
        this.$router.push('/');

      }
    }
  }


</script>

<style>
.luffy_logo{
  width: 40px;
  height: 40px;
}
</style>
