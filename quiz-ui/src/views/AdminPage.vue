<template>
  <h1>Page d'administration</h1>
  <div
    v-if="adminMode === 'login'"
    id="login"
    class="main-container flex-column"
  >
    <h1>Connexion compte administrateur</h1>
    <p>Saisissez le mot de passe administrateur :</p>
    <div class="input-container">
      <input
        id="password"
        type="password"
        placeholder="Mot de passe"
        v-model="password"
      />
      <button
        type="button"
        class="btn btn-outline-primary btn-grey btn-sm"
        @click="switchPasswordVisibility"
      >
        👁
      </button>
      <button
        type="button"
        class="btn btn-outline-primary btn-grey"
        @click="checkPassword"
      >
        Connexion
      </button>
    </div>
    <p id="wrongPasswordMsg" style="color: red; visibility: hidden">
      Mot de passe erroné
    </p>
  </div>
  <div v-else id="admin" class="main-container flex-column">
    <h1>Administration</h1>
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-sm"
      @click="createQuestion"
    >
      Créer une question
    </button>
    <button
      type="button"
      class="btn btn-outline-primary btn-grey btn-sm"
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
    />
    <QuestionsList v-else @show-question="showQuestionHandler" />
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import authStorageService from "@/services/AuthStorageService";
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
    var token = authStorageService.getToken();
    //check token is ok TODO
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
      if (quizApiResult) {
        authStorageService.saveToken(quizApiResult.data.token);
        this.adminMode = "admin";
      } else {
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
    async createQuestion() {
      console.log("Create question");
      this.action = "edit";
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
    },
    async deleteQuestionHandler(position) {
      console.log("Delete question n°" + position);
      var token = authStorageService.getToken();
      var quizApiResult = await quizApiService.deleteQuestion(position, token);
      this.action = "";
      this.currentQuestion = null;
      alert("Question n°" + position + " supprimée avec succès.");
    },
    logout() {
      authStorageService.clear();
      return this.$router.go();
    },
  },
};
</script>

<style>
h2 {
  margin: 0 auto;
}

h3 {
  margin-bottom: 5%;
}

.logo {
  margin-top: 7%;
}

.container-left,
.container-right {
  width: 50%;
}

.container-left > * {
  margin-bottom: 15%;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.trait {
  width: 1px;
  height: 60%;
  border-radius: 50px;
  background: rgb(144, 238, 140);
  background: linear-gradient(
    180deg,
    rgba(144, 238, 140, 1) 0%,
    rgba(227, 235, 55, 1) 17%,
    rgba(222, 189, 94, 1) 29%,
    rgba(219, 124, 132, 1) 41%,
    rgba(211, 147, 235, 1) 57%,
    rgba(146, 152, 209, 1) 78%,
    rgba(118, 150, 222, 1) 89%,
    rgba(125, 227, 230, 1) 100%
  );
  filter: blur(0.5px);
}

.container-right {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.name-score {
  display: flex;
  justify-content: space-between;
  width: 40%;
}

.score {
  font-weight: bold;
}
</style>
