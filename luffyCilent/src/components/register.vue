<template>
  <div class="container">
    <!--<h1 class="logo">Welcome to luffy</h1>-->

    <div class="row col-md-6 col-lg-offset-3">
      <input type="text" placeholder="用户名" class="form-control" v-model="user">
      <input type="text" placeholder="密码" class="form-control" v-model="pwd">
      <input type="button" class="btn btn-danger" value="确定" v-on:click="login">
    </div>
  </div>
</template>

<script>
//  import axios from 'axios'

  export default {
//    name: 'HelloWorld',
    data() {
      return {
        user: '',
        pwd: '',
        error:'',

      }
    },
    methods: {
      login: function () {
        let that = this;
        this.error= '';
//        let user = this.user,
//        let pwd = this.pwd
        this.$axios.request({
          url:this.$store.state.apiList.auth,
          method:'POST',
          data:{
            user:this.user,
            pwd:this.pwd,
        },
          responseType:"json",
        }).then(function (response) {
          if(response.data.code === 1000){
            that.$store.commit('saveToken', response.name,response.data.token)
            let backurl = that.$router.query.backurl;
            if(backurl){
              that.$router.push({path:backurl})
            }
          }

        }).cache(function (response) {
          this.error = response.errors
        })

      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  input {
    margin: 30px 0 0 0;
  }

  .logo {
    font-family: "Microsoft JhengHei";
  }
</style>
