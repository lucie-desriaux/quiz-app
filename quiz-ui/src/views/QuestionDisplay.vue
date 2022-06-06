<template>
  <div v-if="display === 'admin'">
    <p>{{ question.text }}</p>
    <p>{{ question.title }}</p>
    <img v-if="question.image" :src="question.image" width="50" />
    <a
      v-for="(possibleAnswers, index) in question.possibleAnswers"
      @click="$emit('answer-selected', index)"
      style="color: green"
    >
      {{ possibleAnswers.text }}
    </a>
  </div>
  <div v-else>
    <p>{{ question.text }}</p>
    <p>{{ question.title }}</p>
    <img v-if="question.image" :src="question.image" />
    <a
      v-for="(possibleAnswers, index) in question.possibleAnswers"
      @click="$emit('answer-selected', index)"
    >
      {{ possibleAnswers.text }}
    </a>
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

<style></style>
