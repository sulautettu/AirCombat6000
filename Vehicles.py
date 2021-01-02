from random import randint
class vehicle:


    def __init__(self, name = "Maverick", x = randint(40,1900) , y = randint(40,400) , pitch = randint(0,359),
                 imagePath = 'images/helicopter.png', thrust = 1):
        self.name = name
        self.x = x
        self.y = y
        self.pitch = pitch
        self.imagePath = imagePath
        self.thrust = thrust
        self.pitchRate = 0

