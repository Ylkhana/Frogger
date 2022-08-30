from os import supports_fd
import pygame

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups) -> None:
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class LongSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups) -> None:
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
