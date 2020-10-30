import sys
from PySide2 import QtCore, QtGui

#cria uma aplicação
app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()
win.resize(600,400)
win.setWindowTitle('Curso de Python3: Estrutura de dados e algoritmos')
win.show()

sys.exit(app.exec_())