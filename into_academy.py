from random import randint


def leave_waiting_list():
    training_academies = {}
    waiting_list = []
    for random_centre in training_academies:
        into_training = randint(0, 20)
        for x in range(0, into_training):
            if training_academies[random_centre] >= 100:
                print(f"{random_centre} has reached full capacity!")
                break
            if len(waiting_list) >= 1:
                waiting_list.pop(0)
                training_academies[random_centre] += 1
            if len(waiting_list) == 0:
                break