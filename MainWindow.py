from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from GUI.test import TestUi


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