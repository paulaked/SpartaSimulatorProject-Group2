identification = 1

waiting_list = 40

month_intake = 14

people = []

for i in range(0, waiting_list):
    people.append(identification)
    identification += 1

print(people)

for x in range(0, month_intake):
    person = people.pop(0)
    print(person)

print(people)
