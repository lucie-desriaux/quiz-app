<template>
  <h1>Question Admin Display page</h1>
  <button type="button" class="btn btn-outline-primary btn-grey btn-sm"
    @click="$emit('edit-question', question.position)">
    Editer
  </button>
  <button type="button" class="btn btn-outline-primary btn-grey btn-sm"
    @click="$emit('delete-question', question.position)">
    Supprimer
  </button>
  <QuestionDisplay display="admin" :question="question" @answer-selected="" />
</template>

<script>
import QuestionDisplay from "@/views/QuestionDisplay.vue";

export default {
  name: "QuestionAdminDisplay",
  emits: ["edit-question", "delete-question"],
  components: { QuestionDisplay },
  props: {
    question: {
      type: Object,
    },
  },
  data() {
    return {};
  },
  async created() {
    console.log("Composant Question Admin Display page 'created'");
  },
};
</script>

<style>
</style>
