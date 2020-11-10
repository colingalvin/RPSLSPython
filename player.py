from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock
import random


class Player:
    def __init__(self):
        self.name = ""
        self.gestures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]
        self.score = 0

    def choose_gesture(self):
        chosen_gesture = self.gestures[random.randint(1, 5)]
        return chosen_gesture
