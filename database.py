
#########Documentation##########################
# Defines Database class                       #
# Defines methods to interact with database    #
# Only public method getquiz() should be used #
################################################ 


import sqlite3
import random

class Database:
    def __init__(self, name):
        self.name = name
        self.db = sqlite3.connect(self.name)
    def run(self, query):
        temp = self.db.execute(query)
        return temp.fetchone()
    def runall(self, query):
        temp = self.db.execute(query)
        return temp.fetchall()
    def getlength(self):
        temp = self.runall("select * from questions")
        return len(temp)
    def commit(self):
        self.db.commit()
    def getquiz(self, length):
        """takes int length
        
        This method will query the database and return a tuple of 2 lists: the first one contains the questions, the second contains the question type.
        Each list will be the length of the parameter passed into the method.
        """
        questions = self.db.execute("select * from questions where fib!=1 order by ratio asc, random();")
        fibquestions = self.db.execute("select * from questions where fib==1 order by ratio asc, random();")
        
        out = []
        outtype = []
        for i in range(length):
            qtype = random.randint(1,4)
            outtype.append(qtype)
            # mc
            if qtype==1:
                try:
                    out.append(questions.fetchone()[:6])
                except:
                    out.append(fibquestions.fetchone()[:6])
                    
            # tf
            if qtype==2:
                if random.randint(0,1):
                    try:
                        out.append((questions.fetchone()[:3], True))
                    except:
                        out.append((fibquestions.fetchone()[:3], True))
                        
                else:
                    randfalse = random.randint(3, 5)
                    try:
                        tempq = questions.fetchone()
                    except:
                        tempq = fibquestions.fetchone()
                    out.append((tempq[:2] + (tempq[randfalse],), False))
            # fib
            if qtype==3:
                out.append(fibquestions.fetchone()[:3])
            # dd
            if qtype==4:
                try:
                    out.append(questions.fetchone()[:6])
                except:
                    out.append(fibquestions.fetchone()[:6])
                    
        return out, outtype        

        
    def getmc(self):
        out = self.run("select id, question, answer, wrong1, wrong2, wrong3 from questions order by ratio asc, random();")
        return out
    def gettf(self):
        rand = random.randint(0,1)
        if rand:
            out = self.run("select id, question, answer from questions order by ratio asc, random();")
        else:
            rand1 = random.randint(1,3)
            out = self.run(f"select id, question, wrong{rand1} from questions order by ratio asc, random();")
        return out, bool(rand)
    def getfib(self):
        out = self.run("select id, question, answer from questions where fib==1 order by ratio asc, random();")
        return out
    def report(self):
        out = self.runall("select id, question, answer, right, total from questions")
        return out
    def reportNoAnswers(self):
        out = self.runall("select id, question, right, total from questions")
        return out
    def increment(self, id_, correct):
        right, total = self.run(f"select right, total from questions where id=={id_}")
        self.run(f"update questions set total = {total+1} where id=={id_}")
        total+=1
        if correct:
            self.run(f"update questions set right = {right+1} where id=={id_}")
            right+=1
        self.run(f"update questions set ratio = {right/total} where id=={id_}")
        self.db.commit()
if __name__ == '__main__':
    db = Database("questions.db")
