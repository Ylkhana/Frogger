import pygame, sys
from settings import *
from player import Player

# Basic init
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player((0,0), all_sprites)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60) / 1000

    display_surface.fill((0,0,0))

    # Update
    all_sprites.update(dt)

    # Draw
    all_sprites.draw(display_surface)

    pygame.display.update()