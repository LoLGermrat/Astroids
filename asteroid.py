from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen): 
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        return self.position
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rangle = random.uniform(20, 50)
        spawn1 = self.velocity.rotate(rangle)
        spawn2 = self.velocity.rotate(-rangle)
        
        self.radius -= ASTEROID_MIN_RADIUS

    
