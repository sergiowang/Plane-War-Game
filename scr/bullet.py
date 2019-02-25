#! /usr/bin/env python
# -*- coding: gbk -*-

import pygame
import os
from config.settings import BASE_DIR
#继承类
class Bullet(pygame.sprite.Sprite):
    #构造函数，参数为子弹位置
    def __init__(self, position):
        super(Bullet, self).__init__()              #调用父类构造函数
        self.image = pygame.image.load(os.path.join(BASE_DIR,"image/bone.png"))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 30
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        子弹移动, 超出屏幕范围, 则设置死亡
        :return:
        """
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        """
        复位函数
        :param position:
        :return:
        """
        self.rect.left, self.rect.top = position
        self.active = True