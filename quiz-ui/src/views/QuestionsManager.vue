<template>
  <div class="container-display-question">
    <h1 class="question-title">
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}
    </h1>
    <QuestionDisplay
      display="quiz"
      :question="currentQuestion"
      @answer-selected="answerClickedHandler"
    />
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return {
      totalNumberOfQuestions: 0,
      currentQuestionPosition: 1,
      currentQuestion: {
        title: "",
        text: "",
        image: "",
        possibleAnswers: [],
      },
      answers: [],
    };
  },
  methods: {
    async loadQuestionByPosition(position) {
      var quizInfoApiResult = await quizApiService.getQuestion(position);
      var q = quizInfoApiResult.data;
      this.currentQuestion.title = q.title;
      this.currentQuestion.text = q.text;
      this.currentQuestion.image = q.image;
      this.currentQuestion.possibleAnswers = q.possibleAnswers;
    },
    async answerClickedHandler(position) {
      position++;
      this.answers.push(position);
      this.currentQuestionPosition + 1 > this.totalNumberOfQuestions
        ? this.endQuiz()
        : this.loadQuestionByPosition(++this.currentQuestionPosition);
    },
    async endQuiz() {
      participationStorageService.saveAnswers(this.answers);
      this.$router.push("/score");
    },
  },
  components: {
    QuestionDisplay,
  },
  async created() {
    console.log("Questions manager 'created'");
    var all = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestions = all.data.size;
    this.loadQuestionByPosition(this.currentQuestionPosition);
  },
};
</script>

<style>
.container-display-question {
  width: 60%;
  max-height: 70%;
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -45%);
  height: 60%;
}

.question-title {
  font-size: 2.5vw;
  width: 100%;
  text-align: center;
  margin: 0;
}
</style>
