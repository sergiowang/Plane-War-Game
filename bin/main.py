#! /usr/bin/env python
# -*- coding: gbk -*-

import sys
from pygame.locals import *

#��������
from config.settings import *
#����ɻ�
from scr.myplane import myplane
#�����ӵ�
from scr.bullet import Bullet
#����л�������
from scr.enemy import SmallEnemy, Moon

#��������
bg_size = 480, 852  # ��ʼ����Ϸ������С(��, ��)
screen = pygame.display.set_mode(bg_size)  # ���ñ����Ի���
pygame.display.set_caption("���ֲ���Ҫ")  # ���ñ���, ��Ҫ����Ϊgbk�����ʽ
background = pygame.image.load(os.path.join(BASE_DIR, "image\\background.png"))  # ���ر���ͼƬ,������Ϊ��͸��
#Ѫ��
color_black = (0, 0, 0)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_white = (255, 255, 255)
#��ȡ�ҷ��ɻ�(��ʼ��һ��myplane���ʵ����me�� ֮���meȥ���в�����������myplane�ࣺ
me = myplane(bg_size)

def add_small_enemies(group1, group2, num):
    """
    ���С�͵л�
    ָ�����л�������ӵ������飨sprite.group��
    ����group1��group2���������������͵��βΣ����Դ洢���������󣨵л�����
    ��Ҫע���һ����group��Ȼ���ض��ľ�����ṹ�壬�������ڲ���Ӿ������ʱ��Ҫ�������Ӧ�ĳ�Ա����add()
    :return:
    """
    for i in range(num):
        small_enemy = SmallEnemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)

def add_Moons(group1, group2, num):
    """
    �������
    :return:
    """
    for i in range(num):
        moon = Moon(bg_size)
        group1.add(moon)
        group2.add(moon)


