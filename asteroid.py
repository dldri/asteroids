import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        self.__split_angle__ = random.uniform(20, 50)
        self.__new_vector1__ = self.velocity.rotate(self.__split_angle__)
        self.__new_vector2__ = self.velocity.rotate(-self.__split_angle__)
        self.__new_radius__ = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position.x, self.position.y, self.__new_radius__)
        split2 = Asteroid(self.position.x, self.position.y, self.__new_radius__)

        split1.velocity = self.__new_vector1__ * 1.2
        split2.velocity = self.__new_vector2__ * 1.2
