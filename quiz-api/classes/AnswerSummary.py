
class AnswerSummary():
 	def __init__(self, correctAnswerPosition: int, wasCorrect: bool):
         self.correctAnswerPosition = correctAnswerPosition
         self.wasCorrect = wasCorrect

def SetAnswerSummary(answers, correctAnswers):
    res = []
    isCorrect = 0
    for i in range(len(correctAnswers)):
        for j in range(len(correctAnswers[i])):
            if correctAnswers[i][j] == answers[i]:
                isCorrect = 1
                break
        param = correctAnswers[i][0] if len(correctAnswers[i]) == 1 else correctAnswers[i]
        res.append(AnswerSummary(param, isCorrect))
        isCorrect = 0
    return res
