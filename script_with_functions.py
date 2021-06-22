from new_centre import new_centre
from into_academy import leave_waiting_list
import time
from random import randint

t = int(input("Enter the time in months for the programme to run: "))

waiting_list = []
identification = 1
training_academies = {}
while t != 0:
    years, months = divmod(t, 12)
    timer = '{:02d}:{:02d}'.format(years, months)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
    new_people = randint(20, 30)
    if t % 2 == 0:
        new_centre()
    for i in range(0, new_people):
        waiting_list.append(identification)
        identification += 1
    print(new_people)
    print(waiting_list)
    leave_waiting_list()
    print(training_academies)
    print(waiting_list)
print("The simulation is over.")



