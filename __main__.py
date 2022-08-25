from lib2to3.pgen2 import grammar
import pygame, sys
from settings import *
from player import Player
from car import Car

class AllSprites(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load('graphics/main/map.png').convert()
        self.fg = pygame.image.load('graphics/main/overlay.png').convert_alpha()

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        display_surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, -self.offset)

# Basic init
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

all_sprites = AllSprites()
    
player = Player((600,400), all_sprites)
car = Car((600,200), all_sprites)

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
    all_sprites.custom_draw()

    pygame.display.update()