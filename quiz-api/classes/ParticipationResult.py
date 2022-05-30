import datetime
from classes.AnswerSummary import AnswerSummary, SetAnswerSummary
from classes.Question import GetRightAnswers, CountQuestions
from classes.Answer import Answer
import db_utils
import json

class ParticipationResult:
    def __init__(self, playerName: str, score: int, date: datetime):
        self.playerName = playerName
        self.score = score
        self.date = date

def DbObjectToObject(obj):
    return ParticipationResult(obj[1], obj[2], obj[3])

class AnswerSummaryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AnswerSummary):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def ObjectToJson(obj):
    return json.dumps(obj.__dict__, cls = AnswerSummaryEncoder)

def GetAllScores():
    request = f"SELECT * FROM ParticipationResult ORDER BY score DESC"
    res = []
    for score in db_utils.callDb_multipleResults(request):
        res.append(DbObjectToObject(score))
    if len(res) == 0:
        return ''
    ret = json.dumps([obj.__dict__ for obj in res])
    return json.loads(ret)

def DeleteParticipations():
    request = "DELETE FROM ParticipationResult"
    db_utils.callDb_oneResult(request)
    return '', 204

def AddParticipation(json):
    playerName = json['playerName']
    nbQuestions = CountQuestions()
    if len(json['answers']) != nbQuestions:
        return '', 400
    rightAnswers = GetRightAnswers()
    summary = SetAnswerSummary(json['answers'], rightAnswers)
    score = 0
    for s in summary:
        if s.wasCorrect == 1:
            score += 1
    a = Answer(
        playerName,
        score,
        summary
    )
    scoreDate = datetime.datetime.now()
    request = f"INSERT INTO ParticipationResult (playerName, score, date) VALUES (\"{playerName}\",\"{score}\",\"{scoreDate}\")"
    db_utils.callDb_oneResult(request)
    return ObjectToJson(a), 200
