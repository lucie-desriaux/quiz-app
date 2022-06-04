<template>
  <h1>Result page</h1>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "ResultPage",
  data() {
    return {};
  },
  async created() {
    var playerName = participationStorageService.getPlayerName();
    var answers = participationStorageService.getAnswers();
    var body =
      '{"playerName": "' + playerName + '", "answers": [' + answers + "]}";
    var result = await quizApiService.postParticipation(body);
    participationStorageService.saveParticipationScore(result.data.score);
    console.log(result.data.answers);
  },
};
</script>

<style></style>
