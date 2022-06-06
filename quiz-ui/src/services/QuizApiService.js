import axios from "axios";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json"
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
        return { status: error.response.status };
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions/" + position);
  },
  getQuestions() {
    return this.call("get", "questions");
  },
  postParticipation(body) {
    return this.call("post", "participations", body);
  },
  // Administration 
  login(body) {
    return this.call("post", "login", body);
  },
  postQuestion(body, token) {
    return this.call("post", "questions", body, token);
  },
  putQuestion(position, body, token) {
    return this.call("put", "questions/" + position, body, token);
  },
  deleteQuestion(position, token) {
    return this.call("delete", "questions/" + position, null, token);
  },
  deleteParticipations(token) {
    return this.call("delete", "participations", null, token);
  }
};