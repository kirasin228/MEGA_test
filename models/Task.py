class Task:
    def __init__(self, question, answer, level):
        self.question = question
        self.answer = answer
        self.level = level

    def __str__(self):
        s = f"{{'question': '{self.question}', 'answer': '{self.answer}', 'level': {self.level}}}"
        return s

# t = Task("революцио..ый", "революционный", 3)
# print(t)