import random
from dict_centres import centre

training_academies = {}


def new_centre():

    try:
        random_centre = random.choice(list(centre))
        training_academies[random_centre] = 0
        centre.remove(random_centre)
    except IndexError:
        pass
    except KeyError:
        pass