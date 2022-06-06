<template>
  <div class="container-edit-question">
    <h2>Edition de question</h2>
    <p>Texte</p>
    <div class="input-container">
      <input
        id="position"
        type="number"
        min="1"
        placeholder="1"
        v-model="position"
      />
      <input id="title" type="text" placeholder="Titre" v-model="title" />
      <input id="text" type="text" placeholder="Intitulé" v-model="text" />
      <ImageUpload @file-change="imageFileChangedHandler" />
      <div v-for="index in 4" :key="index">
        <PossibleAnswerForm
          :index="index - 1"
          :possibleAnswer="possibleAnswers[index - 1]"
        />
      </div>
    </div>
    <div>
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="createOrUpdate"
      >
        Sauvegarder
      </button>
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="cancelEdit"
      >
        Annuler
      </button>
    </div>
  </div>
</template>

<script>
import ImageUpload from "@/views/ImageUpload.vue";
import PossibleAnswerForm from "@/views/PossibleAnswerForm.vue";
import quizApiService from "@/services/QuizApiService";
import authStorageService from "@/services/AuthStorageService";

export default {
  name: "QuestionEdition",
  components: {
    ImageUpload,
    PossibleAnswerForm,
  },
  data() {
    return {
      title: "",
      text: "",
      position: 1,
      image: "",
      possibleAnswers: [
        {
          text: "",
          isCorrect: false,
        },
        {
          text: "",
          isCorrect: false,
        },
        {
          text: "",
          isCorrect: false,
        },
        {
          text: "",
          isCorrect: false,
        },
      ],
    };
  },
  props: {
    editMode: String,
    question: {
      type: Object,
    },
  },
  methods: {
    checkForm() {
      if (this.title === null || this.title.trim() === "") {
        console.log("Titre erroné");
        return false;
      }
      if (this.text === null || this.text.trim() === "") {
        console.log("Intitulé erroné");
        return false;
      }
      if (this.position === null || this.position < 1) {
        console.log("Position set à 1");
        this.position = 1;
      }
      // Check answers
      var nbOfAnswers = 0;
      var nbOfCorrectAnswers = 0;
      this.possibleAnswers.forEach((pa) => {
        if (pa.text != null && pa.text.trim() != "") {
          nbOfAnswers += 1;
          if (pa.isCorrect) {
            nbOfCorrectAnswers += 1;
          }
        }
      });
      if (nbOfAnswers < 2 || nbOfCorrectAnswers != 1) {
        console.log("Réponses non valides");
        return false;
      }
      return true;
    },
    createOrUpdate() {
      if (this.checkForm()) {
        console.log("Form ok");
        var token = authStorageService.getToken();
        var answers = "";
        for (let i = 0; i < this.possibleAnswers.length; i++) {
          if (
            this.possibleAnswers[i].text != null &&
            this.possibleAnswers[i].text.trim() != ""
          ) {
            if (answers === "") {
              answers +=
                '{"text":"' +
                this.possibleAnswers[i].text +
                '","isCorrect":' +
                this.possibleAnswers[i].isCorrect +
                "}";
            } else {
              answers +=
                ',{"text":"' +
                this.possibleAnswers[i].text +
                '","isCorrect":' +
                this.possibleAnswers[i].isCorrect +
                "}";
            }
          }
        }
        var body =
          '{"text":"' +
          this.text +
          '","title":"' +
          this.title +
          '", "image":"' +
          this.image +
          '", "position":' +
          this.position +
          ', "possibleAnswers": [' +
          answers +
          "]}";
        console.log(body);
        if (this.editMode === "create") {
          var quizApiResult = quizApiService.postQuestion(body, token);
        } else {
          var quizApiResult = quizApiService.putQuestion(body, token);
        }
        this.$router.go();
      } else {
        console.log("Form pas ok");
      }
    },
    cancelEdit() {
      return this.$router.go();
    },
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
  },
  async created() {
    console.log("Composant Question Edition page 'created'");
    if (this.editMode === "update") {
      this.title = this.question.title;
      this.text = this.question.text;
      this.position = this.question.position;
      this.image = this.question.image;
      this.possibleAnswers = this.question.possibleAnswers;
    }
  },
};
</script>

<style>
.container-edit-question {
  border: red solid;
  margin: 2%;
}
</style>
