import random

centre = {"London", "Birmingham", "Leeds", "Glasgow", "Aberdeen", "Manchester", "Edinburgh", "Newcastle",
          "Liverpool", "Cardiff", "Bristol", "Nottingham", "Sheffield", "Leicester", "York", "Portsmouth", "Cambridge",
          "Exeter", "Plymouth", "Norwich", "Oxford", }

random_centre = random.choice(list(centre))
print(random_centre)
