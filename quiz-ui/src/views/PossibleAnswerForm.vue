<template>
  <div>
    <input
      type="text"
      placeholder="Réponse possible"
      v-model="possibleAnswer.text"
    />
    <input type="checkbox" id="isCorrect" v-model="possibleAnswer.isCorrect" />
  </div>
</template>

<script>
export default {
  name: "PossibleAnswerForm",
  props: {
    index: Number,
    possibleAnswer: {
      type: Object,
    },
  },
  data() {
    return {};
  },
  async created() {
    if (this.possibleAnswer === null || this.possibleAnswer == ) {
      console.log("yes");

      this.possibleAnswer = {
        text: "",
        isCorrect: false,
      };
    }
  },
};
</script>

<style></style>
