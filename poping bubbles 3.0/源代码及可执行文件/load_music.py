import pygame

pygame.init()
pygame.mixer.init()

# 加载所需音效及音乐
pygame.mixer.music.load('music\\bgm.ogg')
pygame.mixer.music.set_volume(0.4)
poping_sound = pygame.mixer.Sound('music\\poping.wav')
poping_sound.set_volume(0.2)
fail_sound = pygame.mixer.Sound('music\\fail.wav')
fail_sound.set_volume(0.05)
bomb_sound = pygame.mixer.Sound('music\\bomb.wav')
bomb_sound.set_volume(0.3)