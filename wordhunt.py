import sys
import random
import string
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget

# list of valid words in English dictionary from https://github.com/dwyl/english-words

class WordHunt(QMainWindow):
    def __init__(self):
        super().__init__()

        with open("words_alpha.txt") as file:
            # list of valid words in English dictionary
            self.validWords = set(word.strip().lower() for word in file)
        # list of valid words that have already been entered
        self.enteredWords = []
        # list of LetterButtons that form the current word
        self.currentWord = []

        self.score = 0
        self.words = 0

        self.initialize_window()
        self.create_buttons()

    def initialize_window(self):
        self.window = QWidget(self)
        self.setCentralWidget(self.window)
        self.setGeometry(50, 50, 400, 600)
        self.setWindowTitle("Word Hunt Game")
        self.show()

    def create_buttons(self):
        row = 4
        col = 4
        # creating row x col sized grid of letter buttons
        self.grid = QGridLayout()
        for i in range(0, row):
            for j in range(0, col):
                button = LetterButton(i, j, row, col, self.currentWord)
                self.grid.addWidget(button, i, j)
        # TEMPORARY: creating enter button to submit a word
        self.enterButton = QPushButton(self.window)
        self.enterButton.setText("Enter")
        self.enterButton.clicked.connect(self.enter)
        self.grid.addWidget(self.enterButton, row + 1, 0)
        self.window.setLayout(self.grid)
        self.statusBar()

    def get_word(self):
        word = ""
        for button in self.currentWord:
            word += button.get_letter()
        return word

    # TODO: trigger this method by release of mouse button
    def enter(self):
        word = self.get_word()
        print("new potential word is:", word)
        if (word not in self.enteredWords and len(word) >= 3 and word in self.validWords):
            self.enteredWords.append(word)
            print(self.enteredWords)
        self.currentWord.clear()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Return:
            self.enter()

class LetterButton(QPushButton):
    def __init__(self, x, y, row, col, list):
        super().__init__()
        self.name = str(col*x + y)
        self.letter = random.choice(string.ascii_lowercase)
        self.setText(self.letter)
        self.clicked.connect(self.button_clicked)
        self.list = list
        self.x = x
        self.y = y
    
    def button_clicked(self):
        if (not self.list):
            self.add_to_list()
            print(self.letter)
        else:
            if (self not in self.list):
                prevButton = self.list[-1]
                if (self.is_adjacent(prevButton)):
                    self.add_to_list()
                    print(self.letter)

    def get_letter(self):
        return self.letter
    
    def is_adjacent(self, button):
        return abs(button.x - self.x) <= 1 and abs(button.y - self.y) <= 1
    
    def add_to_list(self):
        self.list.append(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wordHunt = WordHunt()
    sys.exit(app.exec_())