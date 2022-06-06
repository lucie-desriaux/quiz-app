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
	
	def DbObjectToObject(obj):
		return PossibleAnswer(obj[1], True if obj[2] == 1 else False)


def CheckCorrectAnswer(possibleAnswers):
	s = set([pa.text for pa in possibleAnswers])
	if len(s) != len(possibleAnswers):
		return False
	nbOfCorrectAnswers = 0
	for pa in possibleAnswers:
		if pa.isCorrect == 1:
			nbOfCorrectAnswers+=1
	if nbOfCorrectAnswers != 1:
		return False
	return True
		

def CreatePossibleAnswers(questionId, possibleAnswers):
	for pa in possibleAnswers:
		isCorrect = 1 if pa.isCorrect else 0
		request = f"INSERT INTO PossibleAnswer (text, isCorrect, questionId) VALUES (\"{pa.text}\",{isCorrect},{questionId})"
		db_utils.callDb_oneResult(request)
