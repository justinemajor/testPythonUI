from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from GUI.MainWindow import MainWindow
from tools.mainModel import MainModel
import sys
import ctypes
import os


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.setStyle("Fusion")
        self.mainWindow = MainWindow()
        self.mainWindow.setWindowTitle("test")
        self.mainWindow.show()

    
def main():
    # Makes the icon in the taskbar as well.
    appID = "test"  # arbitrary string
    if os.name == 'nt':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
    elif os.name == 'posix':
        pass
    app = App(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
