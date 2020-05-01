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
					<span><v-text-field v-model="surveyName" label="Name of Survey" solo outlined
            shaped hint="Name of Course" :rules="['Required']"/></span>
					<div v-for="(question, index) in questions" :key="index">
						<!-- {{question.title}} -->
						<v-text-field v-model="question.title" hint="Question"/>
						<v-text-field v-if="question.type==='text'" background-color="white" label="Answer" disabled hint="Answer to the question"/>
						<v-radio-group row v-if="question.type==='radio'">
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
		}
	},
	methods:{
		async createSurvey(){
			const response = await fetch('/api/new_survey', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					surveyName: this.surveyName,
					questions: this.questions,
				}),
			});
			if(!response.ok) return;
			const json = await response.json();
			// console.log(json);
			this.$router.push({path:`/${this.$store.state.status}`});
		}
	}
}
</script>