<template>
  <h1>Question Admin Display page</h1>
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
h2 {
  margin: 0 auto;
}

h3 {
  margin-bottom: 5%;
}

.logo {
  margin-top: 7%;
}

.container-left,
.container-right {
  width: 50%;
}

.container-left > * {
  margin-bottom: 15%;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.trait {
  width: 1px;
  height: 60%;
  border-radius: 50px;
  background: rgb(144, 238, 140);
  background: linear-gradient(
    180deg,
    rgba(144, 238, 140, 1) 0%,
    rgba(227, 235, 55, 1) 17%,
    rgba(222, 189, 94, 1) 29%,
    rgba(219, 124, 132, 1) 41%,
    rgba(211, 147, 235, 1) 57%,
    rgba(146, 152, 209, 1) 78%,
    rgba(118, 150, 222, 1) 89%,
    rgba(125, 227, 230, 1) 100%
  );
  filter: blur(0.5px);
}

.container-right {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.name-score {
  display: flex;
  justify-content: space-between;
  width: 40%;
}

.score {
  font-weight: bold;
}
</style>
