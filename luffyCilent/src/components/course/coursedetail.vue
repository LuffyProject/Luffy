<template>
  <div class="container">
    <div CLASS="row col-md-6 col-lg-offset-2">
        <h1>{{ course_name }}</h1>
        <div>
            <p>为什么来学Python?</p>
            <p>{{ why_study }}</p>
            <p>课程先修要求</p>
            <P>{{ prerequisite }}</P>
            <div>
              <span>难度：{{ level }}</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'detail',
        data() {
            return {
                msg: '课程详情页',
                coursedetail:'',
              why_study:'',
              course_name:'',
              prerequisite:'',
              level:'',
            }
        },
        mounted:function () {

          var url = this.$store.state.apiList.coursedetail + this.$route.params.id;
          var self = this;
          this.$axios({
            url:url,
            method: 'GET',
          }).then(function (response) {
            if(response.data.code == 1000){
              self.coursedetail = response.data.data.coursedetail.id;
              self.why_study = response.data.data.coursedetail.why_study;
              self.course_name = response.data.data.coursedetail.course_name;
              self.prerequisite = response.data.data.coursedetail.prerequisite;
              self.level = response.data.data.coursedetail.level;
              console.log(self.coursedetail)
            }
          })
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h1, h2 {
        font-weight: normal;
    }
</style>
