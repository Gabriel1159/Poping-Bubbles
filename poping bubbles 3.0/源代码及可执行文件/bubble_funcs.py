import pygame
from random import *

class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, speed, bg_size, poping_images):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = randint(5, self.width-self.rect.width), randint(self.height, self.height+5*self.height)
        self.speed = speed
        self.active = True
        self.poping_images = poping_images
        self.poping_index = 0
        self.count = False    # 判断是否已计入错过的泡泡
    
    def move(self):
        self.rect.top += self.speed[1]
        if (-3)*self.height<=self.rect.top<=(-2)*self.height:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width-self.rect.width), randint(self.height, self.height+5*self.height)
        self.active = True
        self.count = False

class Bomb(Bubble):
    def __init__(self, image, speed, bg_size, bomb_set_off_image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.set_off_image = bomb_set_off_image
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = randint(5, self.width-self.rect.width), randint(self.height, self.height+5*self.height)
        self.speed = speed
        self.active = True
    
    def move(self):
        self.rect.top += self.speed[1]
        if (-3)*self.height<=self.rect.top<=(-2)*self.height:
            self.reset()


def set_speed(level, num):
    speed = []
    speed_low = [-1, -2]
    speed_middle = [-3, -4]
    speed_high = [-5, -6]
    speed_too_high = -7

    if 1<=level<=2:
        for i in range(num):
            speed.append(choice(speed_low))

    elif 3<=level<=5:
        for i in range(int(num*0.5)):
            speed.append(choice(speed_low))
        for i in range(num-int(num*0.5)):
            speed.append(choice(speed_middle))

    elif 6<=level<=8:
        for i in range(int(num*0.4)):
            speed.append(choice(speed_low))
        for i in range(int(num*0.3)):
            speed.append(choice(speed_middle))
        for i in range(num-int(num*0.4)-int(num*0.3)):
            speed.append(choice(speed_high))

    elif level>8:
        for i in range(int(num*0.3)):
            speed.append(choice(speed_low))
        for i in range(int(num*0.4)):
            speed.append(choice(speed_middle))
        for i in range(int(num*0.2)):
            speed.append(choice(speed_high))
        for i in range(num-int(num*0.3)-int(num*0.4)-int(num*0.2)):
            speed.append(speed_too_high)

    return speed


def add_bubbles(ori_num, bubble_well_images, bg_size, poping_images, bubbles, level=1): 
    num = ori_num + level*2
    speed = set_speed(level, num)
    for i in range(num):
        bubble_image = choice(bubble_well_images)
        poping_bubbles_images = poping_images[bubble_well_images.index(bubble_image)]
        bubble_obj = Bubble(bubble_image, [0, speed[i]], bg_size, poping_bubbles_images)
        bubbles.append(bubble_obj)

def add_bombs(bomb_image, bg_size, bomb_set_off_image, bomb_bubbles, level=1):
    num = (level-4)//2+1
    speed = -5
    if level<4:
        pass
    else:
        for i in range(num):
            bomb_bubble_obj = Bomb(bomb_image, [0, speed], bg_size, bomb_set_off_image)
            bomb_bubbles.append(bomb_bubble_obj)


#实现暂停控制
def bubble_pause(bubbles):
    bubbles_speed = []
    count = 0
    for each in bubbles:
        bubbles_speed.append(each.speed[1])
        each.speed[1] = 0
        count += 1

    return bubbles_speed, count

def bubble_continue(bubbles, bubbles_speed, bubble_num):
    bubble_index = 0
    for each in bubbles:
        each.speed[1] = bubbles_speed[bubble_index]
        bubble_index += 1
        if bubble_num == bubble_index:
            break