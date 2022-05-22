from flask import Flask, request
import jwt_utils
from classes.Question import Question

app = Flask(__name__)

@app.route('/questions', methods=['POST'])
def AddQuestions():
	token = request.headers.get('Authorization')
	if token is None or jwt_utils.decode_token(token.removeprefix("Bearer ")) != "quiz-app-admin":
		return '', 401
	Question.CreateQuestion(request.get_json())
	return '', 201
