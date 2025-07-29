import pygame
import threading

pygame.mixer.init()

def play_sound_async(sound_path):
    def _play():
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    threading.Thread(target=_play, daemon=True).start()
