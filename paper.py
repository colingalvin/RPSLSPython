from gesture import Gesture


class Paper(Gesture):
    def __init__(self):
        self.name = "Paper"
        self.can_beat_rock = True
        self.can_beat_paper = False
        self.can_beat_scissors = False
        self.can_beat_lizard = False
        self.can_beat_spock = True
