from new_centre import new_centre
from into_academy import leave_waiting_list
import time
from random import randint
from into_academy import waiting_list
from new_centre import training_academies


t = int(input("Enter the time in months for the programme to run: "))
identification = 1
while t != 0:
    years, months = divmod(t, 12)
    timer = '{:02d}:{:02d}'.format(years, months)
    print(timer, end="\r")
    time.sleep(1)
    new_people = randint(20, 30)
    if t % 2 == 0:
        new_centre()
    for i in range(0, new_people):
        waiting_list.append(identification)
        identification += 1
    print("New trainees this month:", new_people)
    print("Current waiting list:", waiting_list)
    leave_waiting_list()
    print("Training academy(s):", training_academies)
    print("Current waiting list:", waiting_list)
    t -= 1
print("The simulation is over.")