from gesture import Gesture


class Rock(Gesture):
    def __init__(self):
        self.name = "Rock"
        self.can_beat_rock = False
        self.can_beat_paper = False
        self.can_beat_scissors = True
        self.can_beat_lizard = True
        self.can_beat_spock = False
