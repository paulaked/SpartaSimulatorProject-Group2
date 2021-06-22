import random
from Config_Files.centres_config import centre_config

training_academies = {}


def new_centre():

    centre = centre_config
    random_centre = random.choice(list(centre))
    training_academies[random_centre] = 0
    centre.remove(random_centre)
