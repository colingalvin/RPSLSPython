from gesture import Gesture


class Scissors(Gesture):
    def __init__(self):
        self.name = "Scissors"
        self.can_beat_rock = False
        self.can_beat_paper = True
        self.can_beat_scissors = False
        self.can_beat_lizard = True
        self.can_beat_spock = False
