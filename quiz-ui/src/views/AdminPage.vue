<template>
  <div
    v-if="adminMode === 'login'"
    id="login"
    class="main-container flex-column"
  >
    <h2>Connexion compte administrateur</h2>
    <p>Saisissez le mot de passe administrateur :</p>
    <div class="input-container">
      <div class="eye-mdp">
        <input
          id="password"
          type="password"
          placeholder="Mot de passe"
          v-model="password"
        />
        <i class="eye" @click="switchPasswordVisibility"> 👁 </i>
      </div>
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="checkPassword"
        :disabled="password === null || password.trim() === ''"
      >
        Connexion
      </button>
    </div>
    <p id="wrongPasswordMsg" style="color: red; visibility: hidden">
      Mot de passe erroné
    </p>
  </div>
  <div v-else id="admin" class="flex-column">
    <h1>Administration</h1>
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-sm deconnexion"
      @click="logout"
    >
      Déconnexion
    </button>
    <QuestionAdminDisplay
      v-if="action === 'display'"
      :question="currentQuestion"
      @edit-question="editQuestionHandler"
      @delete-question="deleteQuestionHandler"
    />
    <QuestionEdition
      v-else-if="action === 'edit'"
      :question="currentQuestion"
      :editMode="editMode"
    />
    <QuestionsList
      v-else
      @show-question="showQuestionHandler"
      @create-question="createQuestionHandler"
    />
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import authStorageService from "@/services/AuthStorageService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionAdminDisplay from "@/views/QuestionAdminDisplay.vue";
import QuestionsList from "@/views/QuestionsList.vue";
import QuestionEdition from "@/views/QuestionEdition.vue";

export default {
  name: "AdminPage",
  components: {
    QuestionAdminDisplay,
    QuestionEdition,
    QuestionsList,
  },
  data() {
    return {
      editMode: "create",
      action: "",
      adminMode: "login",
      password: "",
      currentQuestion: {
        title: "",
        text: "",
        image: "",
        position: "",
        possibleAnswers: [],
      },
    };
  },
  async created() {
    console.log("Composant Admin page 'created'");
    participationStorageService.clear();
    var token = authStorageService.getToken();
    if (token) {
      this.adminMode = "admin";
    } else {
      this.adminMode = "login";
    }
  },
  methods: {
    async checkPassword() {
      var body = '{"password":"' + this.password + '"}';
      var quizApiResult = await quizApiService.login(body);
      if (quizApiResult.status == 200) {
        authStorageService.saveToken(quizApiResult.data.token);
        this.adminMode = "admin";
      } else if (quizApiResult.status == 401) {
        const passwordField = document.querySelector("#wrongPasswordMsg");
        passwordField.style.visibility = "visible";
      }
    },
    switchPasswordVisibility() {
      const passwordField = document.querySelector("#password");
      if (passwordField.getAttribute("type") === "password") {
        passwordField.setAttribute("type", "text");
      } else {
        passwordField.setAttribute("type", "password");
      }
    },
    async createQuestionHandler() {
      console.log("Create question");
      this.action = "edit";
      this.editMode = "create";
    },
    async showQuestionHandler(position) {
      console.log("Show question n°" + position);
      var quizApiResult = await quizApiService.getQuestion(position);
      this.action = "display";
      this.currentQuestion = quizApiResult.data;
    },
    async editQuestionHandler(position) {
      console.log("Edit question n°" + position);
      this.action = "edit";
      this.editMode = "update";
    },
    async deleteQuestionHandler(position) {
      console.log("Delete question n°" + position);
      var token = authStorageService.getToken();
      var quizApiResult = await quizApiService.deleteQuestion(position, token);
      this.action = "";
      this.currentQuestion = null;
      switch (quizApiResult.status) {
        case 204:
          alert("Question supprimée avec succès !");
          break;
        case 404:
          alert("Question non trouvée, suppression annulée.");
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
          alert("Erreur lors de la suppression, réessayez plus tard.");
          break;
      }
      this.$router.go();
    },
    logout() {
      authStorageService.clear();
      return this.$router.go();
    },
  },
};
</script>

<style>
.eye {
  position: absolute;
  right: 4%;
  top: 10%;
}

.eye:hover {
  cursor: pointer;
}

.eye-mdp {
  width: 60%;
}

.eye-mdp input {
  width: 100%;
}

.deconnexion {
  position: absolute;
  right: 2%;
  top: -1%;
  width: 8%;
}

.creer-question:hover {
  background-color: white;
  color: lightcoral;
}

#admin h1 {
  text-align: center;
  margin-top: 4%;
}

.creer-question {
  background-color: lightcoral;
  color: white;
  position: fixed;
  bottom: 4%;
  right: 3%;
  z-index: 5;
  height: 45px;
  padding-right: 2%;
  font-size: 16px;
}

.creer-question:focus {
  outline: none !important;
}

.bi-plus-square {
  position: absolute;
  right: 8%;
  top: 31%;
}
</style>
