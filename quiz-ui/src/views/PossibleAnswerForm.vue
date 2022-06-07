<template>
  <div>
    <input
      type="text"
      placeholder="Réponse possible"
      v-model="possibleAnswer.text"
    />
    <input
      class="form-check-input"
      type="checkbox"
      id="isCorrect"
      v-model="possibleAnswer.isCorrect"
    />
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
};
</script>

<style>
.form-check-input {
  border: lightcoral solid 1px;
  width: 20px;
  height: 20px;
}

.form-check-input:checked {
  background-color: lightcoral;
  border: lightcoral solid 1px;
}

.form-check-input:focus {
  outline: none;
}
</style>
