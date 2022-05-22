import base64
import json
from classes.PossibleAnswer import PossibleAnswer, CreatePossibleAnswers, CheckCorrectAnswer
import db_utils

class Question:
    def __init__(self, title: str, text: str, image: base64, position: int, possibleAnswers: list):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

def JsonToObject(json):
    return Question(
        json['title'],
        json['text'],
        json['image'],
        json['position'],
        PossibleAnswer.JsonToObject(json['possibleAnswers'])
    )

class PossibleAnswerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PossibleAnswer):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def ObjectToJson(obj):
    return json.dumps(obj.__dict__, cls=PossibleAnswerEncoder)

def DbObjectToObject(obj, paList):
    return Question(obj[1], obj[2], obj[3], obj[4], paList)

def DbObjectToJson(obj, paList):
    q = DbObjectToObject(obj, paList)
    return ObjectToJson(q)

def ObjectListToJson(objList):
    return json.dumps([obj.__dict__ for obj in objList], cls = PossibleAnswerEncoder)

def GetQuestionId(position):
    request = f"SELECT id FROM Question WHERE position = {position}"
    res = db_utils.callDb_oneResult(request)
    return res[0] if res != None else ''

def CreateQuestion(json):
    # Check if possible answers are correct
    question = JsonToObject(json)
    if not CheckCorrectAnswer(question.possibleAnswers):
        return 0

    # Insert new question
    request = f"INSERT INTO Question (title, text, image, position) VALUES (\"{question.title}\",\"{question.text}\",\"{question.image}\",{question.position})"
    db_utils.callDb_oneResult(request)
    questionId = GetQuestionId(question.position)

    # Insert possible answers for this question
    CreatePossibleAnswers(questionId, question.possibleAnswers)

def GetQuestion(position):
    request = f"SELECT * FROM Question WHERE position = {position}"
    question = db_utils.callDb_oneResult(request)
    if question is None: 
        return '', 404
    request = f"SELECT * FROM PossibleAnswer WHERE questionId = {question[0]}"
    paList = []
    for pa in db_utils.callDb_multipleResults(request):
        paList.append(PossibleAnswer.DbObjectToJson(pa))
    return DbObjectToJson(question, paList), 200

def GetAllQuestions():
    request = f"SELECT * FROM Question"
    questions = db_utils.callDb_multipleResults(request)
    res = []
    for q in questions:
        request = f"SELECT * FROM PossibleAnswer WHERE questionId = {q[0]}"
        paList = []
        for pa in db_utils.callDb_multipleResults(request):
            paList.append(PossibleAnswer.DbObjectToJson(pa))
        res.append(DbObjectToObject(q, paList))
    return ObjectListToJson(res), 200

def DeleteQuestion(position):
    # Check if question exists
    questionId = GetQuestionId(position)
    if not questionId:
        return 0
    # Delete question
    request = f"DELETE FROM Question WHERE position = {position}"
    db_utils.callDb_oneResult(request)

    # Delete possible answers
    request = f"DELETE FROM PossibleAnswer WHERE questionId = {questionId}"
    db_utils.callDb_oneResult(request)

def UpdateQuestion(position, body):
    # Check if question exists
    questionId = GetQuestionId(position)
    if not questionId:
        return 404

    # Check if possible answers are correct
    question = JsonToObject(body)
    if not CheckCorrectAnswer(question.possibleAnswers):
        return 400

    # Update question
    request = f"UPDATE Question SET title = \"{question.title}\", text = \"{question.text}\", image = \"{question.image}\", position = {question.position} WHERE id = {questionId}"
    db_utils.callDb_oneResult(request)

    # Update possible answers
    request = f"DELETE FROM PossibleAnswer WHERE questionId = {questionId}"
    db_utils.callDb_oneResult(request)
    CreatePossibleAnswers(questionId, question.possibleAnswers)
    return 200