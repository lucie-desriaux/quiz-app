from flask import Flask, request
from jwt_utils import build_token, decode_token
from classes.Question import CountQuestions, AddQuestion, GetQuestion, DeleteQuestion, UpdateQuestion, GetAllQuestions, ObjectListToJson
from classes.ParticipationResult import GetAllScores, DeleteParticipations, AddParticipation

ADMIN = "quiz-app-admin"

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	size = CountQuestions()
	scores = GetAllScores()
	return {"size": size, "scores": scores}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	if payload['password'] == 'Vive l\'ESIEE !':
		return {"token": build_token()}, 200
	return '', 401

@app.route('/questions', methods=['POST'])
def CreateQuestion():
	token = request.headers.get('Authorization')
	if token is None or decode_token(token.removeprefix("Bearer ")) != ADMIN:
		return '', 401
	return AddQuestion(request.get_json())

@app.route('/questions/<position>', methods=['GET'])
def GetQuestionByPosition(position):
	return GetQuestion(position)

@app.route('/questions', methods=['GET'])
def GetQuestions():
	res = GetAllQuestions()
	return ObjectListToJson(res), 200

@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestionByPosition(position):
	token = request.headers.get('Authorization')
	if token is None or decode_token(token.removeprefix("Bearer ")) != ADMIN:
		return '', 401
	return DeleteQuestion(position)

@app.route('/questions/<position>', methods=['PUT'])
def UpdateQuestionByPosition(position):
	token = request.headers.get('Authorization')
	if token is None or decode_token(token.removeprefix("Bearer ")) != ADMIN:
		return '', 401
	payload = request.get_json()
	return '', UpdateQuestion(position, payload)

@app.route('/participations', methods=['DELETE'])
def DeleteAllParticipations():
	token = request.headers.get('Authorization')
	if token is None or decode_token(token.removeprefix("Bearer ")) != ADMIN:
		return '', 401
	return DeleteParticipations()

@app.route('/participations', methods=['POST'])
def CreateParticipation():
	return AddParticipation(request.get_json())

if __name__ == "__main__":
	app.run(ssl_context='adhoc')