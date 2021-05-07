import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog, QLabel, QDial
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Load new image
        self.setGeometry(700, 400, 950, 450)
        self.setWindowTitle('Load new image')

        # Button 1: Image
        self.bt1 = QPushButton('Select file', self)
        self.bt1.move(30, 70)
        self.bt1.clicked.connect(self.openfile)

        self.lab1 = QLabel('Image: ', self)
        self.lab1.setGeometry(30, 25, 80, 40)

        # Button 2: Label
        self.bt2 = QPushButton('Select file', self)
        self.bt2.move(30, 190)
        self.bt2.clicked.connect(self.openfile)

        self.lab2 = QLabel('Label: ', self)
        self.lab2.setGeometry(30, 145, 80, 40)

        # Button 3: Pointing file
        self.bt3 = QPushButton('Select file', self)
        self.bt3.move(30, 310)
        self.bt3.clicked.connect(self.openfile)

        self.lab3 = QLabel('Label: ', self)
        self.lab3.setGeometry(30, 265, 80, 40)

        # LOAD
        load = QPushButton('LOAD', self)
        # load.clicked.connect(QCoreApplication.instance().quit)
        # load.resize(70, 30)
        load.move(360, 370)

        # CLOSE
        close = QPushButton('CLOSE', self)
        close.clicked.connect(QCoreApplication.instance().quit)
        # close.resize(70, 30)
        close.move(500, 370)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', 'Image files (*.img)')
        '''if frame[0]:
            with open(fname[0], 'r', encoding='', errors='ignore') as f:
                self.'''

    def warning(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Unexpected error in 'caviar_image_load_gui_event':\n")
        # msgBox.setText("Attempt to call undefined procedure: ''.")
        ok = msgBox.addButton('OK', QMessageBox.AcceptRole)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())

