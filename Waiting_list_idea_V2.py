import random

first_name = {"jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul", "ringo", "ally", "nicky", "cam",
              "ari", "trudie", "cal", "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake", "kim", "julio",
              "lorraine", "floyd", "janet", "lydia", "charles", "pedro", "bradley"}
last_name = {"barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller"}


def Name(first_name, last_name):
    first = random.sample(first_name, 1)[0]
    last = random.sample(last_name - {first}, 1)[0]
    return first + " " + last


OUT = []

i = 1000
while i > 0:
    name = Name(first_name, last_name)
    if name not in OUT:
        OUT.append(name)
        print(name)
    i -= 1

print(len(OUT), 'unique names generated.')
