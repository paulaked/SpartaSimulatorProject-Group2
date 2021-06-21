import time
from random import randint
import random

centre = {"London", "Birmingham", "Leeds", "Glasgow", "Aberdeen", "Manchester", "Edinburgh", "Newcastle",
          "Liverpool", "Cardiff", "Bristol", "Nottingham", "Sheffield", "Leicester", "York", "Portsmouth", "Cambridge",
          "Exeter", "Plymouth", "Norwich", "Oxford", }
random_centre = random.choice(list(centre))


def time_counter(t):
    waiting_list = []
    identification = 1
    in_training = []
    while t != 0:
        years, months = divmod(t, 12)
        timer = '{:02d}:{:02d}'.format(years, months)
        print(timer, end="\r")
        print(t)
        time.sleep(1)
        x = 0
        new_people = randint(20, 30)
        attend_centre = randint(0, 20)
        for i in range(0, new_people):
            waiting_list.append(identification)
            identification += 1
        print(new_people)
        for x in range(0, attend_centre):
            into_training = waiting_list.pop(0)
            in_training.append(into_training)
        print(attend_centre)
        print(waiting_list)
        print(in_training)
        t -= 1
    print("The time simulation is over")


t = input("Enter the time in months for the programme to run: ")
time_counter(int(t))
