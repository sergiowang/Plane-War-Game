#! /usr/bin/env python
# -*- coding: gbk -*-
import pygame
import os

from config.settings import BASE_DIR

# �̳� pygame.sprite.Sprite ��
class myplane(pygame.sprite.Sprite):
    #���캯��������Ϊ��Ϸ���ڳߴ磬����ݴ˽��г����ж�:
    def __init__(self, bg_size):
        super(myplane, self).__init__()        #���ø��� pygame.sprite.Sprite �Ĺ��캯��
        #����״̬ͼ��
        self.image_one = pygame.image.load(os.path.join(BASE_DIR, "image/dog1.png"))
        self.image_two = pygame.image.load(os.path.join(BASE_DIR, "image/dog2.png"))
        #����״̬ͼ��
        self.image_three = pygame.image.load(os.path.join(BASE_DIR, "image/super1.png"))
        self.image_four = pygame.image.load(os.path.join(BASE_DIR, "image/super2.png"))
        # ��ȡ�ҷ��ɻ���λ��
        self.rect = self.image_one.get_rect()
        # C��Ϸ���ڵĳߴ�
        self.width, self.height = bg_size[0], bg_size[1]
        # ��ȡ�ɻ�ͼ�����Ĥ���Ը��Ӿ�ȷ����ײ���
        self.mask = pygame.mask.from_surface(self.image_one)
        # ����ɻ���ʼ��λ�ã��ײ�Ԥ��60����
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # ���÷ɻ��ƶ��ٶ�
        self.speed = 10
        # ���÷ɻ����״̬(TrueΪ���, FalseΪ����)
        self.active = True
        # ���طɻ����ͼƬ
        self.destroy_images = []
        #ע��extend��append������ (����λ�ò���������ı䣡)
        self.destroy_images.extend(
            [                
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown1.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown2.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown2.png")),
                pygame.image.load(os.path.join(BASE_DIR, "image/dogdown1.png")),
            ]
        )
        #����״̬ (0Ϊ����״̬������2Ϊ����״̬)
        self.super = 0
        #�����ƶ�����
    def move_up(self):
        if self.rect.top > 0:  # ����ɻ���δ�ƶ�����������
            self.rect.top -= self.speed
        else:  # �������ƶ�������������ʱ����Ϊ������Եλ��
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
        # ��ʼ���ɻ�(�ɻ�����, ��ʼ������ʼλ��)
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # ���÷ɻ��Ĵ��״̬
        self.active = True
        self.super = 0