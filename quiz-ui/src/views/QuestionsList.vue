<template>
  <div class="m-5">
    <h3 class="text-center m-0">Consultation de toutes les questions</h3>
    <div class="container-questions-libelle">
      <button
        type="button"
        class="btn btn-outline-primary btn-grey btn-sm creer-question"
        @click="$emit('create-question')"
      >
        Créer une question
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-plus-square"
          viewBox="0 0 16 16"
        >
          <path
            d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
          />
          <path
            d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
          />
        </svg>
      </button>
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
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionList",
  emits: ["create-question", "show-question"],
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
  width: 80%;
}

.cont-img {
  width: 10%;
  text-align: center;
}

.container-img-rep img {
  width: 100%;
  object-fit: cover;
}

.cont-reponses {
  margin-left: 4%;
}

.all-questions button {
  margin-top: 2%;
}

.questions-libelle {
  cursor: pointer;
  text-decoration: none;
  color: black;
}

.questions-libelle:hover {
  background-color: transparent;
  color: #d393eb;
}

.bi-search {
  color: lightcoral;
}
</style>
