<template>
  <div class="main-container flex-column">
    <h2>Nouvelle partie</h2>
    <p>Saisissez votre nom :</p>
    <div class="input-container">
      <input type="text" placeholder="Username" v-model="username" />
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="launchNewQuiz"
        :disabled="username === null || username.trim() === ''"
      >
        GO!
      </button>
    </div>
  </div>
</template>

<script>
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
  async created() {
    console.log("Composant New Start Quiz page 'created'");
    participationStorageService.clear();
  },
};
</script>

<style>
@font-face {
  font-family: "Disney";
  src: url("../assets/waltograph42.otf");
}

.main-container h2 {
  margin-bottom: 4%;
}

.input-container {
  display: flex;
  margin: 0 auto;
  width: 50%;
  justify-content: space-around;
}

.input-container input {
  height: 100%;
  padding: 0;
  width: 60%;
  height: 35px;
}

.input-container input[type="text"],
.input-container input[type="password"] {
  padding: 12px 10px;
  box-sizing: border-box;
  color: lightslategray;
}

.input-container input[type="text"]:focus,
.input-container input[type="password"]:focus {
  outline: none;
}

.input-container input:focus::placeholder {
  color: transparent;
}

.input-container button {
  border-radius: 0%;
  margin: 0;
  width: 30%;
}
</style>
