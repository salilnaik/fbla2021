# fix quiz. it repeats the same question multiple times because it selects them each individually based on ratio so it always selects the one with the worst ratio








# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#########Documentation##########
# Main program of the software #
# Defines class Ui_MainWindow  #
# Connnects to database.py     #
# Creates instance of Database #
# Creates GUI and displays it  #
#
# Dependencies: database.py    #
#   Database class             #
################################


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from database import Database
import random
from time import sleep


class Ui_MainWindow(object):
    # Will Set up the home page and display it to the user
    def setup_home(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 335)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeText = QtWidgets.QLabel(self.centralwidget)
        self.welcomeText.setGeometry(QtCore.QRect(10, 10, 581, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.welcomeText.setFont(font)
        self.welcomeText.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.welcomeText.setWordWrap(True)
        self.welcomeText.setObjectName("welcomeText")
        self.beginButton = QtWidgets.QPushButton(self.centralwidget)
        self.beginButton.setGeometry(QtCore.QRect(20, 200, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.beginButton.setFont(font)
        self.beginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.beginButton.setAutoDefault(True)
        self.beginButton.setObjectName("beginButton")
        self.beginButton.clicked.connect(self.quiz)
        self.reportButton = QtWidgets.QPushButton(self.centralwidget)
        self.reportButton.setGeometry(QtCore.QRect(320, 200, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reportButton.setFont(font)
        self.reportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportButton.setObjectName("reportButton")
        self.reportButton.clicked.connect(self.report)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)

    # Helper function for PyQt5
    def setupUi(self, MainWindow):
        self.setup_home()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    # Will set up the reports page and display it to the user
    def setup_report(self):

        
        self.reportwidget = QtWidgets.QWidget(MainWindow)
        self.reportwidget.setObjectName("reportwidget")
        self.reportText = QtWidgets.QLabel(self.reportwidget)
        self.reportText.setGeometry(QtCore.QRect(5, 5, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reportText.setFont(font)
        self.reportText.setStyleSheet("color:blue;")
        self.reportText.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.reportText.setWordWrap(True)
        self.reportText.setObjectName("welcomeText")
        self.reportText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportText.mousePressEvent = self.back
        self.answers = QtWidgets.QCheckBox(self.reportwidget)
        self.answers.setObjectName("answers")
        self.answers.setGeometry(QtCore.QRect(904, 5, 131, 20))
        self.answers.toggled.connect(self.answer)
        
        self.print = QtWidgets.QPushButton(self.reportwidget)
        self.print.setGeometry(QtCore.QRect(1090, 5, 100, 30))
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        self.print.setFont(font1)
        self.print.clicked.connect(self.printa)
        
        self.beginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.beginButton.setObjectName("printButton")
        self.beginButton.clicked.connect(self.quiz)
        self.table = QtWidgets.QTreeView(self.reportwidget)
        self.table.setObjectName("table")
        self.table.setRootIsDecorated(False)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.addDataNoAnswers()
        self.table.setGeometry(QtCore.QRect(5, 40, 1190, 655))
        self.table.hide()


        
    # Will set up quiz page and display it to the user
    def setup_quiz(self):
        _translate = QtCore.QCoreApplication.translate
        self.quizwidget = QtWidgets.QWidget(MainWindow)
        self.quizwidget.setObjectName("quizwidget")
        self.quizText = QtWidgets.QLabel(self.quizwidget)
        self.quizText.setGeometry(QtCore.QRect(5, 5, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quizText.setFont(font)
        self.quizText.setStyleSheet("color:blue;")
        self.quizText.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.quizText.setWordWrap(True)
        self.quizText.setObjectName("quizWelcomeText")
        self.quizText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quizText.mousePressEvent = self.back

        
        self.check = QtWidgets.QPushButton(self.quizwidget)
        self.check.setGeometry(375, 440, 100, 35)
        self.check.setText(_translate("MainWindow", "Check Answer"))


        # Display question 1 (Multiple Choice)
        # Will roll back and display question 5 (Multiple Choice)
        if len(self.results) == 0 or len(self.results)>3:
            self.check.clicked.connect(self.checkans)
            self.mc1 = db.getmc()
            self.text1 = QtWidgets.QLabel(self.quizwidget)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.text1.setFont(font)
            self.text1.setWordWrap(True)
            self.text1.setGeometry(QtCore.QRect(5, 90, 470, 100))

            self.choices = [0, 0, 0, 0]
            self.index = random.randint(0,3)

            
            
            for x, i in enumerate(self.mc1[2:6]):
                self.choices[self.index-x] = QtWidgets.QRadioButton(self.quizwidget)
                self.choices[self.index-x].setText(_translate("MainWindow", i))
            for x, i in enumerate(self.choices):
                self.choices[x].setGeometry(QtCore.QRect(10, (200+40*x), 470, 50))

            
            
            
            self.text1.setText(_translate("MainWindow", self.mc1[1]))
        # Display question 2 (True or False)
        elif len(self.results) == 1:
            self.text1.hide()
            self.check.hide()
            for i in self.choices:
                i.hide()
            self.tf1, self.tf1ans = db.gettf()
            self.text2 = QtWidgets.QLabel(self.quizwidget)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.text2.setFont(font)
            self.text2.setWordWrap(True)
            self.text2.setGeometry(QtCore.QRect(5, 90, 470, 100))
            self.text2.setText(_translate("MainWindow", f'{self.tf1[1]}\n\nDoes "{self.tf1[2]}" make this sentence true?'))

            self.buttonbox = QtWidgets.QDialogButtonBox(self.quizwidget)
            self.buttonbox.setGeometry(QtCore.QRect(-240, 240, 470, 50))
            self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
            self.buttonbox.accepted.connect(self.checktf)
            self.buttonbox.rejected.connect(self.checktff)

        # Display question 3 (Fill in the Blank)
        elif len(self.results) == 2:
            self.fib1 = db.getfib()
            self.text3 = QtWidgets.QLabel(self.quizwidget)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.text3.setFont(font)
            self.text3.setWordWrap(True)
            self.text3.setGeometry(QtCore.QRect(5, 90, 470, 100))
            self.text3.setText(_translate("MainWindow", f'{self.fib1[1]}\n\nPlease enter your answer in the textbox below.'))
            self.line = QtWidgets.QLineEdit(self.quizwidget)
            self.line.setGeometry(QtCore.QRect(5, 240, 200, 25))

            self.check.clicked.connect(self.checkfib)
        # Display question 4 (Dropdown)
        elif len(self.results) == 3:
            self.dd1 = db.getmc()
            self.text4 = QtWidgets.QLabel(self.quizwidget)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.text4.setFont(font)
            self.text4.setWordWrap(True)
            self.text4.setGeometry(QtCore.QRect(5, 90, 470, 100))
            self.text4.setText(_translate("MainWindow", f'{self.dd1[1]}\n\nSelect the correct answer from the dropdown below.'))

            self.drop = QtWidgets.QComboBox(self.quizwidget)
            h = [2,3,4,5]
            random.shuffle(h)
            self.ddindex = h.index(2)
            for x, i in enumerate(h):
                self.drop.addItem(self.dd1[i])
            self.drop.setGeometry(QtCore.QRect(5,240,200,25))

            self.check.clicked.connect(self.checkdd)
            
            
        
        MainWindow.setCentralWidget(self.quizwidget)
        MainWindow.setWindowTitle(_translate("MainWindow", "FBLA Quiz ~ Quiz"))
        self.quizText.setText(_translate("MainWindow", "< Quiz"))
        MainWindow.resize(480, 480)

    def checkdd(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.results)==3:
            if self.drop.currentIndex() == self.ddindex:
                self.results.append(True)
                db.increment(self.dd1[0], True)
                self.text4.setText(_translate("MainWindow", f'{self.dd1[1]}\n\nSelect the correct answer from the dropdown below.\nCORRECT!!'))
            else:
                self.results.append(False)
                db.increment(self.dd1[0], False)
                self.text4.setText(_translate("MainWindow", f'{self.dd1[1]}\n\nSelect the correct answer from the dropdown below.\nINCORRECT!! The correct answer is {self.dd1[2]}'))

        self.check.setText(_translate("MainWindow", "Next Question"))
        self.check.clicked.connect(self.setup_quiz)

    def checkfib(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.results) == 2:
            if self.line.text().lower().strip() == self.fib1[2].lower().strip():
                self.results.append(True)
                db.increment(self.fib1[0], True)
                self.text3.setText(_translate("MainWindow", f'{self.fib1[1]}\n\nPlease enter your answer in the textbox below.\nCORRECT!!'))
            else:
                self.results.append(False)
                db.increment(self.fib1[0], False)
                self.text3.setText(_translate("MainWindow", f'{self.fib1[1]}\n\nPlease enter your answer in the textbox below.\nINCORRECT!! The correct answer is {self.fib1[2]}'))

        
        self.check.clicked.connect(self.setup_quiz)
        self.check.setText(_translate("MainWindow", "Next Question"))

    def checktf(self):
        _translate = QtCore.QCoreApplication.translate
        self.buttonbox.hide()
        if self.tf1ans:
            self.results.append(True)
            db.increment(self.tf1[0], True)
            self.text2.setText(_translate("MainWindow", f'{self.tf1[1]}\n\nDoes "{self.tf1[2]}" make this sentence true?\nCORRECT!!'))
        else:
            self.results.append(False)
            db.increment(self.tf1[0], False)
            self.text2.setText(_translate("MainWindow", f'{self.tf1[1]}\n\nDoes "{self.tf1[2]}" make this sentence true?\nINCORRECT!!'))
        
        self.check.setText(_translate("MainWindow", "Next Question"))
        self.check.clicked.connect(self.setup_quiz)
        self.check.show()
    def checktff(self):
        _translate = QtCore.QCoreApplication.translate
        if not self.tf1ans:
            self.results.append(True)
            db.increment(self.tf1[0], True)
            self.text2.setText(_translate("MainWindow", f'{self.tf1[1]}\n\nDoes "{self.tf1[2]}" make this sentence true?\nCORRECT!!'))
        else:
            self.results.append(False)
            db.increment(self.tf1[0], False)
            self.text2.setText(_translate("MainWindow", f'{self.tf1[1]}\n\nDoes "{self.tf1[2]}" make this sentence true?\nINCORRECT!!'))
        
        self.check.setText(_translate("MainWindow", "Next Question"))
        self.check.clicked.connect(self.setup_quiz)
        self.check.show()
        
    def checkans(self):
        _translate = QtCore.QCoreApplication.translate
        for x, choice in enumerate(self.choices):
            if choice.isChecked():
                if self.pastchecked == choice:
                    break
                else:
                    self.pastchecked = choice
                if x == self.index:
                    self.results.append(True)
                    db.increment(self.mc1[0], True)
                    self.text1.setText(_translate("MainWindow", f'{self.text1.text()}\nCORRECT!!'))
                else:
                    self.results.append(False)
                    db.increment(self.mc1[0], False)
                    self.text1.setText(_translate("MainWindow", f'{self.text1.text()}\nINCORRECT!!'))
                break
        wrongfont = QtGui.QFont()
        wrongfont.setStrikeOut(True)
        for x, i in enumerate(self.choices):
            if x != self.index:
                self.choices[x].setFont(wrongfont)
        if len(self.results) < 5:
            self.check.setText(_translate("MainWindow", "Next Question"))
            self.check.clicked.connect(self.setup_quiz)
        else:
            self.check.setText(_translate("MainWindow", "View Results"))
            self.check.clicked.connect(self.get_results)

    def get_results(self):
        _translate = QtCore.QCoreApplication.translate
        count = 0
        for result in self.results:
            if result:
                count+=1
        font = QtGui.QFont()
        font.setPointSize(40)
        self.text1.setGeometry(QtCore.QRect(5, 90, 470, 300))
        self.text1.setFont(font)
        self.text1.setText(_translate("MainWindow", f"Your score: {count}/5"))

        self.buttoon = QtWidgets.QPushButton(self.quizwidget)
        self.buttoon.setText(_translate("MainWindow", "Print"))
        self.buttoon.setGeometry(QtCore.QRect(420,5,50,100))
        for i in self.choices:
            i.hide()
        self.check.hide()
        
                

    def report(self):
        self.setup_report()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setCentralWidget(self.reportwidget)
        MainWindow.setWindowTitle(_translate("MainWindow", "FBLA Quiz ~ Report"))
        self.reportText.setText(_translate("MainWindow", "< Report"))
        self.answers.setText(_translate("MainWindow", "Show Answers"))
        self.print.setText(_translate("MainWindow", "Print"))
        self.table.show()
        MainWindow.resize(1200, 700)

        
##        dialog = QPrintDialog()
##        printer = dialog.printer()
##        print(0)
##        if dialog.exec_() == QtWidgets.QDialog.Accepted:
##
##            document = QtGui.QTextDocument()
##            print(9)
##            cursor = QtGui.QTextCursor(document)
##            print(0)
##            print(self.reportwidget.columnCount())
##            table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())
##            print(9)
##            for row in range(table.rows()):
##                for col in range(table.columns()):
##                    cursor.insertText(self.table.item(row, col).text())
##                    cursor.movePosition(QtGui.QTextCursor.NextCell)
##            document.print_(dialog.printer())

    def quiz(self):
        self.pastchecked = ""
        self.results = []
        self.setup_quiz()

    def back(self, event):
        _translate = QtCore.QCoreApplication.translate
        self.setup_home()
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle(_translate("MainWindow", "FBLA Quiz ~ Home"))
        MainWindow.resize(601, 335)

    def printa(self):
        dialog = QPrintDialog()
        printer = dialog.printer()
        printer.setOrientation(QPrinter.Landscape)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            
            font = QtGui.QFont()
            font.setPointSize(10)

            document = QtGui.QTextDocument()
            cursor = QtGui.QTextCursor(document)
            table = cursor.insertTable(self.model.rowCount()+1, self.model.columnCount())
            document.setDefaultFont(font)
            for col in range(table.columns()):
                cursor.insertText(ui.model.horizontalHeaderItem(col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
            for row in range(table.rows()-1):
                for col in range(table.columns()):
                    cursor.insertText(self.model.item(row, col).text())
                    cursor.movePosition(QtGui.QTextCursor.NextCell)
            document.print_(dialog.printer())
        

    def answer(self):
        checked = self.answers.isChecked()
        if checked:
            self.addData()
        else:
            self.addDataNoAnswers()
        
       
        
    def addData(self):
        self.model = QtGui.QStandardItemModel(0, 5, self.reportwidget)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Index")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Question")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Answer")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Correct")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Total")
        self.table.setModel(self.model)
        data = db.report()
        for x, entry in enumerate(data):
            self.model.insertRow(x)
            for y, value in enumerate(entry):
                self.model.setData(self.model.index(x, y), value)
        for i in range(5):
            self.table.resizeColumnToContents(i)

    def addDataNoAnswers(self):
        self.model = QtGui.QStandardItemModel(0, 4, self.reportwidget)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Index")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Question")        
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Correct")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Total")
        self.table.setModel(self.model)
        data = db.reportNoAnswers()
        for x, entry in enumerate(data):
            self.model.insertRow(x)
            for y, value in enumerate(entry):
                self.model.setData(self.model.index(x, y), value)
        for i in range(5):
            self.table.resizeColumnToContents(i)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FBLA Quiz ~ Home"))
        self.welcomeText.setText(_translate("MainWindow", "Hello! Welcome to the FBLA Quiz! Select the Begin button below to enter the quiz. Or if you have already taken the quiz, select the Report button below to view your question stats."))
        self.beginButton.setText(_translate("MainWindow", "Begin!"))
        self.reportButton.setText(_translate("MainWindow", "Report"))


if __name__ == "__main__":
    db = Database("questions.db")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
