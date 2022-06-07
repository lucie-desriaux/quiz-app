<template>
  <div class="main-container">
    <div class="container-left">
      <h2>Testez vos connaissances</h2>
      <img
        alt="Vue logo"
        class="logo"
        src="@/assets/images/logo2.png"
        width=""
        height="60"
      />
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="$router.push('/start-new-quiz-page')"
      >
        Démarrer le quiz !
      </button>
    </div>
    <div class="container-center">
      <div class="trait"></div>
    </div>
    <div class="container-right">
      <h3>Meilleurs scores</h3>
      <div class="cont-score">
        <div
          class="name-score"
          v-for="scoreEntry in registeredScores"
          v-bind:key="scoreEntry.date"
        >
          <div>{{ scoreEntry.playerName }}</div>
          <div class="score">{{ scoreEntry.score }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    participationStorageService.clear();
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoApiResult.data.scores;
    this.registeredScores = quizInfo;
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
  width: 100%;
  padding: 0 2% 0 2% 0;
}

.cont-score {
  width: 50%;
  height: 200px;
  overflow-y: auto;
  scrollbar-color: #d393eb;
  scrollbar-width: thin;
}

.score {
  font-weight: bold;
  padding-right: 5%;
}
</style>
