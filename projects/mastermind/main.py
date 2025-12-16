import sys

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton

class MastermidGUI(Qwidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        # sets up the layout
        def initUI(self):
            layout=QVBoxLayout()
        self.label=QLabel

        self.guess_input=QLineEdit()
        layout.addWidget(self.guess_input)

        self.submit_button= QPushButton("Submit")
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("mastermidn game")
        self.resize(300,200)

if __name__=='__main__':
    app =QApplication(sys.argv)
    gui=MastermidGUI()
    gui.show()
    sys.exit(ap.exec_())