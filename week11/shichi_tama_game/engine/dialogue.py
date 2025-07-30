import pygame

class DialogueManager:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 16)
        self.message = "Press SPACE to collect the sacred orbs..."
        self.show = True

    def draw_if_triggered(self, screen, player):
        if self.show and player.x < 340 and player.y < 260:
            text = self.font.render(self.message, True, (0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (50, 400, 540, 40))
            screen.blit(text, (60, 410))