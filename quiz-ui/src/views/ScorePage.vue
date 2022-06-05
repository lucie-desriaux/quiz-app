<template>
  <div class="main-container main-container-score flex-column">

    <div class="container-congrats d-flex ">
      <img class="gif" src="../assets/images/stitch-sad.gif" />
      <div>
        <h2>Félicitations {{ playerName }}</h2>
        <h1>Score : {{ score }}</h1>
      </div>

    </div>

    <div class="score-container">
      <div class="name-score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        <div>{{ scoreEntry.playerName }}</div>
        <div class="score"> {{ scoreEntry.score }}</div>
      </div>
    </div>

    <button type="button" class="btn btn-outline-primary btn-grey" @click="$router.push('/')">
      Revenir au menu
    </button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "Score",
  data() {
    return {
      listeQuestions: [],
      registeredScores: [],
      playerName: '',
      score: 0,
      score: participationStorageService.getParticipationScore()
    };
  },
  async created() {
    console.log("Composant Home page 'created'");

    var playerName = participationStorageService.getPlayerName();
    this.playerName = playerName;
    var answers = participationStorageService.getAnswers();
    var body =
      '{"playerName": "' + playerName + '", "answers": [' + answers + "]}";
    var result = await quizApiService.postParticipation(body);
    participationStorageService.saveParticipationScore(result.data.score);
    this.score = result.data.score;
    console.log(result.data.answers);


    var quizInfoApiResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoApiResult.data.scores;
    this.registeredScores = quizInfo;

    var sizeArray = quizInfo.length;
    this.lastRegistered = quizInfo[3];

    console.log(this.lastRegistered);

    console.log("TEST");
    // console.log(quizInfo[sizeArray - 1]);

  },
};
</script>

<style>
.main-container-score {
  border: solid green;
  width: 1000px;
}

.gif {
  width: 30%;
}
</style>
