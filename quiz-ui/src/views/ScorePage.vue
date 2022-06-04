<template>
  <h1>Score : {{ score }}</h1>


  <div>
    <ul id="example-1">
      <li v-for="item in registeredScores" :key="item.date">
        {{ item.playerName }} : {{ item.score }}
      </li>
    </ul>
  </div>


  <button type="button" class="btn btn-outline-danger" @click="$router.push('/')">
    Revenir au menu
  </button>

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "Score",
  data() {
    return {
      registeredScores: [],
      score: participationStorageService.getParticipationScore()
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoApiResult.data.scores;
    this.registeredScores = quizInfo;
    console.log(quizInfoApiResult);

    // console.log(participationStorageService.get)
  },
};
</script>

<style>
</style>
