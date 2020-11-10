from gesture import Gesture


class Spock(Gesture):
    def __init__(self):
        self.name = "Spock"
        self.can_beat_rock = True
        self.can_beat_paper = False
        self.can_beat_scissors = True
        self.can_beat_lizard = False
        self.can_beat_spock = False
