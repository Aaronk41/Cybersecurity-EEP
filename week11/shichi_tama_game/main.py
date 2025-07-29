import pygame
import sys
import json
from engine.movement import Player
from engine.dialogue import DialogueManager
from engine.orb_logic import OrbManager

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shichi Tama")
clock = pygame.time.Clock()

# Load assets
player_img = pygame.image.load("assets/sprites/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (96, 96))  # Scale up to 96x96 for bigger sprite
orb_img = pygame.image.load("assets/sprites/orb_purple.png").convert_alpha()
background_color = (155, 188, 15)  # Placeholder background

# Initialize game objects
player = Player(300, 200, player_img)
dialogue = DialogueManager()
orbs = OrbManager([(400, 300)], orb_img)

# Game loop
running = True
while running:
    screen.fill(background_color)

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
