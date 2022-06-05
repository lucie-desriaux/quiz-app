<template>
  <p>{{ question.questionText }}</p>
  <p>{{ question.questionTitle }}</p>
  <img v-if="question.questionImage" :src="question.questionImage" />
  <a v-for="(possibleAnswers, index) in question.possibleAnswers" @click="$emit('answer-selected', index)">
    {{ possibleAnswers.text }}
  </a>
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
  // methods: {
  //   getQuestion() {
  //     //this.$emit('answer-selected', 2);
  //   },
  // },
};
</script>

<style>
</style>
