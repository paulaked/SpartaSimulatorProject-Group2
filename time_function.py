import time
from random import randint


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
    print(len(in_training))
    print("The time simulation is over")


t = input("Enter the time in months for the programme to run: ")


#To make sure that it runs until a valid number is given
while True:
    try:
        #ensures that value can be inted
        time_counter(int(t))
        break
    except ValueError:
        #gives a more clear message on what is a valid input
        print("Please enter a number in numeric digits e.g. 2 not two.")
        t = input("Enter the time in months for the programme to run: ")
