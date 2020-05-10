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
            Choose course:
          </h1>
        <v-card
          class="d-flex align-content-center flex-wrap transparent"
          flat
          width="80%"
          heigth="33%"
          min-height="200"
        >
          <v-flex xs12 sm6 md4 lg4 v-for="course in courses" :key="course.name">
            <v-card class="text-center ma-2" color="#241663" @click="getSurvey(course._id)">
              <v-card-text>
                <div class="heading">
                    {{course.name}}
                </div>
              </v-card-text>
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
      courses: [],
    }
  },
  mounted: function(){
      this.getCourses(this);
  },
  methods: {
    async getCourses(vm) {
      const response = await fetch('/api/courses', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            year: this.$store.state.year,
          }),
        });
      if(!response.ok) return;
      vm.courses = await response.json();
    },
    async getSurvey(id){
      this.$store.commit("changeIdCourse", id);
      this.$router.push({path:`/template`});
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
    margin-bottom: 5%;
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
