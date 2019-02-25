#! /usr/bin/env python
# -*- coding: gbk -*-

"""
    ����л�
"""

from random import randint
import os
import pygame
from config.settings import BASE_DIR

class SmallEnemy(pygame.sprite.Sprite):
    """
    ����С�ɻ�����
    """
    energy = 1

    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR,"image/enemy1.png"))
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)  # ��ȡ�ɻ�ͼ�����Ĥ���Ը��Ӿ�ȷ����ײ���
        self.speed = 2
        self.energy = SmallEnemy.energy
        # ����л����ֵ�λ��, ��֤�л������ڳ����ѿ�ʼ����������
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 * self.rect.height, -5),
        )
        self.active = True
        # ���طɻ����ͼƬ
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load(os.path.join(BASE_DIR,"image/enemy1_down1.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/enemy1_down2.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/enemy1_down3.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/enemy1_down4.png"))
            ]
        )

    def move(self):
        """
        ����л����ƶ�����
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        ���л������ƶ�����Ļ�ҷɻ�����Ҫ����������ֵ�, �Լ��л�����
        :return:
        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True


#class MidEnemy(pygame.sprite.Sprite):

#    def __init__(self):
#        super(MidEnemy, self).__init__()
#        self.image = pygame.image.load("material/image/enemy2.png")


#class BigEnemy(pygame.sprite.Sprite):

#    def __init__(self):
#        super(BigEnemy, self).__init__()
#        self.image = pygame.image.load("material/image/enemy3.png")

class Moon(pygame.sprite.Sprite):
    """
    ���������������ɱ���
    """
    energy = 10

    def __init__(self, bg_size):
        super(Moon, self).__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR,"image/moon.png"))   #����ͼƬ
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)  # ��ȡ�ɻ�ͼ�����Ĥ���Ը��Ӿ�ȷ����ײ���
        self.speed = 2.5
        self.energy = Moon.energy
        # �����������ֵ�λ��, ��֤���������ڳ���һ��ʼ����������
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 * self.rect.height, -5),
        )
        self.active = True
        # �����������ͼƬ
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load(os.path.join(BASE_DIR,"image/moon.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/moon.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/moon.png")),
                pygame.image.load(os.path.join(BASE_DIR,"image/moon.png"))
            ]
            )

    def move(self):
        """
        �����������ƶ�����
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        ���л������ƶ�����Ļ�ҷɻ�����Ҫ����������ֵ�, �Լ��л�����
        :return:
        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        