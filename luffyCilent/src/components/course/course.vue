<template>
 <div class="container">
   <div class="row">
     <div><h3>课程列表</h3></div>

     <div v-for="item in msg">
       <div><img src="../../assets/logo.png"></div>
       <router-link :to="{path:'/course/detail/'+item.id}">{{ item.name }}</router-link>
       <div>难度：{{ item.level_name }}</div>
       <div>简介：{{ item.brief }}</div>

     </div>


   </div>
 </div>

</template>

<script>
  export default {
    data() {
      return {
        msg :[],

      }
    },
    mounted:function () {
//      console.log(111111,this.$store.state.apiList.course);
      var self = this;

      this.$axios({
        url: this.$store.state.apiList.course,
        method: 'GET',

      })
        .then(function (response) {
          if(response.data.code == 1000){
            self.msg = response.data.data;
          }
        })
    }
  }
</script>

<style>

</style>
