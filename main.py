from human import Human
from ai import AI


def compare_gestures(gesture1, gesture2):
    if gesture1.name == gesture2.name:
        return "tie"
    elif gesture1.name == "Rock":
        if gesture2.can_beat_rock:
            return "lose"
    elif gesture1.name == "Paper":
        if gesture2.can_beat_paper:
            return "lose"
    elif gesture1.name == "Scissors":
        if gesture2.can_beat_scissors:
            return "lose"
    elif gesture1.name == "Lizard":
        if gesture2.can_beat_lizard:
            return "lose"
    elif gesture1.name == "Spock":
        if gesture2.can_beat_spock:
            return "lose"
    return "win"


def display_result(gesture_result):
    if gesture_result == "tie":
        print("Tie round!")
    elif gesture_result == "lose":
        print(f"{ai.name} wins this round!")
        ai.score += 1
    else:
        print(f"{colin.name} wins this round!")
        colin.score += 1


if __name__ == '__main__':
    colin = Human("Colin")
    ai = AI()

    while colin.score < 2 and ai.score < 2:
        print(f"{colin.name}: {colin.score} // {ai.name}: {ai.score}")
        colin_gesture = colin.choose_gesture()
        ai_gesture = ai.choose_gesture()
        print(f"{colin.name} chose {colin_gesture.name}, {ai.name} chose {ai_gesture.name}")
        result = compare_gestures(colin_gesture, ai_gesture)
        display_result(result)
    else:
        print(f"Final results: {colin.name}: {colin.score}, {ai.name}: {ai.score}")
