from flask import Flask, request
import jwt_utils
from classes.Question import CountQuestions, CreateQuestion, GetQuestion, DeleteQuestion, UpdateQuestion, GetAllQuestions

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	size = CountQuestions()
	return {"size": size, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	if payload['password'] == 'Vive l\'ESIEE !':
		return {"token": jwt_utils.build_token()}, 200
	return '', 401

@app.route('/questions', methods=['POST'])
def AddQuestion():
	token = request.headers.get('Authorization')
	if token is None or jwt_utils.decode_token(token.removeprefix("Bearer ")) != "quiz-app-admin":
		return '', 401
	return CreateQuestion(request.get_json())

@app.route('/questions/<position>', methods=['GET'])
def GetQuestionByPosition(position):
	return GetQuestion(position)

@app.route('/questions', methods=['GET'])
def GetQuestions():
	return GetAllQuestions()

@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestionByPosition(position):
	token = request.headers.get('Authorization')
	if token is None or jwt_utils.decode_token(token.removeprefix("Bearer ")) != "quiz-app-admin":
		return '', 401
	return DeleteQuestion(position)

@app.route('/questions/<position>', methods=['PUT'])
def UpdateQuestionByPosition(position):
	token = request.headers.get('Authorization')
	if token is None or jwt_utils.decode_token(token.removeprefix("Bearer ")) != "quiz-app-admin":
		return '', 401
	payload = request.get_json()
	return '', UpdateQuestion(position, payload)

if __name__ == "__main__":
	app.run(ssl_context='adhoc')