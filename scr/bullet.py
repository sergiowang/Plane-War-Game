#! /usr/bin/env python
# -*- coding: gbk -*-

import pygame
import os
from config.settings import BASE_DIR
#�̳���
class Bullet(pygame.sprite.Sprite):
    #���캯��������Ϊ�ӵ�λ��
    def __init__(self, position):
        super(Bullet, self).__init__()              #���ø��๹�캯��
        self.image = pygame.image.load(os.path.join(BASE_DIR,"image/bone.png"))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 30
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        �ӵ��ƶ�, ������Ļ��Χ, ����������
        :return:
        """
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        """
        ��λ����
        :param position:
        :return:
        """
        self.rect.left, self.rect.top = position
        self.active = True