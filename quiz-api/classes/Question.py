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

def JsonToObject(body):
    return Question(
        body['title'],
        body['text'],
        body['image'],
        body['position'],
        PossibleAnswer.JsonToObject(body['possibleAnswers'])
    )

class PossibleAnswerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PossibleAnswer):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def ObjectToJson(obj):
    return json.dumps(obj.__dict__, cls = PossibleAnswerEncoder)

def DbObjectToObject(obj, paList):
    return Question(obj[1], obj[2], obj[3], obj[4], paList)

def DbObjectToJson(obj, paList):
    q = DbObjectToObject(obj, paList)
    return ObjectToJson(q)

def ObjectListToJson(objList):
    return json.dumps([obj.__dict__ for obj in objList], cls = PossibleAnswerEncoder)

def CountQuestions():
    request = f"SELECT COUNT(id) FROM Question"
    return db_utils.callDb_oneResult(request)[0]

def CheckPositionCreate(position):
    nbOfQuestions = CountQuestions()
    return True if position <= (nbOfQuestions+1) and position > 0 else False

def CheckPositionUpdate(position):
    nbOfQuestions = CountQuestions()
    return True if position <= nbOfQuestions and position > 0 else False

def IncrementPosition(position):
    newPos = position+1
    request = f"UPDATE Question SET position = {newPos} WHERE position = {position}"
    db_utils.callDb_oneResult(request)

def DecrementPosition(position):
    newPos = position-1
    request = f"UPDATE Question SET position = {newPos} WHERE position = {position}"
    db_utils.callDb_oneResult(request)

def AddPosition(position):
    nbOfQuestions = CountQuestions()
    for i in range(nbOfQuestions, position-1, -1):
        IncrementPosition(i)
        i-=1

def SwitchPositions(actualPos, updatedPos):
    actualPos = int(actualPos)
    request = f"UPDATE Question SET position = 0 WHERE position = {actualPos}"
    db_utils.callDb_oneResult(request)  
    if actualPos < updatedPos:
        for i in range(actualPos+1, updatedPos+1):
            DecrementPosition(i)
    else:
        for i in range(actualPos-1, updatedPos-1, -1):
            IncrementPosition(i)

def DeletePosition(position):
    nbOfQuestions = CountQuestions()
    for i in range(position+1, nbOfQuestions+2):
        DecrementPosition(i)

def GetQuestionId(position):
    request = f"SELECT id FROM Question WHERE position = {position}"
    res = db_utils.callDb_oneResult(request)
    return res[0] if res != None else ''

def AddQuestion(body):
    # Check if question is valid
    if not "title" in body or not "text" in body or not "image" in body or not "position" in body or not "possibleAnswers" in body:
        return '', 400 

    # Check if possible answers are correct
    question = JsonToObject(body)
    if not CheckCorrectAnswer(question.possibleAnswers):
        return '', 400

    # Check if position is valid
    if not CheckPositionCreate(question.position):
        return '', 403

    # If position already exists 
    if GetQuestion(question.position)[1] != 404: 
        AddPosition(question.position)

    # Insert new question
    request = f"INSERT INTO Question (title, text, image, position) VALUES (\"{question.title}\",\"{question.text}\",\"{question.image}\",{question.position})"
    db_utils.callDb_oneResult(request)
    questionId = GetQuestionId(question.position)

    # Insert possible answers for this question
    CreatePossibleAnswers(questionId, question.possibleAnswers)
    return '', 200

def GetQuestion(position):
    request = f"SELECT * FROM Question WHERE position = {position}"
    question = db_utils.callDb_oneResult(request)
    if question is None: 
        return '', 404
    request = f"SELECT * FROM PossibleAnswer WHERE questionId = {question[0]}"
    paList = []
    for pa in db_utils.callDb_multipleResults(request):
        paList.append(PossibleAnswer.DbObjectToObject(pa))
    return DbObjectToJson(question, paList), 200

def GetAllQuestions():
    request = f"SELECT * FROM Question ORDER BY position"
    questions = db_utils.callDb_multipleResults(request)
    res = []
    for q in questions:
        request = f"SELECT * FROM PossibleAnswer WHERE questionId = {q[0]}"
        paList = []
        for pa in db_utils.callDb_multipleResults(request):
            paList.append(PossibleAnswer.DbObjectToObject(pa))
        res.append(DbObjectToObject(q, paList))
    return res

def DeleteQuestion(position):
    # Check if question exists
    questionId = GetQuestionId(position)
    if not questionId:
        return '', 404

    # Delete question
    request = f"DELETE FROM Question WHERE position = {position}"
    db_utils.callDb_oneResult(request)

    # Switch positions after delete
    DeletePosition(int(position))

    # Delete possible answers
    request = f"DELETE FROM PossibleAnswer WHERE questionId = {questionId}"
    db_utils.callDb_oneResult(request)
    return '', 204

def UpdateQuestion(position, body):
    # Check if question exists
    questionId = GetQuestionId(position)
    if not questionId:
        return '', 404

    question = JsonToObject(body)

    # Check if new position is valid 
    if not CheckPositionUpdate(question.position):
        return '', 403

    # Switch positions
    SwitchPositions(position, question.position)

    # Check if possible answers are correct
    if not CheckCorrectAnswer(question.possibleAnswers):
        return '', 400

    # Update question
    request = f"UPDATE Question SET title = \"{question.title}\", text = \"{question.text}\", image = \"{question.image}\", position = {question.position} WHERE id = {questionId}"
    db_utils.callDb_oneResult(request)

    # Update possible answers
    request = f"DELETE FROM PossibleAnswer WHERE questionId = {questionId}"
    db_utils.callDb_oneResult(request)
    CreatePossibleAnswers(questionId, question.possibleAnswers)
    return '', 200

def GetRightAnswers():
    result = []
    position = 1
    questions = GetAllQuestions()
    for q in questions:
        for pa in q.possibleAnswers:
            if pa.isCorrect is True:
                result.append(position)
                break
            position += 1
        position = 1
    return result
