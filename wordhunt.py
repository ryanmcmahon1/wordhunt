from tkinter import *
import random
import string

class WordHunt:
    def __init__(self, window):
        self.window = window
        window.title("Word Hunt")

        self.wordlist = []

        self.current_word = CurrentWord(window)
        self.score = Score(window)

        self.letter1_button = LetterButton(window, self.current_word, "A", 1, 0)
        self.letter2_button = LetterButton(window, self.current_word, "B", 1, 1)
        self.letter3_button = LetterButton(window, self.current_word, "C", 2, 0)
        self.letter4_button = LetterButton(window, self.current_word, "D", 2, 1)

        self.enter_button = ActionButton(window, "enter", 3, self.enter)
        self.undo_button = ActionButton(window, "undo", 4, self.undo)
        self.clear_button = ActionButton(window, "clear", 5, self.clear)

        self.exit_button = ActionButton(window, "exit", 6, window.quit)
    
    def clear(self):
        self.current_word.clear()
    
    def enter(self):
        if (len(self.word()) >= 3 and self.word() not in self.wordlist):
            self.wordlist.append(self.word())
            self.current_word.clear()
            print(self.wordlist)
    
    def undo(self):
        self.current_word.undo()
    
    def word(self):
        return self.current_word.get_word()

class LetterButton:
    def __init__(self, window, label, letter, row, column):
        self.button = Button(window, text = letter, command = self.letter_button_click)
        self.button.grid(row = row, column = column)
        self.letter = letter
        self.label = label
    
    def letter_button_click(self):
        self.label.update_word(self.get_letter())

    def get_button(self):
        return self.button

    def get_letter(self):
        return self.letter

class ActionButton:
    def __init__(self, window, text, row, command):
        self.button = Button(window, text = text, command = command)
        self.button.grid(row = row, columnspan = 2, sticky = W+E)

# class Score:
#     def __init__(self, window):
#         self.score = 0
#         self.label = Label(window, text = self.score)
#         self.label.grid(columnspan=3, sticky=W+E)
    
#     def get_score(self):
#         return self.score

class CurrentWord:
    def __init__(self, window):
        self.word = ""
        self.label = Label(window, text = self.word)
        self.label.grid(columnspan=3, sticky=W+E)
    
    def get_word(self):
        return self.word
    
    def update_word(self, letter):
        self.word = self.word + letter
        self.update_label()
    
    def clear(self):
        self.word = ""
        self.update_label()
    
    def undo(self):
        self.word = self.word[:-1]
        self.update_label()
    
    def update_label(self):
        self.label.configure(text = self.word)

    

# using Tkinter and above classes to create the game board
root = Tk()
game = WordHunt(root)
root.mainloop()