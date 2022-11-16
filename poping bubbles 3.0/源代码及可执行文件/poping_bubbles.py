import pickle
import sys
import traceback
from random import *

import pygame
from pygame.locals import *

from load_images import *
from load_music import *
from bubble_funcs import *
from judge import *
from clear_cache import *
import alarm

def __TakeSecond(element):
    return element[1]

def __SetMousePos(width, height):
    flag = False
    x, y = pygame.mouse.get_pos()
    if x < 0:
        x = 0
        flag = True
    if x > width:
        x = width
        flag = True
    if y < 0:
        y = 0
        flag = True
    if y > height:
        y = height
        flag = True

    if flag:
        pygame.mouse.set_pos(x, y)

def main():
    state = 0
    '''
    state变量用于确定进入哪一界面。
    0：开始界面
    1：登录界面
    2：模式选择界面
    3：说明选择界面
    4：normal游戏界面
    5：normal说明界面
    6：normal结束界面
    7：time limit游戏界面
    8：time limit说明界面
    9：time limit结束界面
    10:结束缓冲界面
    '''      
    pygame.init()
    pygame.mixer.init()

    bg_size = width, height = 600, 720

    WHITE = (255, 255, 255)
    GRAY = (170, 170, 170)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BROWN = (255, 126, 0)

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Poping Bubbles')

    # 开始界面所需变量
    press_del = False
    show_msg_time = 0

    # 登录界面所需变量
    input_contents = ''
    user_name = ''
    waiting = 0
    OK_pressed = False
    inputing = False
    notice_show = False
    notice2_show = False

    # 游戏界面所需变量
    score = 0
    pause = False
    music_play = False
    delay = 4999
    level = 1
    missed_num = 0
    num = 10
    bubbles = []
    bomb_bubbles = []
    mouse_pressed = True
    showing = 0
    firework_show = False
    ratio = 0.1
    paused = False
    alarmed = False
    life = 3
    boom_show = 0
    ori_state = 0


    # 结束界面所需变量
    fail_played = False
    recorded = False
    added = False
    break_record = False
    record_dict = {}
    record_list = []
    fail_show = 0

    # 说明界面所需变量
    block_rect_pos = 0
    
    while True:
        # 控制鼠标不出边界
        __SetMousePos(width, height)

        # 进入开始界面
        if state == 0:
            # 设置背景
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            # 设置标题及按钮
            title_text_font = pygame.font.Font('font\\font.TTF', 72)
            title_text = title_text_font.render("Poping Bubbles!", True, BLACK)
            screen.blit(title_text, (100, 80))

            x, y = pygame.mouse.get_pos()
            # 按start进入登录界面
            screen.blit(start_nor_image, (200, 300))
            if 200<x<400 and 300<y<360:
                screen.blit(start_pressed_image, (200, 300))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 1
                    mouse_pressed = False

            # 按how to play进入说明界面
            screen.blit(how_to_play_nor_image, (200, 400))
            if 200<x<400 and 400<y<460:
                screen.blit(how_to_play_pressed_image, (200, 400))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 3
                    mouse_pressed = False

            # 按exit退出程序        
            screen.blit(exit_nor_image, (200, 500))
            if 200<x<400 and 500<y<560:
                screen.blit(exit_pressed_image, (200, 500))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()

            # 按clear cache清除缓存
            screen.blit(clear_cache_nor_image, (width-200-20, height-60-40))
            if width-200-20<x<width-20 and height-60-40<y<height-40:
                screen.blit(clear_cache_pressed_image, (width-200-20, height-60-40))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    press_del = True
                    cancel_record()
                    cancel_time_limit_record()
                    mouse_pressed = False

            if press_del:
                if show_msg_time <= 60:
                    show_msg_time += 1
                
                    del_record_text_font = pygame.font.Font('font\\font_2.TTF', 36)
                    del_record_text = del_record_text_font.render("Records has been deleted.", True, RED)
                    del_record_text_rect = del_record_text.get_rect()
                    screen.blit(del_record_text, ((width-del_record_text_rect.width)//2, height-del_record_text_rect.height-15))
                else:
                    press_del = False
                    show_msg_time = 0

            # 绘制鼠标
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        #登录界面
        elif state == 1:
            # 绘制界面
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, ((100, 180), (400, 240)), 1)
            pygame.draw.rect(screen, BLACK, ((125, 270), (350, 50)), 1)
            OK_button_rect = OK_nor_image.get_rect()
            screen.blit(OK_nor_image, ((width-OK_button_rect.width)//2, 350))
            if (width-OK_button_rect.width)//2<x<(width-OK_button_rect.width)//2+100 and 350<y<400:
                screen.blit(OK_pressed_image, ((width-OK_button_rect.width)//2, 350))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    OK_pressed = True
                    mouse_pressed = False

            # 绘制文字提示
            login_text1_font = pygame.font.Font('font\\font.ttf', 48)
            login_text1 = login_text1_font.render('Log In', True, BLACK)
            login_text1_rect = login_text1.get_rect()
            screen.blit(login_text1, ((width-login_text1_rect.width)//2, 180+5))
            login_text2_font = pygame.font.Font('font\\font_3.ttf', 30)
            login_text2 = login_text2_font.render('Your name', True, GRAY)
            

            name_text_font = login_text2_font
            name_text = name_text_font.render(input_contents, True, BLACK)
            name_text_rect = name_text.get_rect()
            screen.blit(name_text, (135, 280))

            notice_text_font = pygame.font.Font('font\\font_3.ttf', 36)
            notice_text = notice_text_font.render('Please input your name!', True, RED)
            notice_text_rect = notice_text.get_rect()
            notice_text2_font = pygame.font.Font('font\\font_3.ttf', 24)
            notice_text2 = notice_text2_font.render('Your name shall not be longer than 10 letters!', True, RED)
            notice_text2_rect = notice_text2.get_rect()

            #进入输入状态
            if 120<x<125+340 and 265<y<310:
                mouse_in = True
            else:
                mouse_in = False
            
            if mouse_in:
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    inputing = True
                    OK_pressed = False
                    notice_show = False
                    mouse_pressed = False

            if not inputing:
                screen.blit(login_text2, (135, 280))

            # 绘制输入状态闪烁竖线
            if inputing:
                waiting += 1
                if waiting>=200:
                    waiting = 0
                if 0<=(waiting%100)<50:
                    line = pygame.draw.aaline(screen, BLACK, (135 + name_text_rect.width, 280), (135 + name_text_rect.width, 310), blend=1)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True
                
                # 输入字母或使用退格键删除
                if inputing:
                    if event.type == KEYDOWN:
                        if event.unicode.isalpha():
                                input_contents += event.unicode
                        elif event.key == K_BACKSPACE:
                            input_contents = input_contents[:-1]
            
            # 输入为空显示提示1
            if notice_show:
                screen.blit(notice_text, ((600-notice_text_rect.width)//2, 430))
            # 输入过长显示提示2
            if len(input_contents)>10:
                notice2_show = True
            else:
                notice2_show = False
            if notice2_show:
                screen.blit(notice_text2, ((600-notice_text2_rect.width)//2, 480))


            # 判断名称输入是否合法，合法则储存
            if OK_pressed:
                inputing = False
                if input_contents=='':
                    notice_show = True
                
                if (not notice_show) and (not notice2_show):
                    user_name = input_contents
                    state = 2

            screen.blit(return_nor_image, (200, 620))
            if 200<x<400 and 620<y<680:
                screen.blit(return_pressed_image, (200, 620))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 0
                    mouse_pressed = False

            x, y = pygame.mouse.get_pos()
            if mouse_in:
                screen.blit(mouse_image_input, (x, y))
            else:
                screen.blit(mouse_image, (x, y))

        elif state == 2:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            mode_title_font = pygame.font.Font('font\\font_3.ttf', 48)
            mode_title = mode_title_font.render('GAME MODES', True, BLACK)
            mode_title_rect = mode_title.get_rect()
            screen.blit(mode_title, ((width-mode_title_rect.width)//2, 150))

            screen.blit(normal_mode_nor_image, (200, 250))
            if 200<x<400 and 250<y<330:
                screen.blit(normal_mode_pressed_image, (200, 250))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 4
                    mouse_pressed = False

            screen.blit(time_limit_mode_nor_image, (157, 410))
            if 157<x<443 and 410<y<490:
                screen.blit(time_limit_mode_pressed_image, (157, 410))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 7
                    mouse_pressed = False

            screen.blit(return_nor_image, (200, 620))
            if 200<x<400 and 620<y<680:
                screen.blit(return_pressed_image, (200, 620))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 0
                    mouse_pressed = False

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 3:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            mode_title_font = pygame.font.Font('font\\font_3.ttf', 48)
            mode_title = mode_title_font.render('GAME MODES', True, BLACK)
            mode_title_rect = mode_title.get_rect()
            screen.blit(mode_title, ((width-mode_title_rect.width)//2, 100))

            screen.blit(return_nor_image, (200, 620))
            if 200<x<400 and 620<y<680:
                screen.blit(return_pressed_image, (200, 620))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 0
                    mouse_pressed = False

            normal_guide_nor_image_rect = normal_guide_nor_image.get_rect()
            screen.blit(normal_guide_nor_image, ((width-normal_guide_nor_image_rect.width)//2, 230))
            if (width-normal_guide_nor_image_rect.width)//2<x<(width+normal_guide_nor_image_rect.width)//2 and 230<y<230+normal_guide_nor_image_rect.height:
                screen.blit(normal_guide_pressed_image, ((width-normal_guide_nor_image_rect.width)//2, 230))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 5
                    mouse_pressed = False

            time_limit_guide_nor_image_rect = time_limit_guide_nor_image.get_rect()
            screen.blit(time_limit_guide_nor_image, ((width-time_limit_guide_nor_image_rect.width)//2, 400))
            if (width-time_limit_guide_nor_image_rect.width)//2<x<(width+time_limit_guide_nor_image_rect.width)//2 and 400<y<400+time_limit_guide_nor_image_rect.height:
                screen.blit(time_limit_guide_pressed_image, ((width-time_limit_guide_nor_image_rect.width)//2, 400))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 8
                    mouse_pressed = False


            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 4:
            level = judge_level(score)[0]

            if not pause:
                delay += 1
                if delay==5000:
                    delay = 0

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    # 空格暂停
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            pause = True
                            pygame.mixer.music.pause()

                    if event.type == MOUSEBUTTONUP:
                        mouse_pressed = True

                # 音乐控制
                if not music_play:
                    pygame.mixer.music.play(-1)
                    music_play = True

                # 绘制界面
                screen.fill(WHITE)
                score_font = pygame.font.Font('font\\font.TTF', 36)
                score_text = score_font.render("Score : %s" % str(score), True, BLACK)
                screen.blit(score_text, (10, 5))
                level_font = pygame.font.Font('font\\font.TTF', 36)
                level_text = level_font.render("Level : %s" % str(level), True, BLACK)
                screen.blit(level_text, (10, 45))
                player_text_font = pygame.font.Font('font\\font.TTF', 36)
                player_text = player_text_font.render("Player : %s" % user_name, True, BLACK)
                screen.blit(player_text, (10, 85))
                missed_num_font = pygame.font.Font('font\\font.TTF', 36)
                if 0<=missed_num<=10:
                    missed_num_text = missed_num_font.render("You have missed : %s / 20" % str(missed_num), True, BLACK)
                elif 10<missed_num<=15:
                    missed_num_text = missed_num_font.render("You have missed : %s / 20" % str(missed_num), True, BROWN)
                elif 15<missed_num<=20:
                    missed_num_text = missed_num_font.render("You have missed : %s / 20" % str(missed_num), True, RED)
                missed_num_text_rect = missed_num_text.get_rect()
                screen.blit(missed_num_text, (width-missed_num_text_rect.width-10, 45))
                life_font = pygame.font.Font('font\\font.TTF', 36)
                life_text = life_font.render("Life : ", True, BLACK)
                life_text_rect = life_text.get_rect()
                screen.blit(life_text, (10, 125))
                heart_image_rect = heart_image.get_rect()
                for n in range(life):
                    screen.blit(heart_image, (10+life_text_rect.width+(heart_image_rect.width+5)*n, 130))
                
                mode_font = pygame.font.Font('font\\font.TTF', 36)
                mode_text = mode_font.render("Mode : normal", True, BLACK)
                mode_text_rect = mode_text.get_rect()
                screen.blit(mode_text, (width-mode_text_rect.width-10, 5))

                # 升级特效显示
                if judge_level(score)[1]:
                    firework_show = True
                else:
                    if showing>=25:
                        firework_show = False
                        showing = 0

                if not firework_show:
                    showing = 0
                elif 0<=showing<=25:
                    showing += 1

                if ratio <= 0.3:
                    ratio += 0.05
                

                if showing<=25 and firework_show:
                    firework_purple_image_big = pygame.transform.smoothscale(firework_purple_image, (int(firework_purple_image_rect.width*ratio), int(firework_purple_image_rect.height*ratio)))
                    firework_purple_image_big_rect = firework_purple_image_big.get_rect()
                    firework_orange_image_big = pygame.transform.smoothscale(firework_orange_image, (int(firework_orange_image_rect.width*ratio), int(firework_orange_image_rect.height*ratio)))
                    firework_orange_image_big_rect = firework_orange_image_big.get_rect()
                    firework_green_image_big = pygame.transform.smoothscale(firework_green_image, (int(firework_green_image_rect.width*ratio), int(firework_green_image_rect.height*ratio)))
                    firework_green_image_big_rect = firework_green_image_big.get_rect()
                    screen.blit(firework_purple_image_big, ((width-firework_purple_image_big_rect.width)//2, (height-firework_purple_image_big_rect.height)//2))
                    screen.blit(firework_orange_image_big, ((width-firework_orange_image_big_rect.width)//2+120, (height-firework_orange_image_big_rect.height)//2+160))
                    screen.blit(firework_green_image_big, ((width-firework_green_image_big_rect.width)//2-130, (height-firework_green_image_big_rect.height)//2-150))

                    firework_text_font = pygame.font.Font('font\\font_3.ttf', 72)
                    firework_text2 = firework_text_font.render('Level %s' % str(level), True, BLACK)
                    firework_text2_rect = firework_text2.get_rect()
                    screen.blit(firework_text2, ((width-firework_text2_rect.width)//2, 320))

                # 生成泡泡
                if not (delay%1000):
                    add_bubbles(num, bubble_well_images, bg_size, poping_images, bubbles, level)
                    add_bombs(bomb_image, bg_size, set_off_bomb_image, bomb_bubbles, level)

                # 点击泡泡
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    poping_objs = []

                    for each in bubbles:
                        if judge_in((x, y), [(each.rect.left, each.rect.width+each.rect.left), (each.rect.top, each.rect.top+each.rect.height)]):
                            poping_objs.append(each)

                    if poping_objs != []:
                        poping_objs[-1].active = False
                        poping_sound.play()

                    for each in bomb_bubbles:
                        if judge_in((x, y), [(each.rect.left, each.rect.width+each.rect.left), (each.rect.top, each.rect.top+each.rect.height)]):
                            life -= 1
                            each.active = False
                            bomb_sound.play()

                    mouse_pressed = False

                for each in bubbles:
                    each.move()

                    # 泡泡破裂执行模块
                    if not each.active:
                        if not (delay%1):
                            screen.blit(each.poping_images[each.poping_index], each.rect)
                            each.poping_index = (each.poping_index + 1) % 3 
                            if each.poping_index==0:
                                score += 10
                                bubbles.pop(bubbles.index(each))
                    # 泡泡正常冒出屏幕
                    else:
                        screen.blit(each.image, each.rect)
                        if (-2)*each.rect.height<=each.rect.top<=(-1)*each.rect.height:
                            if not each.count:
                                missed_num += 1
                                each.count = True

                # 错过个数超过限制，进入结束界面
                if missed_num == 20:
                    ori_state = 4
                    state = 10

                for each in bomb_bubbles:
                    each.move()

                    # 点中炸弹执行模块
                    if not each.active:
                        if not (delay%1):
                            screen.blit(each.set_off_image, each.rect)
                            boom_show += 1
                            if boom_show==10:
                                bomb_bubbles.pop(bomb_bubbles.index(each))
                                boom_show = 0

                    # 炸弹正常冒出屏幕
                    else:
                        screen.blit(each.image, each.rect)
                        if (-2)*each.rect.height<=each.rect.top<=(-1)*each.rect.height:
                            bomb_bubbles.pop(bomb_bubbles.index(each))


                # 错过个数超过限制，进入结束界面
                if life == 0:
                    state = 6

                x, y = pygame.mouse.get_pos()
                screen.blit(mouse_image, (x, y))

            # 暂停界面
            else:
                # 记录泡泡速度
                if not paused:
                    bubbles_speed = bubble_pause(bubbles)[0]
                    bubble_num = bubble_pause(bubbles)[1]
                    paused = True

                screen.fill(WHITE)
                title_text_font = pygame.font.Font('font\\font.TTF', 48)
                title_text = title_text_font.render("Poping Bubbles!", True, BLACK)
                screen.blit(title_text, (30, 20))
                pause_text_font = pygame.font.Font('font\\font.TTF', 96)
                pause_text = pause_text_font.render('PAUSE', True, BLACK)
                screen.blit(pause_text, (180, 150))
                score_font = pygame.font.Font('font\\font_3.TTF', 48)
                score_text = score_font.render("Score : %s" % str(score), True, BLACK)
                score_text_rect = score_text.get_rect()
                screen.blit(score_text, ((width-score_text_rect.width)//2, 280))

                # 恢复泡泡速度
                screen.blit(continue_nor_image, (200, 400))
                if 200<x<400 and 400<y<460:
                    screen.blit(continue_pressed_image, (200, 400))
                    if mouse_pressed and pygame.mouse.get_pressed()[0]:
                        mouse_pressed = False
                        pause = False
                        bubble_continue(bubbles, bubbles_speed, bubble_num)
                        pygame.mixer.music.unpause()

                screen.blit(exit_nor_image, (200, 500))
                if 200<x<400 and 500<y<560:
                    screen.blit(exit_pressed_image, (200, 500))
                    if mouse_pressed and pygame.mouse.get_pressed()[0]:
                        pygame.quit()
                        sys.exit()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key==K_SPACE:
                            pause = False
                            bubble_continue(bubbles, bubbles_speed, bubble_num)
                            pygame.mixer.music.unpause()

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 5:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            # 绘制界面
            bomb_guide_title_text_font = pygame.font.Font('font\\font.TTF', 48)
            bomb_guide_title_text = bomb_guide_title_text_font.render("Guidance for normal mode", True, BLACK)
            bomb_guide_title_text_rect = bomb_guide_title_text.get_rect()
            screen.blit(bomb_guide_title_text, ((width-bomb_guide_title_text_rect.width)//2, 20))

            with open('guide\\guide_normal.txt', 'r') as f:
                guide_str = f.read()

            guide_contents = guide_str.splitlines(False)
            guide_text_font = pygame.font.Font('font\\font_3.TTF', 24)
            
            line_height = pygame.font.Font.get_linesize(guide_text_font)

            for each in guide_contents:
                each_text = guide_text_font.render(each, True, BLACK)
                screen.blit(each_text, (30, 100+(line_height+15)*guide_contents.index(each)))
            
            if block_rect_pos<=height:
                block_rect_pos += 1

            pygame.draw.rect(screen, WHITE, ((0, block_rect_pos), (600, 720)), 0)

            screen.blit(return_nor_image, (200, 620))
            if 200<x<400 and 620<y<680:
                screen.blit(return_pressed_image, (200, 620))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 3
                    mouse_pressed = False
                    block_rect_pos = 0

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 6:
            # 声音控制
            pygame.mixer.music.stop()
            if not fail_played:
                fail_sound.play()
                fail_played = True

            # 绘制界面
            screen.fill(WHITE)
            screen.blit(play_again_nor_image, (200, 330))
            screen.blit(exit_nor_image, (200, 400))
            final_text1_font = pygame.font.Font('font\\font.TTF', 40)
            
            final_text2_font = pygame.font.Font('font\\font.TTF', 48)
            final_text2 = final_text2_font.render("Your Score : %s" % str(score), True, BLACK)
            final_text2_rect = final_text2.get_rect()
            screen.blit(final_text2, ((width-final_text2_rect.width)//2, 200))
            mode_font = pygame.font.Font('font\\font.TTF', 40)
            mode_text = mode_font.render("Mode : normal", True, BLACK)
            mode_text_rect = mode_text.get_rect()
            screen.blit(mode_text, (20, 70))

            #读取存档并更新最好记录
            if not recorded:
                with open('record\\highest_score.pkl', 'rb') as f:
                    record_dict = pickle.load(f)
                    print('读取存档')
                    try:
                        highest_score = record_dict[user_name]
                    except KeyError:
                        highest_score = 0
                    finally:
                        recorded = True

                if highest_score<score:
                    with open('record\\highest_score.pkl', 'wb') as f:
                        record_dict[user_name] = score
                        pickle.dump(record_dict, f)
                        print('写入存档')
                        print('写入内容为')
                        print(record_dict)
                    show_score = score
                    break_record = True
                else:
                    show_score = highest_score
            
            #按钮事件
            if 200<x<400 and 330<y<390:
                screen.blit(play_again_pressed_image, (200, 330))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    fail_sound.stop()
                    mouse_pressed = False
                    # 数据清零
                    score = 0
                    pause = False
                    music_play = False
                    delay = 4999
                    level = 1
                    missed_num = 0
                    bubbles = []
                    bomb_bubbles = []
                    life = 3
                    mouse_pressed = False
                    fail_played = False
                    recorded = False
                    break_record = False
                    record_dict = {}
                    record_list = []
                    fail_show = 0
                    # 状态改变
                    state = 2
            if 200<x<400 and 400<y<460:
                screen.blit(exit_pressed_image, (200, 400))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True
            
            

            final_text1 = final_text1_font.render("Highest Score : %s" % str(show_score), True, BLACK)
            screen.blit(final_text1, (20, 10))

            # 绘制破纪录文字
            if break_record:
                final_text3_font = pygame.font.Font('font\\font_3.TTF', 36)
                final_text3 = final_text3_font.render("New record!", True, RED)
                final_text3_rect = final_text3.get_rect()
                screen.blit(final_text3, (width-final_text3_rect.width-10, 20))

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 7:
            if not alarmed:
                alarm1 = alarm.MyThread(alarm.alarm_setter)
                alarm1.start()
                alarmed = True

            delay += 1
            if delay==5000:
                delay = 0

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            # 音乐控制
            if not music_play:
                pygame.mixer.music.play(-1)
                music_play = True

            # 绘制界面
            screen.fill(WHITE)
            score_font = pygame.font.Font('font\\font.TTF', 36)
            score_text = score_font.render("Score : %s" % str(score), True, BLACK)
            screen.blit(score_text, (10, 5))
            player_text_font = pygame.font.Font('font\\font.TTF', 36)
            player_text = player_text_font.render("Player : %s" % user_name, True, BLACK)
            screen.blit(player_text, (10, 45))
            time_text_font = pygame.font.Font('font\\font.TTF', 36)
            time_text_content = alarm.time
            if 20<=time_text_content<=30:
                time_text = time_text_font.render("Time left : %s" % str(time_text_content), True, BLACK)
            elif 10<=time_text_content<20:
                time_text = time_text_font.render("Time left : %s" % str(time_text_content), True, BROWN)
            elif time_text_content<10:
                time_text = time_text_font.render("Time left : %s" % str(time_text_content), True, RED)
            screen.blit(time_text, (10, 85))
            mode_font = pygame.font.Font('font\\font.TTF', 36)
            mode_text = mode_font.render("Mode : time limit", True, BLACK)
            mode_text_rect = mode_text.get_rect()
            screen.blit(mode_text, (width-mode_text_rect.width-10, 5))

            level = 7
            # 生成泡泡
            if not (delay%500):
                add_bubbles(num, bubble_well_images, bg_size, poping_images, bubbles, level)

            # 点击泡泡
            if mouse_pressed and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                poping_objs = []

                for each in bubbles:
                    if judge_in((x, y), [(each.rect.left, each.rect.width+each.rect.left), (each.rect.top, each.rect.top+each.rect.height)]):
                        poping_objs.append(each)

                if poping_objs != []:
                    poping_objs[-1].active = False
                    poping_sound.play()

                mouse_pressed = False

            for each in bubbles:
                each.move()

                # 泡泡破裂执行模块
                if not each.active:
                    if not (delay%1):
                        screen.blit(each.poping_images[each.poping_index], each.rect)
                        each.poping_index = (each.poping_index + 1) % 3 
                        if each.poping_index==0:
                            score += 10
                            bubbles.pop(bubbles.index(each))
                # 泡泡正常冒出屏幕
                else:
                    screen.blit(each.image, each.rect)
                    if (-2)*each.rect.height<=each.rect.top<=(-1)*each.rect.height:
                        if not each.count:
                            missed_num += 1
                            each.count = True

            if time_text_content == 0:
                ori_state = 7
                state = 10

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 8:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            # 绘制界面
            time_limit_guide_title_text_font = pygame.font.Font('font\\font.TTF', 48)
            time_limit_guide_title_text = time_limit_guide_title_text_font.render("Guidance for time limit mode", True, BLACK)
            time_limit_guide_title_text_rect = time_limit_guide_title_text.get_rect()
            screen.blit(time_limit_guide_title_text, ((width-time_limit_guide_title_text_rect.width)//2, 20))

            with open('guide\\guide_time_limit.txt', 'r') as f:
                guide_str = f.read()

            guide_contents = guide_str.splitlines(False)
            guide_text_font = pygame.font.Font('font\\font_3.TTF', 24)
            
            line_height = pygame.font.Font.get_linesize(guide_text_font)

            for each in guide_contents:
                each_text = guide_text_font.render(each, True, BLACK)
                screen.blit(each_text, (30, 120+line_height*guide_contents.index(each)*2))
            
            if block_rect_pos<=height:
                block_rect_pos += 1

            pygame.draw.rect(screen, WHITE, ((0, block_rect_pos), (600, 720)), 0)

            screen.blit(return_nor_image, (200, 620))
            if 200<x<400 and 620<y<680:
                screen.blit(return_pressed_image, (200, 620))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    state = 2
                    mouse_pressed = False
                    block_rect_pos = 0

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 9:
            # 声音控制
            pygame.mixer.music.stop()
            if not fail_played:
                fail_sound.play()
                fail_played = True

            # 绘制界面
            screen.fill(WHITE)
            screen.blit(play_again_nor_image, (200, 530))
            screen.blit(exit_nor_image, (200, 600))
            final_text1_font = pygame.font.Font('font\\font.TTF', 40)
            
            final_text2_font = pygame.font.Font('font\\font.TTF', 48)
            final_text2 = final_text2_font.render("Ranking List", True, BLACK)
            final_text2_rect = final_text2.get_rect()
            screen.blit(final_text2, ((width-final_text2_rect.width)//2, 20))

            final_text3_font = pygame.font.Font('font\\font.TTF', 48)
            final_text3 = final_text3_font.render("Your score", True, BLACK)
            final_text3_rect = final_text3.get_rect()
            screen.blit(final_text3, ((width-final_text3_rect.width)//2, 370))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONUP:
                    mouse_pressed = True

            screen.blit(gold_image, (70, 120))
            screen.blit(silver_image, (70, 200))
            screen.blit(bronze_image, (70, 280))
            
            #读取存档并更新最好记录
            if not recorded:
                with open('record\\time_limit.pkl', 'rb') as f:
                    print('读取存档')
                    record_list = pickle.load(f)
                    recorded = True

            if not added:
                record_list.append((user_name, score))
                record_list.sort(key=__TakeSecond, reverse=True)
                with open('record\\time_limit.pkl', 'wb') as f:
                    print('写入存档')
                    print('写入内容为')
                    print(record_list)
                    pickle.dump(record_list, f)

                added = True
            

            for i in range(3):
                record_show_font = pygame.font.Font('font\\font_3.ttf', 42)
                try:
                    record_show_name_text = record_show_font.render("%s" % record_list[i][0], True, BLACK)
                    record_show_name_rect = record_show_name_text.get_rect()
                    record_show_score_text = record_show_font.render('%d' % record_list[i][1], True, BLACK)
                    record_show_score_rect = record_show_score_text.get_rect()
                    screen.blit(record_show_name_text, (300-record_show_name_rect.width//2, 130+(80+5)*i))
                    screen.blit(record_show_score_text, (500-record_show_score_rect.width//2, 130+(80+5)*i))
                except IndexError:
                    error_show_text = record_show_font.render('-', True, BLACK)
                    error_show_text_rect = error_show_text.get_rect()
                    screen.blit(error_show_text, (300-error_show_text_rect.width//2, 130+(80+5)*i))
                    screen.blit(error_show_text, (500-error_show_text_rect.width//2, 130+(80+5)*i))


            current_rank_text = record_show_font.render('%s' % str(record_list.index((user_name, score))+1), True, BLACK)
            current_rank_rect = current_rank_text.get_rect()
            current_name_text = record_show_font.render('%s' % user_name, True, BLACK)
            current_name_rect = current_name_text.get_rect()
            current_score_text = record_show_font.render('%s' % score, True, BLACK)
            current_score_rect = current_score_text.get_rect()
            screen.blit(current_rank_text, (100-current_rank_rect.width//2, 440))
            screen.blit(current_name_text, (300-current_name_rect.width//2, 440))
            screen.blit(current_score_text, (500-current_score_rect.width//2, 440))

            #按钮事件
            if 200<x<400 and 530<y<590:
                screen.blit(play_again_pressed_image, (200, 530))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    fail_sound.stop()
                    mouse_pressed = False
                    # 数据清零
                    score = 0
                    pause = False
                    music_play = False
                    delay = 4999
                    level = 1
                    missed_num = 0
                    bubbles = []
                    bomb_bubbles = []
                    life = 3
                    mouse_pressed = False
                    fail_played = False
                    recorded = False
                    added = False
                    break_record = False
                    record_dict = {}
                    record_list = []
                    time_text_content = 0
                    alarmed = False
                    alarm.time = 30
                    fail_show = 0
                    
                    # 状态改变
                    state = 2
            if 200<x<400 and 600<y<660:
                screen.blit(exit_pressed_image, (200, 600))
                if mouse_pressed and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        elif state == 10:
            # 声音控制
            pygame.mixer.music.stop()
            if not fail_played:
                fail_sound.play()
                fail_played = True

            fail_show += 1
            if fail_show == 200:
                state = ori_state + 2

            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            fail_text1_font = pygame.font.Font('font\\font.ttf', 96)
            fail_text1 = fail_text1_font.render('You have failed!', True, BLACK)
            fail_text1_rect = fail_text1.get_rect()
            fail_text2_font = pygame.font.Font('font\\font.ttf', 96)
            fail_text2 = fail_text2_font.render('Time out!', True, BLACK)
            fail_text2_rect = fail_text2.get_rect()
            if ori_state == 4:
                screen.blit(fail_text1, ((width-fail_text1_rect.width)//2, 300))
            elif ori_state == 7:
                screen.blit(fail_text2, ((width-fail_text2_rect.width)//2, 300))

            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_image, (x, y))

        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(150)



if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()