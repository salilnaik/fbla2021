##
##from database import Database
##class Quiz:
##    def __init__(self):
##        self.db = Database("questions.db")
##        self.getQuiz()
##        while len([self.mc1, self.mc2, self.tf, self.fib, self.dd]) > len(set([self.mc1, self.mc2, self.tf, self.fib, self.dd])):
##            self.getQuiz()
##            print("j")
##    def getQuiz(self):
##        self.mc1 = self.db.getmc()
##        self.tf = self.db.gettf()
##        self.fib = self.db.getfib()
##        self.dd = self.db.getmc()
##        self.mc2 = self.db.getmc()
##q = Quiz()


from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.table = QtWidgets.QTableWidget(200, 5, self)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QtWidgets.QTableWidgetItem('(%d, %d)' % (row, col))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row, col, item)
        self.table.setHorizontalHeaderLabels(
            'SKU #|NAME|DESCRIPTION|QUANTITY|PRICE'.split('|'))
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        table = cursor.insertTable(
            self.table.rowCount(), self.table.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.table.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
