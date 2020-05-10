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
            <!-- Good {{getDayPart()}}, {{data.name}} -->
            Your surveys 
          </h1>
          <h2 class="subintro ">Here’re some feedback forms to fill for you</h2>
        <v-card
          class="d-flex align-content-center flex-wrap transparent"
          flat
          width="80%"
          heigth="33%"
          min-height="200"
        >
         <v-flex xs12 sm6 md4 lg4 v-for="course in data.surveys" :key="course.name">
            <v-card class="text-center ma-2" color="#241663" @click="survey(course)">
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
      message: '',
      courses: [
        {name: 'Software Project'},
        {name: 'Control Theory'},
        {name: 'Networks'},
        {name: 'Probability and Statistics'},
        {name: 'Sport'},
        {name: 'Artificial Intelligence'}
      ],
      // mess: {'course':'Software Project'}
      // mess: {course: 'Control Theory'}
      data: {},
    }
  },
  // beforeMount(){
  //   this.getName();
  // },
    beforeMount(){
      this.test();
    },
  methods: {
    async test(){
      console.log(1111);
      // console.log(this.$store.getters.getSurveyList)
      const tempd = this.$store.getters.getSurveyList;
      // console.log(data);
      this.data = tempd
      console.log(this.data)
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
    },
    async survey() {      
      console.log(this.mess);
      console.log(JSON.stringify(this.mess));
      const request = new Request(
        "http://0.0.0.0:5000/api/student_unfilled",
        {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          // mode: "cors",
          cache: "default",
          body: JSON.stringify(this.mess)
        }
      );
      const res = await fetch(request);
      const data = await res.json();
      this.data = data;
      console.log(data)
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
