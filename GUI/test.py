from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QApplication
from PyQt5 import uic
import os
import sys


testUiPath = os.path.dirname(os.path.realpath(__file__)) + '{0}testUi.ui'.format(os.sep)
Ui_testUi, QtBaseClass = uic.loadUiType(testUiPath)


class TestUi(QWidget, Ui_testUi):
    def __init__(self):
        super(TestUi, self).__init__()
        self.connectButtons()
    
    def connectButtons(self):
        self.pub_acquisition.clicked.connect(self.acquisition)

    def acquisition(self):
        print('yessssir je suis wow!')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")
        layout = QVBoxLayout()
        layout.addWidget(TestUi())
        widget = QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()