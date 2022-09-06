from lib2to3.pgen2 import grammar
from selectors import EVENT_WRITE
import pygame, sys
from random import choice, randint, random
from settings import *
from player import Player
from car import Car
from sprite import *

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
obstacle_sprites = pygame.sprite.Group()
    
player = Player((2062,3274), all_sprites, obstacle_sprites)

# timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# sprite setup
for sprite_name, pos_list in SIMPLE_OBJECTS.items():
    surf = pygame.image.load(f'graphics/objects/simple/{sprite_name}.png').convert_alpha()
    for sprite_pos in pos_list:
        SimpleSprite(surf, sprite_pos, [all_sprites, obstacle_sprites])

for sprite_name, pos_list in LONG_OBJECTS.items():
    surf = pygame.image.load(f'graphics/objects/long/{sprite_name}.png').convert_alpha()
    for sprite_pos in pos_list:
        LongSprite(surf, sprite_pos, [all_sprites, obstacle_sprites])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == car_timer:
            random_pos = choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                adjusted_pos = (random_pos[0], random_pos[1] + randint(-8, 8))
                Car(adjusted_pos, [all_sprites, obstacle_sprites])
                pos_list.append(random_pos)
            if len(pos_list) > 5:
                del pos_list[0]


    dt = clock.tick(60) / 1000

    display_surface.fill((0,0,0))

    # Update
    all_sprites.update(dt)

    # Draw
    all_sprites.custom_draw()

    pygame.display.update()