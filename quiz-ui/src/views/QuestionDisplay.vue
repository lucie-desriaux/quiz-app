<template>
  <div class="container-all-question">
    <div class="question-entete">
      <p class="question-sub-title">{{ question.title }}</p>
      <h3 class="question-libelle">{{ question.text }}</h3>
    </div>

    <div class="container-reponses d-flex">
      <div class="cont-img-question">
        <img
          class="img-questions"
          v-if="question.image"
          :src="question.image"
        />
      </div>
      <div class="reponses d-flex flex-column">
        <a
          class="reponse"
          v-for="(possibleAnswers, index) in question.possibleAnswers"
          @click="$emit('answer-selected', index)"
        >
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
    question: {
      type: Object,
    },
  },
};
</script>

<style>
.container-all-question {
  /* border: purple solid; */
  height: 90%;
  width: 100%;
}

.img-questions {
  width: 100%;
  max-height: 100%;
  object-fit: contain;
  /* box-shadow: 10px 5px 5px lightgrey; */
}

.question-entete {
  /* border: green solid; */
  /* height: 30%; */
}

.cont-img-question {
  display: flex;
  width: 45%;
  /* height: 100%; */
  /* border: purple solid; */
}

.container-reponses {
  justify-content: space-between;
  width: 80%;
  margin: 0 auto;
  /* border: red solid; */
  height: 70%;
}

.reponses {
  font-size: 1vw;

  text-align: start;
  justify-content: center;
  /* border: grey solid; */
  width: 50%;
}

.reponse {
  margin: 1%;
  color: black;
  cursor: pointer;
}

.reponse:hover {
  background-color: transparent;
  color: rgba(118, 150, 222, 1);
  font-size: 1.1vw;
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
  /* margin-top: -1%; */
}
</style>
