from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import * 

from UI_MainWindow import Ui_MainWindow
from solver import Solver

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFocus()
        self.installEventFilter(self)
        self.solver = Solver()
        

    def keyPressEvent(self, e):
        if self.solver.capture(e.key()):
            self.buffer.setText(self.solver.buffer)
            self.text.setText(self.text.toPlainText() + self.solver.newText)
        else:
            self.text.setReadOnly(False)
            self.text.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
            self.text.keyPressEvent(e)
            self.text.setReadOnly(True)
        self.setFocus()
        self.updateWaiting()


    def updateWaiting(self):
        self.solver.updateWaitingList()
        self.waiting.setText("")
        WL = self.solver.getWaitingList()
        for i in range(len(WL)):
            self.waiting.append('%d: %s'%(i+1, WL[i]))


    def eventFilter(self, obj, event):
        if (event == QEvent.KeyPress):
            return True
        return super(MainWindow, self).eventFilter(obj, event)

