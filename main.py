from database import Database

class Quiz:
    def __init__(self):
        self.db = Database("questions.db")
        self.getQuiz()
        while len([self.mc1, self.mc2, self.tf, self.fib, self.dd]) > len(set([self.mc1, self.mc2, self.tf, self.fib, self.dd])):
            self.getQuiz()
            print("j")
    def getQuiz(self):
        self.mc1 = self.db.getmc()
        self.tf = self.db.gettf()
        self.fib = self.db.getfib()
        self.dd = self.db.getmc()
        self.mc2 = self.db.getmc()
q = Quiz()
