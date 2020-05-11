<template>
	<v-app>
    <v-img
      src="@/assets/backgroundv2.png" 
      class="background"
      height = 100%
    >
		<v-container
			fluid
			fill-height
		>
			<v-layout row fill-height justify-space-around>
				<v-flex
					xs12
					sm8
					md4
					offset-xs1
				>
					<div style="background-color:white" class="pa-3" center outlined>
            <div v-if="loading" class="text-center">
              <div>
              <v-progress-circular
                :size="70"
                :width="6"
                color="#241663"
                indeterminate
              ></v-progress-circular>
              </div>
              <div class="pa-3">Results are loading</div>
            </div>
            <div class="text-center"><h1>{{courseName}}</h1></div>
            <div class="text-center"><h3>{{surveyName}}</h3></div>
            <div class="text-center">{{surveyDescription}}</div>
            
            <div v-for="(question, index) in results" :key="index">{{question.text}}
              <div v-if="question.type==='text'">
                <v-data-table
                  :headers="[{text: 'Answer', align: 'start',value:'answer',},]"
                  :items="question.answers"
                  :items-per-page="5"
                  class="elevation-0"
                ></v-data-table>
              </div>
              <div v-if="question.type==='radio'">
                <v-data-table
                  :headers="[{text: 'Option', align: 'start',value:'option',},{text: 'Quantity', align: 'start',value:'number',}]"
                  :items="question.answers"
                  :items-per-page="5"
                  :hide-default-footer="true"
                  class="elevation-0"
                ></v-data-table>
              </div>
            </div>
					</div>
					<div class="text-center pa-2">
            <v-btn @click="returnToSurveys" class="ma-2">Return</v-btn>
						<v-btn @click="returnToHome" class="ma-2">Return to Home Page</v-btn>
					</div>
				</v-flex>
			</v-layout>
		</v-container>
    </v-img>
	</v-app>
</template>

<script>
export default{
	name: "Survey",
	data(){
		return{
      courseName: '',
      surveyName: '',
      surveyDescription: '',
      results: [],
      loading: true,
		}
  },
  mounted: function(){
    this.getResults(this);
  },
	methods:{
    async getResults(vm){
      const response = await fetch('/api/get_results', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					survey_id: vm.$store.state.idSurvey,
				}),
			});
			if(!response.ok) return;
      const json = await response.json();
      vm.courseName = json.course_name;
      vm.surveyName = json.name;
      vm.surveyDescription = json.description;
      vm.results = json.results;
      vm.loading = false;
    },
    returnToSurveys(){
      this.$router.push({path:`/results`});
    },
		returnToHome(){
      this.$router.push({path:`/${this.$store.state.status}`});
    }
	}
}
</script>