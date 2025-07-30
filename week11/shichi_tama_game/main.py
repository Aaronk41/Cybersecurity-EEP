import pygame
import sys
import json
from engine.movement import Player
from engine.dialogue import DialogueManager
from engine.orb_logic import OrbManager

pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shichi Tama")
clock = pygame.time.Clock()

# Load player direction sprites (front and back only)
front_img = pygame.image.load("assets/sprites/player_front.png").convert_alpha()
back_img = pygame.image.load("assets/sprites/player_back.png").convert_alpha()

# Scale sprites to 96x96
front_img = pygame.transform.scale(front_img, (96, 96))
back_img = pygame.transform.scale(back_img, (96, 96))

# Sprite dictionary
player_sprites = {
    "front": front_img,
    "back": back_img
}

# Load other game assets
orb_img = pygame.image.load("assets/sprites/orb_purple.png").convert_alpha()
background_img = pygame.image.load("maps/map_grassland.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Initialize game objects
player = Player(300, 200, player_sprites)
dialogue = DialogueManager()
orbs = OrbManager([(400, 300)], orb_img)

# Game loop
running = True
while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    player.draw(screen)
    orbs.draw_and_check(screen, player)
    dialogue.draw_if_triggered(screen, player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

