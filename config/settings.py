#! /usr/bin/env python
# -*- coding: gbk -*-

import os
import sys
import pygame

#在这里设置项目的BASE_DIR 即 项目加载文件所需的目录

# 打包时，代码冻结，使用普通的os. 要使用该路径定位到打包后，.exe文件所在的文件夹下
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS    #打包后 .exe 文件所在的文件夹位置

# 非打包时，使用正常项目根路径+material
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\material"   #文件绝对位置 —— 绝对位置上一层 —— 绝对位置上两 即PW文件夹下

pygame.init()
pygame.mixer.init()

#非打包时，BASE_DIR是“项目目录\material\”下,  打包时，是“exe文件所在目录”下
pygame.mixer.music.load(os.path.join(BASE_DIR, "sound\\BrownSugar.mp3"))
pygame.mixer.music.set_volume(0.2)

## 子弹发射音乐
bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\bullet.wav"))
bullet_sound.set_volume(0.2)

# 我方飞机挂了的音乐
me_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\game_over.wav"))
me_down_sound.set_volume(0.2)

# 敌方飞机挂了的音乐
enemy1_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\enemy1_down.wav"))
enemy1_down_sound.set_volume(0.2)

enemy2_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\enemy2_down.wav"))
enemy2_down_sound.set_volume(0.2)

enemy3_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\enemy3_down.wav"))
enemy3_down_sound.set_volume(0.2)

button_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\button.wav"))
button_down_sound.set_volume(0.2)

level_up_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\achievement.wav"))
level_up_sound.set_volume(0.2)

bomb_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\use_bomb.wav"))
bomb_sound.set_volume(0.2)

get_bomb_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\get_bomb.wav"))
get_bomb_sound.set_volume(0.2)

get_bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\get_double_laser.wav"))
get_bullet_sound.set_volume(0.2)

big_enemy_flying_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\big_spaceship_flying.wav"))
big_enemy_flying_sound.set_volume(0.2)
