<template>
  <div class="main-container main-container-score flex-column">

    <div class="container-congrats d-flex">
      <img class="gif" src="../assets/images/stitch-sad.gif" />
      <div>
        <h2>Votre score est de {{ score }} points</h2>
        <p>Bien joué {{ playerName }} ! Vous avez fait un sans faute !</p>
      </div>
    </div>

    <classement></classement>

    <div class="container-score-part d-flex">
      <div class="part-left-score">
        <h3>Meilleurs scores</h3>
        <div class="high-score-container ">
          <div class="heigh-score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
            <div><span class="classement">{{ classement + 1 }}. </span>{{ scoreEntry.playerName }}</div>
            <div class="score"> {{ scoreEntry.score }}</div>
          </div>
        </div>
      </div>
      <div class="part-right-score">
        <h3>Vos scores</h3>
        <div class="your-score-container">
          <div class="your-score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
            <div>{{ scoreEntry.playerName }}</div>
            <div class="score"> {{ scoreEntry.score }}</div>
          </div>
        </div>
      </div>
    </div>
    <button type="button" class="btn btn-outline-primary btn-grey btn-menu" @click="$router.push('/')">
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
      texte: "",
      classement: 0
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
    console.log(this.classement);
    // console.log(quizInfo[sizeArray - 1]);

  },
};
</script>

<style>
.main-container-score {
  /* border: solid green; */
  width: 1000px;
  height: 75%;
}

.gif {
  width: auto;
}

.container-congrats {
  /* border: blue solid; */
  width: 80%;
  height: 30%;
  justify-content: space-around;
  margin: 0 auto;
}


.container-score-part {
  /* border: purple solid; */
  width: 100%;
  height: 60%;
}

.btn-menu {
  height: auto;
  margin: 0 auto;
}

.part-left-score,
.part-right-score {
  /* border: solid grey; */
  width: 50%;
}

.part-left-score h3,
.part-right-score h3 {
  margin-bottom: 2%;
  margin-top: 5%;
}

.your-score-container,
.high-score-container {
  justify-content: space-between;
  overflow-y: auto;
  scrollbar-color: #d393eb lightgrey;
  scrollbar-width: thin;
  height: 65%;
  width: 60%;
  /* border: solid red; */
  margin: 0 auto;
}

.your-score,
.heigh-score {
  display: flex;
  justify-content: space-between;
  padding: 0 5% 0 5%;
}

.classement {
  font-size: 1.5em;
}
</style>
