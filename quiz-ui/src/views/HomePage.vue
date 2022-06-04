<template>
  <div class="main-container">
    <div class="container-left">
      <h2>Testez vos connaissances</h2>
      <img alt="Vue logo" class="logo" src="@/assets/images/logo2.png" width="" height="60" />
      <!-- <router-link to="">Démarrer le quiz !</router-link> -->
      <button type="button" class="btn btn-outline-primary btn-grey" @click="$router.push('/start-new-quiz-page')">
        Démarrer le quiz !
      </button>
    </div>
    <div class="container-center">
      <div class="trait"></div>
    </div>
    <div class="container-right">
      <h3>Meilleurs scores</h3>
      <div class="name-score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        <div>{{ scoreEntry.playerName }}</div>
        <div class="score"> {{ scoreEntry.score }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoApiResult.data.scores;
    this.registeredScores = quizInfo;
    //console.log(quizInfo);
  },
};
</script>

<style>
h2 {
  font-size: 2.5em;
  margin: 0 auto;
}

h3 {
  font-size: 1.5em;
  margin-bottom: 5%;
  color: #d393eb;
  font-weight: bold;
}

.logo {
  margin-top: 7%;
}

.main-container {
  display: flex;
  justify-content: space-around;
  width: 880px;
  text-align: center;
  margin: 0 auto;
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, 25%);
}

.container-left,
.container-right {
  width: 50%;
}

.container-left>* {
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
  background: linear-gradient(180deg, rgba(144, 238, 140, 1) 0%, rgba(227, 235, 55, 1) 17%, rgba(222, 189, 94, 1) 29%, rgba(219, 124, 132, 1) 41%, rgba(211, 147, 235, 1) 57%, rgba(146, 152, 209, 1) 78%, rgba(118, 150, 222, 1) 89%, rgba(125, 227, 230, 1) 100%);
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
