
class AnswerSummary():
 	def __init__(self, correctAnswerPosition: int, wasCorrect: bool):
         self.correctAnswerPosition = correctAnswerPosition
         self.wasCorrect = wasCorrect

def SetAnswerSummary(answers, correctAnswers):
    res = []
    for i in range(len(correctAnswers)):
        res.append(AnswerSummary(correctAnswers[i], correctAnswers[i] == answers[i]))
    return res
