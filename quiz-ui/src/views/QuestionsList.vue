<template>
  <div class="m-5">
    <h3 class="text-center m-0">Consultation de toutes les questions</h3>
    <div class="container-questions-libelle">
      <!-- <h3 class="text-center">Toutes les questions</h3> -->
      <div
        class="all-questions d-flex"
        v-for="q in questions"
        v-bind:key="q.position"
      >
        <a
          class="questions-libelle"
          @click="$emit('show-question', q.position)"
        >
          <span class="numero">{{ q.position }}.</span> {{ q.title }} -
          {{ q.text }}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-pencil-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"
            />
          </svg>
        </a>
        <!-- <button type="button" class="" @click="$emit('show-question', q.position)">
          Détails
        </button> -->
      </div>
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
.m-5 .text-center {
  margin-top: 5%;
}

h4 {
  font-size: 1.1em;
  margin-top: 3%;
  color: #d393eb;
  font-weight: bold;
}

.container-questions-libelle {
  margin: 2% 0 2% 0;
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

.questions-libelle {
  cursor: pointer;
  text-decoration: none;
  color: black;
  /* margin-top: 1; */
}

.questions-libelle:hover {
  background-color: transparent;
  color: #d393eb;
}

.bi-pencil-fill {
  color: lightcoral;
}
</style>
