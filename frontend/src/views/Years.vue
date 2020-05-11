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
          <v-card class="d-flex align-content-center flex-wrap transparent" flat>
          <h1 class="intro display-4">
            Choose year:
          </h1>
          </v-card>
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
          <v-flex xs12 sm6 md4 lg4 v-for="year in years" :key="year.year">
            <v-card class="text-center ma-2" color="#241663" @click="chooseYear(year.year)">
              <v-card-title class="justify-center" style="height:100px; font-family: 'Poppins';font-style: normal;color: #EFFFFF; font-weight: 30; font-size: 140%;">
                  BS{{year.year}}
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
      years: [],
      loading: true,
    }
  },
  created: function(){
    if(this.$store.state.id === ''){
      this.$router.push({path:`/`});
    }
  },
  mounted: function(){
      this.getYears(this);
  },
  methods: {
    async getYears(vm) {
      const response = await fetch('/api/bs_years');
      if(!response.ok) return;
      vm.years = await response.json();
      vm.loading = false;
    },
    chooseYear(year) {
      this.$store.commit("changeYear", year);
      this.$router.push({path:`/courses`});
    },
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
