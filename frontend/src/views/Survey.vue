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
					<div style="background-color:white" class="pa-3">
					<h1 condensed >{{surveyName}}</h1>
					<div v-for="(question, index) in questions" :key="index">
						{{question.title}}
						<v-text-field v-if="question.type==='text'" v-model="question.answer" label="Answer" hint="Answer to the question"/>
						<v-radio-group row v-if="question.type==='radio'">
							<v-radio 
								v-for="(option,idx) in question.options"
								:key="idx"
								:label="option"
                                :value="idx">
							</v-radio>
						</v-radio-group>
					</div>
					</div>
					<div class="text-center pa-2">
						<v-btn @click="submit">Send feedback</v-btn>
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
			surveyName: `${this.$store.state.surveyName}`,
			questions: [
				{title: "What you don\'t like about the course?", type: 'text', answer:''},
				{title: "What do you like about the course?", type: 'text', answer:''},
				{title: "Course structure?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
				{title: "Content of the course?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
				{title: "Quality of lectures?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
				{title: "Quality of labs?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
				{title: "Homework activities?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
				{title: "Clearness of learning?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad'], answer:''},
			],
		}
	},
	created: function(){
		if(this.$store.state.id === ''){
		this.$router.push({path:`/`});
		}
  },
	methods:{
		async submit(){
			const response = await fetch('/api/submit_survey', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					surveyName: this.surveyName,
					answers: this.questions,
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