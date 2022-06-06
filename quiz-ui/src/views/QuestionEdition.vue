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
    <button
      type="button"
      class="btn btn-outline-primary btn-grey"
      @click="backToList"
    >
      Retour à la liste des questions
    </button>
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
    async createOrUpdate() {
      if (this.checkForm()) {
        console.log("Formulaire valide");
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
        if (this.editMode === "create") {
          var quizApiResult = await quizApiService.postQuestion(body, token);
        } else {
          var quizApiResult = await quizApiService.putQuestion(
            this.question.position,
            body,
            token
          );
        }
        switch (quizApiResult.status) {
          case 200:
            alert("Question sauvegardée avec succès !");
            this.$router.go();
            break;
          case 400:
            alert("Réponses invalides, veuillez vérifier vos saisies.");
            break;
          case 403:
            alert("Position invalide.");
            break;
          case 404:
            alert("Question non trouvée");
            break;
          default:
            alert(
              "Erreur : veuillez vérifiez vos saisies ou réessayez plus tard."
            );
            break;
        }
      } else {
        console.log("Formulaire invalide");
        alert("Formulaire invalide, vérifiez vos entrées.");
      }
    },
    cancelEdit() {
      return this.$router.go();
    },
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    backToList() {
      return this.$router.go();
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
