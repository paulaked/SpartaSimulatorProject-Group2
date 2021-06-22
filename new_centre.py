import random
from dict_centres import centre

training_academies = {}


def new_centre():
    random_centre = random.choice(list(centre))
    training_academies[random_centre] = 0
    centre.remove(random_centre)
