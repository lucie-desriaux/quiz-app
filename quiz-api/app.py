from flask import Flask, request
import jwt_utils
from classes.Question import CreateQuestion, GetQuestion, DeleteQuestion, UpdateQuestion, GetAllQuestions

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

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
	if CreateQuestion(request.get_json()) == 0:
		return '', 400
	return '', 200

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
	if DeleteQuestion(position) == 0:
		return '', 404
	return '', 204

@app.route('/questions/<position>', methods=['PUT'])
def UpdateQuestionByPosition(position):
	token = request.headers.get('Authorization')
	if token is None or jwt_utils.decode_token(token.removeprefix("Bearer ")) != "quiz-app-admin":
		return '', 401
	payload = request.get_json()
	return '', UpdateQuestion(position, payload)

if __name__ == "__main__":
	app.run(ssl_context='adhoc')