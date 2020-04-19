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
            Good {{getDayPart()}}, DOE member!
          </h1>
        <v-card
          class="d-flex align-content-center flex-wrap transparent"
          flat
          width="80%"
          heigth="33%"
          min-height="200"
        >
          <v-flex xs12 sm8 md6 lg4>
            <v-card class="text-center justify-left card" color="#241663" @click="clicked">
                <v-card-text>
                    <div class="heading">
                    Template
                    </div>
                </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs12 sm10 md8 lg6>
            <h1 class="text-right call_for_action">
                -   Create new feedback form
            </h1>
          </v-flex>
          <v-flex xs12 sm10 md8 lg6>
            <h1 class="text-center call_for_action">
                See results -
            </h1>
          </v-flex>
          <v-flex xs12 sm8 md6 lg4>
            <v-card class="text-center justify-left card" color="#241663" @click="clicked">
                <v-card-text>
                    <div class="heading">
                        Results
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
        {name: 'Software Project', tofill: 'true'},
        {name: 'Control Theory', tofill: 'true'},
        {name: 'Networks', tofill: 'true'},
        {name: 'Probability and Statistics', tofill: 'true'},
        {name: 'Sport', tofill: 'true'},
        {name: 'Artificial Intelligence', tofill: 'true'}
      ]
    }
  },
  methods: {
    clicked() {
      console.log("clicked");
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

  .heading{
    font-family: "Poppins";
    font-style: normal;
    font-size: 150%;
    font-weight: 30;
    line-height: 400%;
    
  }

  .call_for_action{
      font-family: "Poppins";
      font-style: normal;
      letter-spacing: 0.05em;
      color: #241663;
      font-weight: 600;
      text-shadow: 0px 3px 4px #EAE7AF;
      margin-top: 25%;
  }

  .card{
      margin-top: 30%;
  }

  .transparent {
    border-color: transparent!important;
  }
</style>
