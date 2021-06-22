import time
from random import randint
from new_centre import new_centre
from new_centre import training_academies
from into_academy import leave_waiting_list
from into_academy import waiting_list
from into_academy import full_centres

while True:
    # ensures that value can be inted
    try:
        t = int(input("Enter the time in months for the programme to run: "))
        if t > 0:
            break
        else:
            print("The number must be greater than 0")

    except ValueError:
        # gives a more clear message on what is a valid input
        print("Please enter a number in numeric digits e.g. 2 not two.")
        t = input("Enter the time in months for the programme to run: ")

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
    print(new_people)
    print(waiting_list)
    leave_waiting_list()
    print(training_academies)
    print(waiting_list)
    t -= 1

trainees_at_each_centre = training_academies.values()
total_trainees = sum(trainees_at_each_centre)
print("The simulation is over.")
print(f"The total number of open centres is {len(training_academies.keys())}")
print(f"The total number of full centres is {len(full_centres)}")
print(f"The total number of trainees currently in training is {total_trainees}")
print(f"The total number of trainees on the waiting list is {len(waiting_list)}")