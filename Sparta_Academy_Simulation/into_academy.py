from random import randint
from new_centre import training_academies

waiting_list = []
full_centres = []


def leave_waiting_list():

    for random_centre in training_academies:
        into_training = randint(0, 20)
        print(into_training)
        for x in range(0, into_training):
            if training_academies[random_centre] >= 100:
                break
            if len(waiting_list) >= 1:
                waiting_list.pop(0)
                training_academies[random_centre] += 1
            if len(waiting_list) == 0:
                break
            if training_academies[random_centre] == 100:
                full_centres.append(training_academies[random_centre])
