from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random
from logger import log_event

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
        log_event("asteroid_split")
        rangle = random.uniform(20, 50)
        spawn1 = self.velocity.rotate(rangle)
        spawn2 = self.velocity.rotate(-rangle)
        
        nradius = self.radius - ASTEROID_MIN_RADIUS
        nasteroid1 = Asteroid(self.position.x, self.position.y, nradius)
        nasteroid2 = Asteroid(self.position.x, self.position.y, nradius)
        nasteroid1.velocity = spawn1 * 1.2
        nasteroid2.velocity = spawn2 * 1.2

    
