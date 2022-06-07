<template>
  <div class="main-container main-container-score flex-column">
    <div class="container-congrats d-flex">
      <img class="gif" :src="gif" />
      <div>
        <h2>Votre score est de {{ score }} points</h2>
        <p>{{ text }}</p>
        <p>
          Tu es {{ rank }} / {{ registeredScores.length }} au classement
          général.
        </p>
      </div>
    </div>
    <div class="container-score-part d-flex">
      <div class="part-left-score">
        <h3>Meilleurs scores</h3>
        <div class="high-score-container">
          <div
            class="heigh-score"
            v-for="(scoreEntry, index) in registeredScores"
            v-bind:key="scoreEntry.date"
          >
            <div>
              <span class="classement">{{ index + 1 }}. </span
              >{{ scoreEntry.playerName }}
            </div>
            <div class="score">{{ scoreEntry.score }}</div>
          </div>
        </div>
      </div>
      <div class="part-right-score">
        <h3>Vos scores</h3>
        <div class="your-score-container">
          <div
            v-for="scoreEntry in registeredScores"
            v-bind:key="scoreEntry.date"
          >
            <div class="your-score" v-if="scoreEntry.playerName == playerName">
              <div>{{ scoreEntry.playerName }}</div>
              <div class="score">{{ scoreEntry.score }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-menu"
      @click="$router.push('/')"
    >
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
      registeredScores: [],
      playerName: "",
      score: 0,
      text: "",
      rank: 0,
      gif: "",
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var playerName = participationStorageService.getPlayerName();
    this.playerName = playerName;
    if (!participationStorageService.getParticipationScore()) {
      var answers = participationStorageService.getAnswers();
      var body =
        '{"playerName": "' + playerName + '", "answers": [' + answers + "]}";
      var result = await quizApiService.postParticipation(body);
      participationStorageService.saveParticipationScore(result.data.score);
    }
    this.score = participationStorageService.getParticipationScore();
    var questionList = await quizApiService.getQuestions();
    var nbQuestions = questionList.data.length;
    if (this.score == nbQuestions) {
      this.text =
        "Félicitations " + playerName + "! Tu es un vrai fan Disney !";
      this.gif = "../../public/olaf-frozen.gif";
    } else if (
      this.score >= Math.round((4 * nbQuestions) / 5) &&
      this.score < nbQuestions
    ) {
      this.text = "C'est un presque parfait " + playerName + "! Bravo !";
      this.gif = "../../public/donald-good.gif";
    } else if (
      this.score >= Math.round(nbQuestions / 2) &&
      this.score < Math.round((4 * nbQuestions) / 5)
    ) {
      this.text =
        "C'est pas mal " + playerName + ", mais tu peux mieux faire !";
      this.gif = "../../public/happy-cat.gif";
    } else if (this.score >= 1 && this.score < Math.round(nbQuestions / 2)) {
      this.text =
        "Retourne réviser tes classiques " +
        playerName +
        ", et reviens jouer !";
      this.gif = "../../public/stitch-sad.gif";
    } else {
      this.text = "Oups, tu le fais exprès " + playerName + "...?";
      this.gif = "../../public/simba-bad.gif";
    }
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoApiResult.data.scores;
    this.registeredScores = quizInfo;
    var lastSubmitDate = "1970-01-01";
    for (let i = 0; i < this.registeredScores.length; i++) {
      if (
        this.registeredScores[i].playerName == this.playerName &&
        this.registeredScores[i].score == this.score
      ) {
        if (lastSubmitDate < this.registeredScores[i].date) {
          this.rank = i + 1;
          break;
        }
      }
    }
  },
};
</script>

<style>
.main-container-score {
  width: 1000px;
  height: 75%;
}

.gif {
  width: auto;
}

.container-congrats {
  width: 80%;
  height: 30%;
  justify-content: space-around;
  margin: 0 auto;
}

.container-score-part {
  width: 100%;
  height: 60%;
}

.btn-menu {
  height: auto;
  margin: 0 auto;
}

.part-left-score,
.part-right-score {
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
  font-weight: bold;
}
</style>
