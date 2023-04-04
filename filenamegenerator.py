import random 
import constants as c


class Random:
    def generate(self):
        randomNumber = random.randint(2,4)
        name = ''
        for x in range(randomNumber):
            randomCap = random.choice(c.CAPS)
            randomLow = random.choice(c.LOW)
            name = name + randomCap + randomLow
        return name