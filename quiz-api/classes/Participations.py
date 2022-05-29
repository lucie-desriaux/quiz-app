import db_utils

class Participations():
	def __init__(self, playerName: str, answers: list):
		self.playerName = playerName
		self.answers = answers


    # def JsonToObject(json):
	# 	list = []
	# 	for obj in json:
	# 		list.append(PossibleAnswer(
	# 			obj['text'],
	# 			obj['isCorrect']
	# 		))
	# 	return list
	
	# def DbObjectToJson(obj):
	# 	return PossibleAnswer(obj[1], True if obj[2] == 1 else False)
