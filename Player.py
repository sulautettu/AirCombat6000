from random import randint
import math

class player (object):


    def __init__(self, name="Maverick", x=100, y=100, pitch=0,
                 imagePath='images/helicopter.png', thrust=1):
        self.name = name
        self.x = x
        self.y = y
        self.pitch = pitch
        self.imagePath = imagePath
        self.thrust = thrust
        self.pitchRate = 0




    def update(self):
        self.pitch += self.pitchRate
        self.x -= self.thrust * math.cos(math.radians(self.pitch))
        self.y += self.thrust * math.sin(math.radians(self.pitch))

        if self.x < 0 and self.y < 500:
            self.x = 1919
            self.y += 500

        if self.x < 0 and self.y > 500:
            self.x = 1919
            self.y -= 500

        if self.x > 1920 and self.y > 500:
            self.x = 0
            self.y -= 500

        if self.x > 1920 and self.y < 500:
            self.x = 0
            self.y += 500

