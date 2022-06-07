<template>
  <button type="button" class="btn-retour" @click="$router.go()">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="30"
      height="30"
      fill="currentColor"
      class="bi bi-arrow-left-square-fill"
      viewBox="0 0 16 16"
    >
      <path
        d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"
      />
    </svg>
  </button>
  <h3 class="mt-4 text-center m-0 subtitle-admin">
    Détails de la question n°{{ question.position }}
  </h3>
  <div class="container-display-question-admin">
    <QuestionDisplay display="admin" :question="question" @answer-selected="" />
  </div>
  <div class="container-btn-main">
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-sm"
      @click="$emit('edit-question', question.position)"
    >
      Editer
    </button>
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-sm"
      @click="$emit('delete-question', question.position)"
    >
      Supprimer
    </button>
  </div>
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
  methods: {
    backToList() {
      return this.$router.go();
    },
  },
};
</script>

<style>
.container-display-question-admin {
  box-shadow: 0px 0px 13px 6px rgba(194, 194, 194, 0.65);
  padding: 1% 0 1% 0;
  width: 50%;
  max-height: 70%;
  margin: 0 auto;
  margin-top: 2%;
  margin-bottom: 2%;
}

.container-btn-main {
  display: flex;
  justify-content: space-around;
  width: 35%;
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
}

.btn-retour {
  border: 0;
  background: transparent;
  color: lightcoral;
  position: absolute;
  top: 0;
  left: 3%;
}
</style>
