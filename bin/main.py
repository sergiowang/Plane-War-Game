#! /usr/bin/env python
# -*- coding: gbk -*-

import sys
from pygame.locals import *

#导入设置
from config.settings import *
#导入飞机
from scr.myplane import myplane
#导入子弹
from scr.bullet import Bullet
#导入敌机及月亮
from scr.enemy import SmallEnemy, Moon

#运行设置
bg_size = 480, 852  # 初始化游戏背景大小(宽, 高)
screen = pygame.display.set_mode(bg_size)  # 设置背景对话框
pygame.display.set_caption("名字不重要")  # 设置标题, 需要设置为gbk编码格式
background = pygame.image.load(os.path.join(BASE_DIR, "image\\background.png"))  # 加载背景图片,并设置为不透明
#血槽
color_black = (0, 0, 0)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_white = (255, 255, 255)
#获取我方飞机(初始化一个myplane类的实例：me， 之后对me去进行操作，而不是myplane类：
me = myplane(bg_size)

def add_small_enemies(group1, group2, num):
    """
    添加小型敌机
    指定个敌机对象添加到精灵组（sprite.group）
    参数group1、group2是两个精灵组类型的形参，用以存储多个精灵对象（敌机）。
    需要注意的一点是group既然是特定的精灵组结构体，在向其内部添加精灵对象时需要调用其对应的成员函数add()
    :return:
    """
    for i in range(num):
        small_enemy = SmallEnemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)

def add_Moons(group1, group2, num):
    """
    添加月亮
    :return:
    """
    for i in range(num):
        moon = Moon(bg_size)
        group1.add(moon)
        group2.add(moon)


#主函数：
def main():
    pygame.mixer.music.play(loops=-1)
    running = True
    switch_image = False        #切换图标
    delay = 60          #帧数

    enemies = pygame.sprite.Group()  # 生成敌方飞机组(一种精灵组用以存储所有敌机精灵)
    small_enemies = pygame.sprite.Group()  # 敌方小型飞机组(不同型号敌机创建不同的精灵组来存储)
    moons = pygame.sprite.Group()    #月亮组
    add_small_enemies(small_enemies, enemies, 6)    #生成若干敌方小型飞机
    add_Moons(moons, enemies, 2)    #生成月亮


    bullet_index = 0       #子弹索引
    e1_destroy_index = 0    #敌机坠毁索引
    m1_destroy_index = 0    #月亮坠毁索引
    me_destroy_index = 0    #我方坠毁索引
    bullet1 = []       #子弹列表
    bullet_num = 6
    for i in range(bullet_num):
        bullet1.append(Bullet(me.rect.midtop))     #初始化子弹并加入列表

    while True:
        # 绘制背景图
        screen.blit(background, (0, 0))
        #帧数：
        clock = pygame.time.Clock()
        clock.tick(60)
        #根据切换标识更改切换BOOL
        if not delay % 3:
            switch_image = not switch_image

        for each in small_enemies:
            if each.active:
                # 随机循环输出小飞机敌机
                each.move()
                screen.blit(each.image, each.rect)

                pygame.draw.line(screen, color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / SmallEnemy.energy
                if energy_remain > 0.2:  # 如果血量大于百分之二十则为绿色，否则为红色
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
                # 随机循环输出月亮
                each.move()
                screen.blit(each.image, each.rect)
                pygame.draw.line(screen, color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / Moon.energy
                if energy_remain > 0.2:  # 如果血量大于百分之二十则为绿色，否则为红色
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

        # 当我方飞机存活状态, 根据切换标识展示不同图标
        if me.active:
            if me.super < 30:
                #切换正常状态的飞机图像
                if switch_image:
                    screen.blit(me.image_one, me.rect)
                else:
                    screen.blit(me.image_two, me.rect)

                # 飞机存活的状态下才可以发射子弹
                if not (delay % 10):  # 每十帧发射一颗移动的子弹
                    bullet_sound.play()
                    bullets = bullet1   #获取子弹列表
                    bullets[bullet_index].reset(me.rect.midtop)      #将飞机位置作为子弹位置传入实例中的reset函数
                    bullet_index = (bullet_index + 1) % bullet_num      #？

                for b in bullets:
                    if b.active:  # 只有激活的子弹才可能击中敌机 # ?
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enemies_hit:  # 如果子弹击中飞机
                            b.active = False  # 子弹损毁
                            for e in enemies_hit:
                                e.active = False  # 小型敌机损毁
            #######################################
            else:
                #切换变身后飞机图像：
                if switch_image:
                    screen.blit(me.image_three, me.rect)
                else:
                    screen.blit(me.image_four, me.rect)

                # 飞机存活的状态下才可以发射子弹
                if not (delay % 1.5):  # 每 1.5 帧发射一颗移动的子弹
                    bullet_sound.play()
                    bullets = bullet1   #获取子弹列表
                    bullets[bullet_index].reset(me.rect.midtop)      #将飞机位置作为子弹位置传入实例中的reset函数
                    bullet_index = (bullet_index + 1) % bullet_num      #？

                for b in bullets:
                    if b.active:  # 只有激活的子弹才可能击中敌机 # ?
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enemies_hit:  # 如果子弹击中飞机
                            b.active = False  # 子弹损毁
                            for e in enemies_hit:
                                e.active = False  # 小型敌机损毁
            #######################################     
        # 毁坏状态绘制爆炸的场面
        else:
            if not (delay % 3):
                screen.blit(me.destroy_images[me_destroy_index], me.rect)
                me_destroy_index = (me_destroy_index + 1) % 4
                if me_destroy_index == 0:
                    me_down_sound.play()
                    me.reset()

        # 调用 pygame 实现的碰撞方法 spritecollide (我方飞机如果和敌机碰撞, 更改飞机的存活属性)
        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            me.active = False
            for row in enemies:
                row.active = False

        #更改切换标识 设置切换速度：
        if delay == 0:
            delay = 60
        #帧数变换
        delay -= 0.5

        #监听用户操作并做出相应反应：
        for event in pygame.event.get():
            if event.type == 12:  # 如果用户按下屏幕上的关闭按钮，触发QUIT事件，程序退出
                pygame.quit()
                sys.exit()
        
        #获取用户操作输入
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()

        # 再而我们将背景图像并输出到屏幕上面
        pygame.display.flip()
            


