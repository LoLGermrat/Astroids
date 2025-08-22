import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    
    Player.containers = (updateable_group, draw_group)

    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable_group.update(dt)

        screen.fill("black")
        for obj in draw_group:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()



