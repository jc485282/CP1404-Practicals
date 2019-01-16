"""
Game - represents the state of game-play of our guessing game
"""

from random import randint
from kivy.app import App
from kivy.lang import Builder


class Game(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.secret = 0
        self.number_of_moves = 0
        self.set_secret()

    def build(self):
        self.title = "Game"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def set_secret(self):
        self.secret = randint(1, 10)

    def handle_new_game(self):
        self.number_of_moves = 0
        self.set_secret()

    def handle_guess(self):
        value = int(self.root.ids.guess_input.text)
        print(value,self.secret)
        if value > self.secret:
            self.root.ids.game_display.text = str("Try smaller")
        elif value < self.secret:
            self.root.ids.game_display.text = str("Try bigger")
        else:
            self.number_of_moves = -1
            self.set_secret()
            self.root.ids.game_display.text = str("Found it!")

    def add_move(self):
        self.number_of_moves += 1
        return self.number_of_moves

Game().run()