#��������
def main():
    pygame.mixer.music.play(loops=-1)
    running = True
    switch_image = False        #�л�ͼ��
    delay = 60          #֡��

    enemies = pygame.sprite.Group()  # ���ɵз��ɻ���(һ�־��������Դ洢���ел�����)
    small_enemies = pygame.sprite.Group()  # �з�С�ͷɻ���(��ͬ�ͺŵл�������ͬ�ľ��������洢)
    moons = pygame.sprite.Group()    #������
    add_small_enemies(small_enemies, enemies, 6)    #�������ɵз�С�ͷɻ�
    add_Moons(moons, enemies, 2)    #��������


    bullet_index = 0       #�ӵ�����
    e1_destroy_index = 0    #�л�׹������
    m1_destroy_index = 0    #����׹������
    me_destroy_index = 0    #�ҷ�׹������
    bullet1 = []       #�ӵ��б�
    bullet_num = 6
    for i in range(bullet_num):
        bullet1.append(Bullet(me.rect.midtop))     #��ʼ���ӵ��������б�

    while True:
        # ���Ʊ���ͼ
        screen.blit(background, (0, 0))
        #֡����
        clock = pygame.time.Clock()
        clock.tick(60)
        #�����л���ʶ�����л�BOOL
        if not delay % 3:
            switch_image = not switch_image

        for each in small_enemies:
            if each.active:
                # ���ѭ�����С�ɻ��л�
                each.move()
                screen.blit(each.image, each.rect)

                pygame.draw.line(screen, color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / SmallEnemy.energy
                if energy_remain > 0.2:  # ���Ѫ�����ڰٷ�֮��ʮ��Ϊ��ɫ������Ϊ��ɫ
                    energy_color = color_green
                else:
                    energy_color = color_red
                pygame.draw.line(screen, energy_color,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                 2)
            else:
                if e1_destroy_index == 0:
                    enemy1_down_sound.play()
                screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                e1_destroy_index = (e1_destroy_index + 1) % 4
                if e1_destroy_index == 0:
                    each.reset()
##############################
        for each in moons:
            if each.active:
                # ���ѭ���������
                each.move()
                screen.blit(each.image, each.rect)
                pygame.draw.line(screen, color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / Moon.energy
                if energy_remain > 0.2:  # ���Ѫ�����ڰٷ�֮��ʮ��Ϊ��ɫ������Ϊ��ɫ
                    energy_color = color_green
                else:
                    energy_color = color_red
                pygame.draw.line(screen, energy_color,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                 2)
            else:
                me.super += 1
                if m1_destroy_index == 0:
                    enemy1_down_sound.play()
                screen.blit(each.destroy_images[m1_destroy_index], each.rect)
                m1_destroy_index = (m1_destroy_index + 1) % 4
                if m1_destroy_index == 0:
                    each.reset()
##############################

        # ���ҷ��ɻ����״̬, �����л���ʶչʾ��ͬͼ��
        if me.active:
            if me.super < 30:
                #�л�����״̬�ķɻ�ͼ��
                if switch_image:
                    screen.blit(me.image_one, me.rect)
                else:
                    screen.blit(me.image_two, me.rect)

                # �ɻ�����״̬�²ſ��Է����ӵ�
                if not (delay % 10):  # ÿʮ֡����һ���ƶ����ӵ�
                    bullet_sound.play()
                    bullets = bullet1   #��ȡ�ӵ��б�
                    bullets[bullet_index].reset(me.rect.midtop)      #���ɻ�λ����Ϊ�ӵ�λ�ô���ʵ���е�reset����
                    bullet_index = (bullet_index + 1) % bullet_num      #��

                for b in bullets:
                    if b.active:  # ֻ�м�����ӵ��ſ��ܻ��ел� # ?
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enemies_hit:  # ����ӵ����зɻ�
                            b.active = False  # �ӵ����
                            for e in enemies_hit:
                                e.active = False  # С�͵л����
            #######################################
            else:
                #�л������ɻ�ͼ��
                if switch_image:
                    screen.blit(me.image_three, me.rect)
                else:
                    screen.blit(me.image_four, me.rect)

                # �ɻ�����״̬�²ſ��Է����ӵ�
                if not (delay % 1.5):  # ÿ 1.5 ֡����һ���ƶ����ӵ�
                    bullet_sound.play()
                    bullets = bullet1   #��ȡ�ӵ��б�
                    bullets[bullet_index].reset(me.rect.midtop)      #���ɻ�λ����Ϊ�ӵ�λ�ô���ʵ���е�reset����
                    bullet_index = (bullet_index + 1) % bullet_num      #��

                for b in bullets:
                    if b.active:  # ֻ�м�����ӵ��ſ��ܻ��ел� # ?
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enemies_hit:  # ����ӵ����зɻ�
                            b.active = False  # �ӵ����
                            for e in enemies_hit:
                                e.active = False  # С�͵л����
            #######################################     
        # �ٻ�״̬���Ʊ�ը�ĳ���
        else:
            if not (delay % 3):
                screen.blit(me.destroy_images[me_destroy_index], me.rect)
                me_destroy_index = (me_destroy_index + 1) % 4
                if me_destroy_index == 0:
                    me_down_sound.play()
                    me.reset()

        # ���� pygame ʵ�ֵ���ײ���� spritecollide (�ҷ��ɻ�����͵л���ײ, ���ķɻ��Ĵ������)
        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            me.active = False
            for row in enemies:
                row.active = False

        #�����л���ʶ �����л��ٶȣ�
        if delay == 0:
            delay = 60
        #֡���任
        delay -= 0.5

        #�����û�������������Ӧ��Ӧ��
        for event in pygame.event.get():
            if event.type == 12:  # ����û�������Ļ�ϵĹرհ�ť������QUIT�¼��������˳�
                pygame.quit()
                sys.exit()
        
        #��ȡ�û���������
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()

        # �ٶ����ǽ�����ͼ���������Ļ����
        pygame.display.flip()
            


