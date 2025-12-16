import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLineEdit,QPushButton,QLabel
import random
class Guess_number:
    def __init__(self):
       
        self.secret=random.randint(0,100)
       


    def guess(self,player):
            if player==self.secret:
                return 'correct'
            if self.secret<player:
                return 'high'
            elif self.secret>player:
                return 'low'

class GuessGameUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.game=Guess_number()

        self.setWindowTitle("Guess the Number")
        self.setGeometry(400,300,300,150)

        self.input=QLineEdit()
        self.input.setPlaceholderText("Enter number from (0 to 100)")

        self.button =QPushButton("Guess")
        self.result_label=QLabel("make a Guess")

        layout =QVBoxLayout()

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)


        self.setLayout(layout)

        self.button.clicked.connect(self.handle_guess)

    def handle_guess(self):
            try:
                value =int(self.input.text())
                result=self.game.guess(value)
                self.result_label.setText(result)
            except ValueError:
                self.result_label.setText("Enter valid number")

app = QApplication(sys.argv)
window =GuessGameUI()
window.show()
sys.exit(app.exec_())