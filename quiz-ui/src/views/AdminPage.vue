<template>
  <div v-if="adminMode === 'login'" id="login" class="main-container flex-column">
    <h2>Connexion compte administrateur</h2>
    <p>Saisissez le mot de passe administrateur :</p>
    <div class="input-container">
      <div class="eye-mdp">
        <input id="password" type="password" placeholder="Mot de passe" v-model="password" />
        <i class="eye" @click="switchPasswordVisibility">
          👁
        </i>
      </div>
      <button type="button" class="btn btn-outline-primary btn-grey" @click="checkPassword">
        Connexion
      </button>
    </div>
    <p id="wrongPasswordMsg" style="color: red; visibility: hidden">
      Mot de passe erroné
    </p>
  </div>
  <div v-else id="admin" class="flex-column">
    <!-- <h1>Administration</h1> -->
    <QuestionAdminDisplay v-if="action === 'display'" />
    <QuestionEdition v-else-if="action === 'edit'" :question="questionToEdit" />
    <QuestionsList v-else @question-selected="questionClickedHandler" />
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
      questionToEdit: {
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
    this.questionToEdit.text = "Test hey";
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
    async questionClickedHandler(position) {
      console.log("Question n°" + position);
      var quizApiResult = await quizApiService.getQuestion(position);
      this.action = "edit";
      this.questionToEdit = quizApiResult.data;
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
</style>
