import random

fname = {"jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul", "ringo", "ally", "nicky", "cam",
         "ari", "trudie", "cal", "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake", "kim", "julio",
         "lorraine", "floyd", "janet", "lydia", "charles", "pedro", "bradley"}
lname = {"barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller"}


def Name(f_name, l_name):
    first = random.sample(f_name, 1)[0]
    last = random.sample(l_name - {first}, 1)[0]
    return first + " " + last


OUT = []

i = 1000
while i > 0:
    name = Name(fname, lname)
    if name not in OUT:
        OUT.append(name)
        print(name)
    i -= 1

print(len(OUT), 'unique names generated.')
