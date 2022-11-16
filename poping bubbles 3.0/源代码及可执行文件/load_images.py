import pygame
from pygame.locals import *
from alpha import change_alpha

pygame.init()

bg_size = width, height = 600, 720
screen = pygame.display.set_mode(bg_size)

ALPHA = 200
ALPHA_firework = 230

#加载各种颜色泡泡图片
bubble_well_image =pygame.image.load('images\\bubble_well.png').convert_alpha()
change_alpha(bubble_well_image, ALPHA)
bubble_pop1_image = pygame.image.load('images\\bubble_pop1.png').convert_alpha()
change_alpha(bubble_pop1_image, ALPHA)
bubble_pop2_image = pygame.image.load('images\\bubble_pop2.png').convert_alpha()
change_alpha(bubble_pop2_image, ALPHA)
bubble_pop3_image = pygame.image.load('images\\bubble_pop3.png').convert_alpha()
change_alpha(bubble_pop3_image, ALPHA)

bubble_well_green_image =pygame.image.load('images\\bubble_well_green.png').convert_alpha()
change_alpha(bubble_well_green_image, ALPHA)
bubble_pop1_green_image = pygame.image.load('images\\bubble_pop1_green.png').convert_alpha()
change_alpha(bubble_pop1_green_image, ALPHA)
bubble_pop2_green_image = pygame.image.load('images\\bubble_pop2_green.png').convert_alpha()
change_alpha(bubble_pop2_green_image, ALPHA)
bubble_pop3_green_image = pygame.image.load('images\\bubble_pop3_green.png').convert_alpha()
change_alpha(bubble_pop3_green_image, ALPHA)

bubble_well_orange_image =pygame.image.load('images\\bubble_well_orange.png').convert_alpha()
change_alpha(bubble_well_orange_image, ALPHA)
bubble_pop1_orange_image = pygame.image.load('images\\bubble_pop1_orange.png').convert_alpha()
change_alpha(bubble_pop1_orange_image, ALPHA)
bubble_pop2_orange_image = pygame.image.load('images\\bubble_pop2_orange.png').convert_alpha()
change_alpha(bubble_pop2_orange_image, ALPHA)
bubble_pop3_orange_image = pygame.image.load('images\\bubble_pop3_orange.png').convert_alpha()
change_alpha(bubble_pop3_orange_image, ALPHA)

bubble_well_purple_image =pygame.image.load('images\\bubble_well_purple.png').convert_alpha()
change_alpha(bubble_well_purple_image, ALPHA)
bubble_pop1_purple_image = pygame.image.load('images\\bubble_pop1_purple.png').convert_alpha()
change_alpha(bubble_pop1_purple_image, ALPHA)
bubble_pop2_purple_image = pygame.image.load('images\\bubble_pop2_purple.png').convert_alpha()
change_alpha(bubble_pop2_purple_image, ALPHA)
bubble_pop3_purple_image = pygame.image.load('images\\bubble_pop3_purple.png').convert_alpha()
change_alpha(bubble_pop3_purple_image, ALPHA)

bubble_well_red_image =pygame.image.load('images\\bubble_well_red.png').convert_alpha()
change_alpha(bubble_well_red_image, ALPHA)
bubble_pop1_red_image = pygame.image.load('images\\bubble_pop1_red.png').convert_alpha()
change_alpha(bubble_pop1_red_image, ALPHA)
bubble_pop2_red_image = pygame.image.load('images\\bubble_pop2_red.png').convert_alpha()
change_alpha(bubble_pop2_red_image, ALPHA)
bubble_pop3_red_image = pygame.image.load('images\\bubble_pop3_red.png').convert_alpha()
change_alpha(bubble_pop3_red_image, ALPHA)

bubble_well_yellow_image =pygame.image.load('images\\bubble_well_yellow.png').convert_alpha()
change_alpha(bubble_well_yellow_image, ALPHA)
bubble_pop1_yellow_image = pygame.image.load('images\\bubble_pop1_yellow.png').convert_alpha()
change_alpha(bubble_pop1_yellow_image, ALPHA)
bubble_pop2_yellow_image = pygame.image.load('images\\bubble_pop2_yellow.png').convert_alpha()
change_alpha(bubble_pop2_yellow_image, ALPHA)
bubble_pop3_yellow_image = pygame.image.load('images\\bubble_pop3_yellow.png').convert_alpha()
change_alpha(bubble_pop3_yellow_image, ALPHA)

bomb_image =pygame.image.load('images\\bomb.png').convert_alpha()
change_alpha(bomb_image, ALPHA)
set_off_bomb_image =pygame.image.load('images\\set_off_bomb.png').convert_alpha()
change_alpha(set_off_bomb_image, ALPHA)

heart_image = pygame.image.load('images\\heart.png').convert_alpha()

firework_green_image = pygame.image.load('images\\firework_green.png').convert_alpha()
change_alpha(firework_green_image, ALPHA_firework)
firework_orange_image = pygame.image.load('images\\firework_orange.png').convert_alpha()
change_alpha(firework_orange_image, ALPHA_firework)
firework_purple_image = pygame.image.load('images\\firework_purple.png').convert_alpha()
change_alpha(firework_purple_image, ALPHA_firework)

