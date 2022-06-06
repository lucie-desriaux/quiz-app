<template>
  <div class="main-container flex-column">
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
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
        questionTitle: "",
        questionText: "",
        questionImage: "",
        possibleAnswers: [],
      },
      answers: [],
    };
  },
  methods: {
    async loadQuestionByPosition(position) {
      var quizInfoApiResult = await quizApiService.getQuestion(position);
      var q = quizInfoApiResult.data;
      this.currentQuestion.questionTitle = q.title;
      this.currentQuestion.questionText = q.text;
      this.currentQuestion.questionImage = q.image;
      this.currentQuestion.possibleAnswers = q.possibleAnswers;
    },
    async answerClickedHandler(position) {
      position++;
      this.answers.push(position);
      console.log("hello : " + position);
      this.currentQuestionPosition + 1 > this.totalNumberOfQuestions
        ? this.endQuiz()
        : this.loadQuestionByPosition(++this.currentQuestionPosition);
    },
    async endQuiz() {
      participationStorageService.saveAnswers(this.answers);
      this.$router.push("/results");
    },
  },
  components: {
    QuestionDisplay,
  },
  async created() {
    console.log("Questions manager 'created'");
    var all = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestions = all.data.size;
    var quizInfoApiResult = await quizApiService.getQuestion(
      this.currentQuestionPosition
    );
    var q = quizInfoApiResult.data;
    this.currentQuestion.questionTitle = q.title;
    this.currentQuestion.questionText = q.text;
    this.currentQuestion.questionImage = q.image;
    this.currentQuestion.possibleAnswers = q.possibleAnswers;
  },
  methods: {
    launchScore() {
      this.$router.push("/score");
    }
  }
};
</script>

<style>
</style>
