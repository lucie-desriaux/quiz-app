<template>
  <h2>Consultation de toutes les questions</h2>
  <div class="container-right">
    <h3>Toutes les questions</h3>
    <div class="all-questions" v-for="q in questions" v-bind:key="q.position">
      <div>{{ q.title }} - {{ q.text }} - {{ q.position }}</div>
      <img width="30" v-if="q.image" :src="q.image" />
      <div
        class="all-possibleAnswers"
        v-for="pa in q.possibleAnswers"
        v-bind:key="pa.index"
      >
        <input type="checkbox" id="isCorrect" v-model="pa.isCorrect" disabled />
        <label for="isCorrect"> {{ pa.text }} </label>
      </div>
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="$emit('show-question', q.position)"
      >
        Détails
      </button>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionList",
  emits: ["show-question"],
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
h2 {
  margin: 0 auto;
}

h3 {
  margin-bottom: 5%;
}

.logo {
  margin-top: 7%;
}

.container-left,
.container-right {
  width: 50%;
}

.container-left > * {
  margin-bottom: 15%;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.trait {
  width: 1px;
  height: 60%;
  border-radius: 50px;
  background: rgb(144, 238, 140);
  background: linear-gradient(
    180deg,
    rgba(144, 238, 140, 1) 0%,
    rgba(227, 235, 55, 1) 17%,
    rgba(222, 189, 94, 1) 29%,
    rgba(219, 124, 132, 1) 41%,
    rgba(211, 147, 235, 1) 57%,
    rgba(146, 152, 209, 1) 78%,
    rgba(118, 150, 222, 1) 89%,
    rgba(125, 227, 230, 1) 100%
  );
  filter: blur(0.5px);
}

.container-right {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.name-score {
  display: flex;
  justify-content: space-between;
  width: 40%;
}

.score {
  font-weight: bold;
}
</style>