firework_purple_image = pygame.image.load('images\\firework_purple.png').convert_alpha()
firework_purple_image_rect = firework_purple_image.get_rect()
firework_green_image = pygame.image.load('images\\firework_green.png').convert_alpha()
firework_green_image_rect = firework_green_image.get_rect()
firework_orange_image = pygame.image.load('images\\firework_orange.png').convert_alpha()
firework_orange_image_rect = firework_orange_image.get_rect()

# 加载按钮图片
start_nor_image = pygame.image.load('images\\start_nor.png').convert_alpha()
start_pressed_image = pygame.image.load('images\\start_pressed.png').convert_alpha()
OK_nor_image = pygame.image.load('images\\OK_nor.png').convert_alpha()
OK_pressed_image = pygame.image.load('images\\OK_pressed.png').convert_alpha()
continue_nor_image = pygame.image.load('images\\continue_nor.png').convert_alpha()
continue_pressed_image = pygame.image.load('images\\continue_pressed.png').convert_alpha()
play_again_nor_image = pygame.image.load('images\\play_again_nor.png').convert_alpha()
play_again_pressed_image = pygame.image.load('images\\play_again_pressed.png').convert_alpha()
exit_nor_image = pygame.image.load('images\\exit_nor.png').convert_alpha()
exit_pressed_image = pygame.image.load('images\\exit_pressed.png').convert_alpha()
clear_cache_nor_image = pygame.image.load('images\\clear_cache_nor.png').convert_alpha()
clear_cache_pressed_image = pygame.image.load('images\\clear_cache_pressed.png').convert_alpha()
how_to_play_nor_image = pygame.image.load('images\\how_to_play_nor.png').convert_alpha()
how_to_play_pressed_image = pygame.image.load('images\\how_to_play_pressed.png').convert_alpha()
return_nor_image = pygame.image.load('images\\return_nor.png').convert_alpha()
return_pressed_image = pygame.image.load('images\\return_pressed.png').convert_alpha()
bomb_mode_nor_image = pygame.image.load('images\\bomb_mode_nor.png').convert_alpha()
bomb_mode_pressed_image = pygame.image.load('images\\bomb_mode_pressed.png').convert_alpha()
normal_mode_nor_image = pygame.image.load('images\\normal_mode_nor.png').convert_alpha()
normal_mode_pressed_image = pygame.image.load('images\\normal_mode_pressed.png').convert_alpha()
time_limit_mode_nor_image = pygame.image.load('images\\time_limit_mode_nor.png').convert_alpha()
time_limit_mode_pressed_image = pygame.image.load('images\\time_limit_mode_pressed.png').convert_alpha()
bomb_guide_nor_image = pygame.image.load('images\\bomb_guide_nor.png').convert_alpha()
bomb_guide_pressed_image = pygame.image.load('images\\bomb_guide_pressed.png').convert_alpha()
normal_guide_nor_image = pygame.image.load('images\\normal_guide_nor.png').convert_alpha()
normal_guide_pressed_image = pygame.image.load('images\\normal_guide_pressed.png').convert_alpha()
time_limit_guide_nor_image = pygame.image.load('images\\time_limit_guide_nor.png').convert_alpha()
time_limit_guide_pressed_image = pygame.image.load('images\\time_limit_guide_pressed.png').convert_alpha()

mouse_image = pygame.image.load('images\\mouse_small.png').convert_alpha()
mouse_image_input = pygame.image.load('images\\mouse_image_input.png').convert_alpha()

gold_image = pygame.image.load('images\\gold.png').convert_alpha()
silver_image = pygame.image.load('images\\silver.png').convert_alpha()
bronze_image = pygame.image.load('images\\bronze.png').convert_alpha()

poping_bubbles = [bubble_pop1_image, bubble_pop2_image, bubble_pop3_image]
poping_bubbles_green = [bubble_pop1_green_image, bubble_pop2_green_image, bubble_pop3_green_image]
poping_bubbles_orange = [bubble_pop1_orange_image, bubble_pop2_orange_image, bubble_pop3_orange_image]
poping_bubbles_purple = [bubble_pop1_purple_image, bubble_pop2_purple_image, bubble_pop3_purple_image]
poping_bubbles_red = [bubble_pop1_red_image, bubble_pop2_red_image, bubble_pop3_red_image]
poping_bubbles_yellow = [bubble_pop1_yellow_image, bubble_pop2_yellow_image, bubble_pop3_yellow_image]

poping_images = [poping_bubbles, poping_bubbles_green, poping_bubbles_orange, poping_bubbles_purple, poping_bubbles_red, poping_bubbles_yellow]
bubble_well_images = [bubble_well_image, bubble_well_green_image, bubble_well_orange_image, bubble_well_purple_image, bubble_well_red_image, bubble_well_yellow_image]