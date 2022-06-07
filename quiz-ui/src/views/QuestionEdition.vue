<template>
  <div class="container-edit-question">
    <h3>Edition de question</h3>
    <div class="">
      <div class="en-tete">
        <div>
          <input
            id="position"
            type="number"
            min="1"
            placeholder="1"
            v-model="position"
          />
        </div>
        <div>
          <input id="title" type="text" placeholder="Titre" v-model="title" />
        </div>
        <div>
          <input id="text" type="text" placeholder="Question" v-model="text" />
        </div>
      </div>

      <div class="container-img-reponses">
        <div class="img-edit">
          <ImageUpload @file-change="imageFileChangedHandler" />
        </div>
      </div>
      <div class="container-bonne-rep">Bonne réponse</div>
      <div class="container-img-reponses">
        <div class="rep-edit">
          <div v-for="index in possibleAnswers.length" :key="index">
            <PossibleAnswerForm
              :index="index - 1"
              :possibleAnswer="possibleAnswers[index - 1]"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="btn-container">
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
          case 401:
            alert("Reconnectez-vous.");
            authStorageService.clear();
            this.$router.go();
            break;
          case 500:
            alert("Reconnectez-vous.");
            authStorageService.clear();
            this.$router.go();
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
  margin: 2%;
  width: 80%;
  margin: 0 auto;
  height: 60vh;
}

.container-edit-question h3 {
  text-align: center;
  margin-bottom: 0;
}

.container-img-reponses {
  display: flex;
  width: 95%;
  margin: 0 auto;
  justify-content: space-around;
  margin-top: 2%;
}

.container-bonne-rep {
  margin-top: 2%;
  margin-left: 75%;
  display: inline-block;
}

.img-edit {
  display: flex;
  flex-direction: column;
}

.rep-edit {
  width: 70%;
}

.rep-edit input:first-child {
  width: 92%;
  margin-right: 2%;
  margin-bottom: 2%;
}

.en-tete {
  width: 50%;
  margin: 0 auto;
  margin-top: 1%;
}

.en-tete div {
  text-align: center;
  margin: 0 auto;
  margin-bottom: 2%;
}

#position {
  width: 10%;
}

div #title,
div #text {
  width: 100%;
}

.btn-container {
  width: 40%;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
}
</style>
