from gesture import Gesture


class Lizard(Gesture):
    def __init__(self):
        self.name = "Lizard"
        self.can_beat_rock = False
        self.can_beat_paper = True
        self.can_beat_scissors = False
        self.can_beat_lizard = False
        self.can_beat_spock = True
