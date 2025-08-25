import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        # sub-classes must override
        ...
    
    def update(self, dt):
        # sub-classes must override
        ...
    
    def collisions(self, second_asteroid):
        return (self.position.distance_to(second_asteroid.position) <= (self.radius + second_asteroid.radius))