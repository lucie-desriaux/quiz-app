<template>
  <div class="m-5">
    <h2 class="text-center">Administration - Consultation de toutes les questions</h2>
    <div class="">
      <!-- <h3 class="text-center">Toutes les questions</h3> -->
      <div class="all-questions" v-for="q in questions" v-bind:key="q.position">
        <h4>
          <span class="numero">{{ q.position }}.</span> {{ q.title }} - {{ q.text }}
        </h4>
        <div class="container-img-rep">
          <div class="cont-img">
            <img width="" v-if="q.image" :src="q.image" />
          </div>
          <div class="cont-reponses d-flex flex-column">
            <div class="all-possibleAnswers" v-for="pa in q.possibleAnswers" v-bind:key="pa.index">
              <input type="checkbox" id="isCorrect" v-model="pa.isCorrect" disabled />
              <label for="isCorrect"> {{ pa.text }} </label>
            </div>
          </div>
        </div>
        <button type="button" class="btn btn-outline-primary btn-grey" @click="$emit('question-selected', q.position)">
          Détails
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionList",
  emits: ["question-selected"],
  data() {
    return {
      questions: [{}],
    };
  },
  async created() {
    console.log("Composant Question List page 'created'");
    var quizApiResult = await quizApiService.getQuestions();
    this.questions = quizApiResult.data;
  },
};
</script>

<style>
.m-5 .text-center {
  margin-top: 5%;
}

h4 {
  font-size: 1.1em;
  margin-top: 3%;
  color: #d393eb;
  font-weight: bold;
}

.numero {

  font-size: 1.3em;

}

.container-img-rep {
  display: flex;
  /* border: black solid; */
  width: 80%;
}

.cont-img {
  /* border: green solid; */
  width: 10%;
  text-align: center;
}

.container-img-rep img {
  width: 100%;
  object-fit: cover;
}

.cont-reponses {
  /* border: solid pink; */
  margin-left: 4%;
}

.all-questions button {
  margin-top: 2%;
}
</style>
