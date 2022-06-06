<template>
  <h3 class="question">{{ question.questionText }}</h3>
  <p>{{ question.questionTitle }}</p>

  <div class="container-reponses d-flex">
    <img class="img-questions" v-if="question.questionImage" :src="question.questionImage" />
    <div class="reponses d-flex flex-column ">
      <a v-for="(possibleAnswers, index) in question.possibleAnswers" @click="$emit('answer-selected', index)">
        <div mt-3>
          {{ possibleAnswers.text }}
        </div>
      </a>
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
  methods: {
    getQuestion() {
      //this.$emit('answer-selected', 2);
    },
  },
};
</script>

<style>
.img-questions {
  width: 60%;
}

.container-reponses {
  justify-content: space-between;
  width: 60%;
  margin: 0 auto;
}

.reponses {
  text-align: start;
  justify-content: center;
}

.question {
  margin-bottom: 4%;
}
</style>
