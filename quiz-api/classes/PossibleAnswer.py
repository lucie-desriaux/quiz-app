import db_utils

class PossibleAnswer():
	def __init__(self, text: str, isCorrect: bool):
		self.text = text
		self.isCorrect = isCorrect

	def JsonToObject(json):
		list = []
		for obj in json:
			list.append(PossibleAnswer(
				obj['text'],
				obj['isCorrect']
			))
		return list
	
	def DbObjectToJson(obj):
		return PossibleAnswer(obj[1], True if obj[2] == 1 else False)


def CheckCorrectAnswer(possibleAnswers):
	counter = 0
	for pa in possibleAnswers:
		if pa.isCorrect == 1:
			counter+=1
	return True if counter == 1 else False
		

def CreatePossibleAnswers(questionId, possibleAnswers):
	for pa in possibleAnswers:
		isCorrect = 1 if pa.isCorrect else 0
		request = f"INSERT INTO PossibleAnswer (text, isCorrect, questionId) VALUES (\"{pa.text}\",{isCorrect},{questionId})"
		db_utils.callDb_oneResult(request)


