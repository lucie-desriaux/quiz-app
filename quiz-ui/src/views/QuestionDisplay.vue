<template>
  <div class="container-all-question">
    <div class="question-entete">
      <p class="question-sub-title">{{ question.title }}</p>
      <h3 class="question-libelle">{{ question.text }}</h3>
    </div>
    <div class="container-reponses d-flex">
      <div class="cont-img-question">
        <img class="img-questions" v-if="question.image" :src="question.image" />
      </div>
      <div v-if="display === 'admin'" class="reponses d-flex flex-column">
        <p class="reponse-admin" v-for="(possibleAnswers, index) in question.possibleAnswers"
          @click="$emit('answer-selected', index)">
        <div class="good-answer" v-if="possibleAnswers.isCorrect == 1">{{ index + 1 }}. {{ possibleAnswers.text }}
        </div>
        <div v-else mt-3>{{ index + 1 }}. {{ possibleAnswers.text }}</div>
        </p>
      </div>
      <div v-else class="reponses d-flex flex-column">
        <a class="reponse" v-for="(possibleAnswers, index) in question.possibleAnswers"
          @click="$emit('answer-selected', index)">
          <div mt-3>{{ index + 1 }}. {{ possibleAnswers.text }}</div>
        </a>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  data() {
    return {};
  },
  props: {
    display: String,
    question: {
      type: Object,
    },
  },
};
</script>

<style>
.container-all-question {
  height: 90%;
  width: 100%;
}

.img-questions {
  width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.cont-img-question {
  display: flex;
  width: 45%;
}

.container-reponses {
  justify-content: space-between;
  width: 80%;
  margin: 0 auto;
  height: 70%;
}

.reponses {
  font-size: 20px;

  text-align: start;
  justify-content: center;
  width: 50%;
}

.reponse {
  margin: 1%;
  font-size: 20px;
  color: black;
  cursor: pointer;
}

.reponse:hover {
  background-color: transparent;
  color: rgba(118, 150, 222, 1);
}

.question-libelle {
  margin-bottom: 3%;
  text-align: center;
  font-size: 1.5vw;
}

.question-sub-title {
  text-align: center;
  font-style: italic;
  font-size: 1.2vw;
  margin-bottom: 1%;
}

.good-answer {
  background-color: rgba(99, 237, 90, 0.2);
  cursor: default;
}

.reponse-admin {
  margin: 1%;
  font-size: 20px;
  color: black;
}
</style>
