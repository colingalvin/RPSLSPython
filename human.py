from player import Player


class Human(Player):
    def __init__(self, name):
        Player.__init__(self)
        self.name = name

    def choose_gesture(self):
        i = 0
        for gesture in self.gestures:
            print(f"Enter {i} to choose {gesture.name}")
            i += 1
        chosen_gesture = self.gestures[int(input())]
        return chosen_gesture
