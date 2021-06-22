import time
from random import randint
import random


def time_counter(t):

    centre = {"London", "Birmingham", "Leeds", "Glasgow", "Aberdeen", "Manchester", "Edinburgh", "Newcastle",
              "Liverpool", "Cardiff", "Bristol", "Nottingham", "Sheffield", "Leicester", "York", "Portsmouth",
              "Cambridge",
              "Exeter", "Plymouth", "Norwich", "Oxford", "Aberystwyth", "Cardiff",
              "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "Torquay", "Coventry", "Blackpool",
              "Chester"}

    waiting_list = []
    identification = 1
    training_academies = {}
    while t != 0:
        years, months = divmod(t, 12)
        timer = '{:02d}:{:02d}'.format(years, months)
        print(timer, end="\r")
        time.sleep(1)
        new_people = randint(20, 30)
        if t % 2 == 0:
            random_centre = random.choice(list(centre))
            training_academies[random_centre] = 0
            centre.remove(random_centre)
        for i in range(0, new_people):
            waiting_list.append(identification)
            identification += 1
        print(new_people)
        print(waiting_list)
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

        print(training_academies)
        print(waiting_list)
        t -= 1
    print("The time simulation is over")


t = input("Enter the time in months for the programme to run: ")
time_counter(int(t))
