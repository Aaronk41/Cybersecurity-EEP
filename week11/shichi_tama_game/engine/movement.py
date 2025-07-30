import pygame

class Player:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.speed = 2
        self.sprites = sprites
        self.current_sprite = self.sprites["front"]
        self.rect = self.current_sprite.get_rect(topleft=(self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            if "left" in self.sprites:
                self.current_sprite = self.sprites["left"]
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            if "right" in self.sprites:
                self.current_sprite = self.sprites["right"]
        elif keys[pygame.K_UP]:
            self.y -= self.speed
            self.current_sprite = self.sprites["back"]
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.current_sprite = self.sprites["front"]

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.current_sprite, (self.x, self.y))
