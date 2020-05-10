<template>
	<v-app>
		<v-img
      src="@/assets/backgroundv2.png" 
      class="background"
      height = 100%
    >
		<v-container
			backgound-color="white"
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
					<span><h1>{{data.name}}</h1></span>
					<div v-for="(question, index) in data.questions" :key="index">
						<h3>{{question.text}}</h3>
						<!-- <v-text-field v-model="question.title" hint="Question"/> -->
						<v-text-field v-model="question.title" v-if="question.type==='text'" background-color="white" label="Answer" hint="Answer to the question"/>
						<v-radio-group v-model="question.title" row v-if="question.type==='radio'">
							<v-radio 
								v-for="(option,idx) in question.options"
								:key="idx"
								:label="option">
							</v-radio>
						</v-radio-group>
					</div>
					</div>
					<div class="text-center pa-2">
						<v-btn @click="createSurvey">Create Survey</v-btn>
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
			surveyName: '',
			questions: [
				{title: "What you don\'t like about the course?", type: 'text'},
				{title: "What do you like about the course?", type: 'text'},
				{title: "Course structure?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
				{title: "Content of the course?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
				{title: "Quality of lectures?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
				{title: "Quality of labs?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
				{title: "Homework activities?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
				{title: "Clearness of learning?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
			],
			answers: [
				{title: "Answer", type: 'text'},
				{title: "Answer", type: 'text'},
				{title: "Answer", type: 'radio'},
				{title: "Answer", type: 'radio',},
				{title: "Answer?", type: 'radio'},
				{title: "Answer", type: 'radio'},
				{title: "Answer", type: 'radio'},
				{title: "Answer", type: 'radio'},
			],
			otvet: {},
			survey_idtemp: '',
		}
	},
	beforeMount(){
      this.test();
    },
	methods:{
		async test(){
			this.data = this.$store.state.questions;
			console.log(this.data);
			this.survey_idtemp = this.data.survey_id;
		},
		async createSurvey(){
			const temp = {
				"user_id": this.$store.state.id,
				"survey_id": this.survey_idtemp,
				"course_id": this.$store.state.courseid,
				"answers": this.data.questions
			};
			console.log(temp)
			this.otvet = temp;
			const request = await fetch("/api/submit_survey",
				{
				method: "POST",
				headers: {
					'Content-Type': 'application/json',
				},
				cache: "default",
				body: JSON.stringify(this.otvet)
				}
			);
			// if(!response.ok) return;
			// const json = await response.json();
			this.$router.push('/student')
		}
	}
}
</script>