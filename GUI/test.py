from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QApplication
from PyQt5 import uic
import os
import sys


testUiPath = os.path.dirname(os.path.realpath(__file__)) + '{0}testUi.ui'.format(os.sep)
Ui_testUi, QtBaseClass = uic.loadUiType(testUiPath)


class TestUi(QWidget, Ui_testUi):
    def __init__(self):
        super(TestUi, self).__init__()
        self.setupUi(self)
        self.connectButtons()
    
    def connectButtons(self):
        self.pub_acquisition.clicked.connect(self.acquisition)

    def acquisition(self):
        print('yessssir je suis wow!')
