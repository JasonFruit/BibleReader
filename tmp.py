import sys
from PySide.QtGui import QApplication, QMainWindow, QWidget, QPushButton
from PySide.QtCore import *

windows = []

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


class JanelaLogin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        btn = QPushButton("Test", self)
        btn.move(5, 5)
        btn.clicked.connect(self.onclick)

    def onclick(self):
        windows[1].show()
        #windows[0].hide()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    locale = QLocale.system().name()
    qtTranslator = QTranslator()
    if qtTranslator.load("tl_" + locale):
        app.installTranslator(qtTranslator)
    janelaLogin = JanelaLogin()
    janelaPrincipal = JanelaPrincipal()
    windows.append(janelaLogin)
    windows.append(janelaPrincipal)
    windows[0].show()
    sys.exit(app.exec_())
