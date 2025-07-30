import pygame

class OrbManager:
    def __init__(self, orb_positions, orb_img):
        self.orbs = [pygame.Rect(x, y, 16, 16) for x, y in orb_positions]
        self.img = orb_img
        self.collected = 0

    def draw_and_check(self, screen, player):
        for orb in self.orbs[:]:
            screen.blit(self.img, (orb.x, orb.y))
            if player.rect.colliderect(orb):
                self.orbs.remove(orb)
                self.collected += 1
                print("Collected orb! Total:", self.collected)