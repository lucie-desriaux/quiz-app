<template>
  <h1>Start new quiz page</h1>
  <p>Saisissez votre nom :</p>
  <input type="text" placeholder="Username" v-model="username" />
  <button type="button" class="btn btn-outline-danger" @click="launchNewQuiz">
    GO!
  </button>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push("/questions");
    },
  },
};
</script>

<style></style>
