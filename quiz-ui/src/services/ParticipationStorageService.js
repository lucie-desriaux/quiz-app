export default {
  clear() {
		window.localStorage.removeItem("playerName");
		window.localStorage.removeItem("participationScore");
		window.localStorage.removeItem("answers");
  },
  savePlayerName(playerName) {
		window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {		
		return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
		window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
		return window.localStorage.getItem("participationScore");
  },
  saveAnswers(answers) {
		window.localStorage.setItem("answers", answers);
  },
  getAnswers() {
		return window.localStorage.getItem("answers");
  },
};