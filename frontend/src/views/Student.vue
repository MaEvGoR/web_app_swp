<template>
  <v-app>
    <v-img
      src="@/assets/backgroundv2.png" 
      class="background"
      height = 100%
    >
      <v-container 
        class="my-5"
      >
        <v-layout row wrap justify-center>
            <h1 class="intro display-4">
            Good {{getDayPart()}}, Student!
            </h1>
            <h2 class="subintro">Here’re some feedback forms to fill for you</h2>
            
            
        <v-card
          class="d-flex align-content-center flex-wrap transparent"
          flat
          width="80%"
          heigth="33%"
          min-height="200"
        >
          
          <v-flex v-if="loading" xs12 sm12 md12 lg12>
            <v-card class="text-center ma-2 elevation-0" style="background-color: transparent">
              <v-progress-circular
                :size="70"
                :width="6"
                color="#241663"
                indeterminate
              ></v-progress-circular>
            </v-card>
          </v-flex>
            
          <v-flex xs12 sm6 md4 lg4 v-for="course in data.courses" :key="course.name">
            <v-card class="ma-2 text-center" color="#241663" @click="clicked(course)">
              <v-card-title class="justify-center" style="height:100px; font-family: 'Poppins';font-style: normal;color: #EFFFFF; font-weight: 30; font-size: 140%;">
                  <p>{{course.name}}</p>
              </v-card-title>
            </v-card>
          </v-flex>
        </v-card>
        </v-layout>
      </v-container>
    </v-img>
  </v-app>
</template>

<script>
export default {
  data(){
    return {
      message: '',
      loading: true,
      data: {}, //for fetch courses
      mess: {}
    }
  },
  mounted: function(){
    this.getCourses(this);
  },
  methods: {
    async getCourses(vm){
      const response = await fetch("/api/student_page",
        {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          cache: "default",
          body: JSON.stringify({
            _id: vm.$store.state.id,
          }),
        }
      );
      // const res = await fetch('http://0.0.0.0:5000/api/student');
      // const data = await res.json();
      // this.data = data;
      vm.data = await response.json();
      vm.loading = false;
      // console.log(this.data);
    },
    async clicked(coursur) {
      // console.log(coursur.course_id);
      const strr = this.$store.state.id
      const message = {
          "_id": strr,
          "course": coursur.name
          };
      this.mess = message;
      // console.log(this.mess)
      //coursur это course surveys
      const request = await fetch("/api/surveys_page",
        {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          cache: "default",
          body: JSON.stringify(this.mess)
        }
      );
      // console.log(2);
      const data = await request.json();
      this.data = data;
      // console.log(this.data)
    //  console.log(data);
      this.$store.commit("changeSurveyList", data);
      this.$store.commit("changeCourseid", coursur.course_id);
      this.$router.push('/surveylist');
      
      
      // this.$store.commit("changeSurveyName", name);
      // this.$router.push({path:`/survey`});
    },
    getDayPart(){
      const hours = new Date().getHours();
      if(4 < hours && hours < 12){
        return 'morning';
      }else if(11 < hours && hours < 18){
        return 'afternoon';
      }else if(17 < hours && hours <= 23){
        return 'evening';
      }else{
        return 'night';
      }
    }
  }
}
</script>

<style>
  .intro{
    font-family: "Poppins";
    color: #EFFFFF;
    font-style: normal;
    -webkit-text-stroke-width: 3px; 
    -webkit-text-stroke-color: black;
    display: flex;
    align-items: center;
    text-align: center;
    margin-top: 4%;
    margin-bottom: 0.5%;
  }
  .subintro{
    font-family: "Poppins";
    font-style: normal;
    display: flex;
    align-items: center;
    text-align: center;
    font-weight: 100;
    color: #000000;
    /* margin-bottom: 5%; */
  }
  .center{
    width:100%
  }
  .heading{
    font-family: "Poppins";
    font-style: normal;
    color: #EFFFFF;
    font-size: 150%;
    font-weight: 30;
    line-height: 400%;
  }
  .transparent {
    border-color: transparent!important;
  }
</style>