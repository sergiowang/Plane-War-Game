#! /usr/bin/env python
# -*- coding: gbk -*-
import pygame
import os

from config.settings import BASE_DIR

# 继承 pygame.sprite.Sprite 类
class myplane(pygame.sprite.Sprite):
    #构造函数，输入为游戏窗口尺寸，需根据此进行出界判断:
    def __init__(self, bg_size):
        super(myplane, self).__init__()        #调用父类 pygame.sprite.Sprite 的构造函数
        #正常状态图像：
        self.image_one = pygame.image.load(os.path.join(BASE_DIR, "image/dog1.png"))
        self.image_two = pygame.image.load(os.path.join(BASE_DIR, "image/dog2.png"))
        #变身状态图像：
        self.image_three = pygame.image.load(os.path.join(BASE_DIR, "image/super1.png"))
        self.image_four = pygame.image.load(os.path.join(BASE_DIR, "image/super2.png"))
        # 获取我方飞机的位置
        self.rect = self.image_one.get_rect()
        # C游戏窗口的尺寸
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.mask = pygame.mask.from_surface(self.image_one)
        # 定义飞机初始化位置，底部预留60像素
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # 设置飞机移动速度
        self.speed = 10
        # 设置飞机存活状态(True为存活, False为死亡)
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        #注意extend和append的区别 (括号位置不可以随意改变！)
        self.destroy_images.extend(
            [                
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown1.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown2.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown2.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown1.png")),
            ]
        )
        #变身状态 (0为正常状态，大于2为变身状态)
        self.super = 0
        #向上移动函数
    def move_up(self):
        if self.rect.top > 0:  # 如果飞机尚未移动出背景区域
            self.rect.top -= self.speed
        else:  # 若即将移动出背景区域，则及时纠正为背景边缘位置
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        # 初始化飞机(飞机挂了, 初始化到初始位置)
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # 重置飞机的存活状态
        self.active = True
        self.super = 0