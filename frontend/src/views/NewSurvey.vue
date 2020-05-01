<template>
    <v-app>
        <span><v-text-field v-model="surveyName" label="Name of Survey" hint="Name of Course"/></span>
        <div>
                <Question v-for="(question, index) in questions"
                :key="index"
                :title="question.title"
                :type="question.type"
                @remove="questions.splice(index, 1)"/>
        </div>
        <span><v-btn @click="createSurvey">Create Survey</v-btn><v-spacer></v-spacer></span>
    </v-app>
</template>

<script>

import Question from '@/components/Question'


export default{
    name: "Survey",
    data(){
        return{
            surveyName: '',
            questions: [
                {title: "What you don\'t like about the course?", type: 'text'},
                {title: "What do you like about the course?", type: 'text'},
            ],
        }
    },
    components:{
        Question
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
            console.log(json);
            // TODO: need to be done dynamically
            this.$router.push({path:`/doe`});
        }
    }
}
</script>