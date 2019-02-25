#! /usr/bin/env python
# -*- coding: gbk -*-

import os
import sys
import pygame

#������������Ŀ��BASE_DIR �� ��Ŀ�����ļ������Ŀ¼

# ���ʱ�����붳�ᣬʹ����ͨ��os. Ҫʹ�ø�·����λ�������.exe�ļ����ڵ��ļ�����
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS    #����� .exe �ļ����ڵ��ļ���λ��

# �Ǵ��ʱ��ʹ��������Ŀ��·��+material
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\material"   #�ļ�����λ�� ���� ����λ����һ�� ���� ����λ������ ��PW�ļ�����

pygame.init()
pygame.mixer.init()

#�Ǵ��ʱ��BASE_DIR�ǡ���ĿĿ¼\material\����,  ���ʱ���ǡ�exe�ļ�����Ŀ¼����
pygame.mixer.music.load(os.path.join(BASE_DIR, "sound\\BrownSugar.mp3"))
pygame.mixer.music.set_volume(0.2)

## �ӵ���������
bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\bullet.wav"))
bullet_sound.set_volume(0.2)

# �ҷ��ɻ����˵�����
me_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR,"sound\\game_over.wav"))
me_down_sound.set_volume(0.2)

# �з��ɻ����˵�����
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
