<template>

  <div >
    <heads></heads>
    <router-view/>
    <!--<foot></foot>-->
  </div>


</template>

<script>
  import heads from './components/heads/head.vue'
  import foot from './components/foot/foot.vue'
export default {
    components:{
      heads,
      foot
    },
    name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
