import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QDialog
from PyQt5.QtGui import QIcon,QImage,QPixmap,QPalette,QBrush
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication,QRect,QSize
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QVBoxLayout,  QLabel, QFileDialog, QToolButton

import os
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Распознание изображений'
        self.left = 10
        self.top = 10
        self.width = 480
        self.height = 240
        self.initUI()

        self.pathimage = os.path.expanduser('images')
        self.outpath   = os.path.expanduser('images/out')



    def recognition(self):
            from test_yolo import _main
            _main(self.pathimage,self.outpath)

    def createimage(self):
            self.imgshow = Dialog()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        oImage = QImage("logo.jpg")
        sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        detectionsMenu = mainMenu.addMenu('Detections')
        runMenu = mainMenu.addMenu('Run')


        self.setStyleSheet("""QMenuBar {
         background-color:white;
        }

     QMenuBar::item {
         background: white;
     }""")

        selectFolder = QAction(QIcon('exit24.png'),'select folder input',self)
        selectFolder.setShortcut('Ctrl+F')
        selectFolder.setStatusTip('select folder input')
        selectFolder.triggered.connect(self.retranslateUi)

        selectout = QAction(QIcon('exit24.png'),'set folder out',self)
        #selectFolder.setShortcut('Ctrl+F')
        selectout.setStatusTip('set folder out')
        selectout.triggered.connect(self.setoutpath)

        runRecognition = QAction(QIcon('exit24.png'),'run recognition',self)
        runRecognition.setShortcut('Ctrl+R')
        runRecognition.setStatusTip('run recognition')
        runRecognition.triggered.connect(self.recognition)

        createImage = QAction(QIcon('exit24.png'),'create image',self)
        createImage.setShortcut('Ctrl+E')
        createImage.setStatusTip('create image')
        createImage.triggered.connect(self.createimage)

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        fileMenu.addAction(exitButton)
        detectionsMenu.addAction(selectFolder)
        runMenu.addAction(runRecognition)
        detectionsMenu.addAction(createImage)
        detectionsMenu.addAction(selectout)
        self.show()

    def setoutpath(self):
       self.outpath = str(QFileDialog.getExistingDirectory())
       #print(self.pathimage)

    def retranslateUi(self):
       self.pathimage = str(QFileDialog.getExistingDirectory())
       #print(self.pathimage)



class Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QVBoxLayout()

        self.setLayout(layout)
        self.showImage()
        self.show()

    def capture(self):
        import numpy as np
        import cv2

        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA
                            )
        cv2.imwrite(os.path.expanduser('images/image.jpeg'), gray)

    def showImage(self):
        self.capture()
        filename = os.path.expanduser('images/image.jpeg')
        image = QImage(filename)

        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

        layout = self.layout()
        layout.addWidget(self.imageLabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())