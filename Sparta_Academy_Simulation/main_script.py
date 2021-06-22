import time
from random import randint
from new_centre import new_centre
from new_centre import training_academies
from into_academy import leave_waiting_list
from into_academy import waiting_list
from into_academy import full_centres
from Config_FIles.user_input import *

if number_of_months != 0:
    length_simulation = number_of_months
else:
    length_simulation = int(input("Enter the time in months for the programme to run: "))
identification = 1

while length_simulation != 0:
    years, months = divmod(length_simulation, 12)
    timer = '{:02d}:{:02d}'.format(years, months)
    time.sleep(0.5)
    new_people = randint(20, 30)
    if length_simulation % 2 == 0:
        new_centre()
    for each_person in range(0, new_people):
        waiting_list.append(identification)
        identification += 1
    print(new_people)
    print(waiting_list)
    leave_waiting_list()
    print(waiting_list)
    print(training_academies)
    length_simulation -= 1
trainees_at_each_centre = training_academies.values()
total_trainees = sum(trainees_at_each_centre)
print(f"The total number of open centres is {len(training_academies.keys())}.")
print(f"The total number of full centres is {len(full_centres)}.")
print(f"The total number of trainees currently in training is {total_trainees}.")
print(f"The total number of trainees on the waiting list is {len(waiting_list)}.")