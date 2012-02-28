#!/usr/bin/env python
# -*- coding:utf-8 -*-
## 
#  Copyright (C) 
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation.
# 本程序是免费软件，基于GPL许可发布。
# 
##
# @文件名(file): saolei.py
# @作者(author): 龙昌锦(LongChangjin)
# @博客(blog): http://www.xefan.com
# @邮箱(mail): admin@xefan.com
# @QQ: 346202141
# @ICQ: wosuopu@gmail.com
# @时间(date): 2011-08-07
# 

import pygame
import random
from os import _exit as exit

pygame.display.init()
pygame.font.init()

wSIZE = [(260,340), (500,580), (920,580)]
gSIZE = [(8,8,10), (16,16,40), (30,16,99)]
POSx0, POSy0 = 10, 70
LEVEL = 0
MARK = 0
FACE = 'face0'

pygame.display.set_mode(wSIZE[LEVEL])
imageDict = {}
imageDict['blank'] = pygame.image.load('image/blank.png').convert_alpha()
imageDict['button'] = pygame.image.load('image/button.png').convert_alpha()
imageDict['button_ed'] = pygame.image.load('image/button_ed.png').convert_alpha()
imageDict['face0'] = pygame.image.load('image/face0.png').convert_alpha()
imageDict['face0_ed'] = pygame.image.load('image/face0_ed.png').convert_alpha()
imageDict['face1'] = pygame.image.load('image/face1.png').convert_alpha()
imageDict['face1_ed'] = pygame.image.load('image/face1_ed.png').convert_alpha()
imageDict['face2'] = pygame.image.load('image/face2.png').convert_alpha()
imageDict['face2_ed'] = pygame.image.load('image/face2_ed.png').convert_alpha()
imageDict['lei'] = pygame.image.load('image/lei.png').convert_alpha()
imageDict['lei_ed'] = pygame.image.load('image/lei_ed.png').convert_alpha()
imageDict['mark'] = pygame.image.load('image/mark.png').convert_alpha()
imageDict['mark_error'] = pygame.image.load('image/mark_error.png').convert_alpha()
imageDict[0] = pygame.image.load('image/level0.png').convert()
imageDict[1] = pygame.image.load('image/level1.png').convert()
imageDict[2] = pygame.image.load('image/level2.png').convert()

pygame.display.set_caption("扫雷 － 作者：龙昌(www.xefan.com)")
ico = pygame.image.load('logo.ico')
pygame.display.set_icon(ico)

class Saolei:
    def __init__(self):
        global MARK
        MARK = 0
        self.count = 0
        self.screen = pygame.display.set_mode(wSIZE[LEVEL], 0, 32)
        self.screen.fill((255,255,255))   
        self.screen.blit(imageDict[LEVEL],(10,0))
        self.screen.blit(imageDict[FACE],((wSIZE[LEVEL][0]-45)/2, 20))
        self.screen.fill((125,125,125),(0,65 ,wSIZE[LEVEL][0],1))
        row = 0
        while row < gSIZE[LEVEL][1]:
            col = 0
            while col < gSIZE[LEVEL][0]:
                self.screen.blit(imageDict['button'],(POSx0+col*30, POSy0+row*30))
                col += 1
            row += 1
        self.screen.fill((125,125,125),(0,wSIZE[LEVEL][1]-27 ,wSIZE[LEVEL][0],1))
        self.font = pygame.font.SysFont("宋体", 20)
        text = self.font.render(u'旗杆:'+str(MARK)+'/'+str(gSIZE[LEVEL][2])+'   ',True,(0,0,0),(255,255,255))
        self.screen.blit(text,(0,wSIZE[LEVEL][1]-25))
        self.matrix = []
        i = 0
        while i < gSIZE[LEVEL][1]:
            a = []
            j = 0
            while j < gSIZE[LEVEL][0]:
                a.append([0,0])
                j += 1
            self.matrix.append(a)
            i += 1
        i = 0
        #游戏信息
        while i < gSIZE[LEVEL][2]:
            x = random.randint(0,gSIZE[LEVEL][0]-1)
            y = random.randint(0,gSIZE[LEVEL][1]-1)
            if self.matrix[y][x][0] == -1:
                continue
            else:
                self.matrix[y][x][0] = -1
                if y > 0:
                    if self.matrix[y-1][x][0] != -1:
                        self.matrix[y-1][x][0] += 1
                    if x > 0:
                        if self.matrix[y-1][x-1][0] != -1:
                            self.matrix[y-1][x-1][0] += 1
                    if x < gSIZE[LEVEL][0]-1:
                        if self.matrix[y-1][x+1][0] != -1:
                            self.matrix[y-1][x+1][0] += 1
                if y < gSIZE[LEVEL][1]-1:
                    if self.matrix[y+1][x][0] != -1:
                        self.matrix[y+1][x][0] += 1
                    if x > 0:
                        if self.matrix[y+1][x-1][0] != -1:
                            self.matrix[y+1][x-1][0] += 1
                    if x < gSIZE[LEVEL][0]-1:
                        if self.matrix[y+1][x+1][0] != -1:
                            self.matrix[y+1][x+1][0] += 1
                if x > 0:
                    if self.matrix[y][x-1][0] != -1:
                        self.matrix[y][x-1][0] += 1
                if x < gSIZE[LEVEL][0]-1:
                    if self.matrix[y][x+1][0] != -1:
                        self.matrix[y][x+1][0] += 1
            i += 1
    def click(self,col,row):
        x = col
        y = row
        back = 0
        if self.matrix[row][col][0] != -1 and self.matrix[row][col][1] == 0:
            self.matrix[row][col][1] = 1
            self.count += 1
            self.screen.blit(imageDict['blank'],(POSx0+col*30, POSy0+row*30))
            if self.matrix[row][col][0]:
                back = 1
                text = self.font.render(str(saolei.matrix[row][col][0]),True,(0,0,0))
                self.screen.blit(text,(POSx0+col*30+10, POSy0+row*30+2))
            pygame.display.update(pygame.rect.Rect((POSx0+col*30, POSy0+row*30), (30,30)))
            if self.matrix[row][col][0]:
                return

    def fail(self):     #游戏结束
        global FACE, LEVEL
        FACE = 'face2'
        saolei.screen.blit(imageDict[FACE],((wSIZE[LEVEL][0]-45)/2, 20))
        row = 0
        while row < gSIZE[LEVEL][1]:
            col = 0
            while col < gSIZE[LEVEL][0]:
                if self.matrix[row][col][0] == -1:
                    if self.matrix[row][col][1] == 1:
                        self.screen.blit(imageDict['lei_ed'],(POSx0+col*30, POSy0+row*30))
                    elif self.matrix[row][col][1] != -1:
                        self.screen.blit(imageDict['lei'],(POSx0+col*30, POSy0+row*30))
                elif self.matrix[row][col][1] == -1:
                    self.screen.blit(imageDict['mark_error'],(POSx0+col*30, POSy0+row*30))
                col += 1
            row += 1
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                #ESC键退出
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pressed = pygame.mouse.get_pressed()
                            if mouse_pressed[0] == 1:
                                #global FACE
                                mouse_pos = pygame.mouse.get_pos()
                                #选择初级
                                if 9 < mouse_pos[0] < 51 and 0 < mouse_pos[1] < 20:
                                    FACE = 'face0'
                                    LEVEL = 0
                                    self.__init__()
                                    return
                                #选择中级
                                if 59 < mouse_pos[0] < 91 and 0 < mouse_pos[1] < 20:
                                    FACE = 'face0'
                                    LEVEL = 1
                                    self.__init__()
                                    return
                                #选择高级
                                if 109 < mouse_pos[0] < 141 and 0 < mouse_pos[1] < 20:
                                    FACE = 'face0'
                                    LEVEL = 2
                                    self.__init__()
                                    return
                                #重新开始
                                if (wSIZE[LEVEL][0]-45)/2 <= mouse_pos[0] <= (wSIZE[LEVEL][0]-45)/2+45 and 20 <= mouse_pos[1] <= 65:
                                    self.screen.blit(imageDict[FACE+'_ed'],((wSIZE[LEVEL][0]-45)/2, 20))
                                    pygame.display.update(pygame.rect.Rect(((wSIZE[LEVEL][0]-45)/2, 20), (45,45)))
                                    FACE = 'face0'
                                    pygame.time.wait(100)
                                    self.__init__()
                                    return
    def check(self):
        global LEVEL, FACE
        if self.count == gSIZE[LEVEL][0]*gSIZE[LEVEL][1]:
            FACE = 'face1'
            saolei.screen.blit(imageDict[FACE],((wSIZE[LEVEL][0]-45)/2, 20))
            text = self.font.render(u'胜利！',True,(255,0,0))
            self.screen.blit(text,(wSIZE[LEVEL][0]-125,wSIZE[LEVEL][1]-25))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit(0)
                    #ESC键退出
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit(0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pressed = pygame.mouse.get_pressed()
                                if mouse_pressed[0] == 1:
                                    #global FACE
                                    mouse_pos = pygame.mouse.get_pos()
                                    #选择初级
                                    if 9 < mouse_pos[0] < 51 and 0 < mouse_pos[1] < 20:
                                        FACE = 'face0'
                                        LEVEL = 0
                                        self.__init__()
                                        return
                                    #选择中级
                                    if 59 < mouse_pos[0] < 91 and 0 < mouse_pos[1] < 20:
                                        FACE = 'face0'
                                        LEVEL = 1
                                        self.__init__()
                                        return
                                    #选择高级
                                    if 109 < mouse_pos[0] < 141 and 0 < mouse_pos[1] < 20:
                                        FACE = 'face0'
                                        LEVEL = 2
                                        self.__init__()
                                        return
                                    #重新开始
                                    if (wSIZE[LEVEL][0]-45)/2 <= mouse_pos[0] <= (wSIZE[LEVEL][0]-45)/2+45 and 20 <= mouse_pos[1] <= 65:
                                        self.screen.blit(imageDict[FACE+'_ed'],((wSIZE[LEVEL][0]-45)/2, 20))
                                        pygame.display.update(pygame.rect.Rect(((wSIZE[LEVEL][0]-45)/2, 20), (45,45)))
                                        FACE = 'face0'
                                        pygame.time.wait(100)
                                        self.__init__()
                                        return
                    
saolei = Saolei()
pygame.display.update()

while True:
    #global LEVEL
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        #ESC键退出
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0] == 1:
                mouse_pos = pygame.mouse.get_pos()
                #选择初级
                if 9 < mouse_pos[0] < 51 and 0 < mouse_pos[1] < 20:
                    FACE = 'face0'
                    LEVEL = 0
                    saolei.__init__()
                #选择中级
                if 59 < mouse_pos[0] < 91 and 0 < mouse_pos[1] < 20:
                    FACE = 'face0'
                    LEVEL = 1
                    saolei.__init__()
                #选择高级
                if 109 < mouse_pos[0] < 141 and 0 < mouse_pos[1] < 20:
                    FACE = 'face0'
                    LEVEL = 2
                    saolei.__init__()
                #重新开始
                if (wSIZE[LEVEL][0]-45)/2 <= mouse_pos[0] <= (wSIZE[LEVEL][0]-45)/2+45 and 20 <= mouse_pos[1] <= 65:
                    saolei.screen.blit(imageDict[FACE+'_ed'],((wSIZE[LEVEL][0]-45)/2, 20))
                    pygame.display.update(pygame.rect.Rect(((wSIZE[LEVEL][0]-45)/2, 20), (45,45)))
                    FACE = 'face0'
                    pygame.time.wait(100)
                    saolei.__init__()
                #扫雷
                if POSx0 <= mouse_pos[0] <= POSx0+gSIZE[LEVEL][0]*30 and POSy0 <= mouse_pos[1] <= POSy0+gSIZE[LEVEL][1]*30:
                    col = int((mouse_pos[0]-POSx0)/30)
                    row = int((mouse_pos[1]-POSy0)/30)
                    if saolei.matrix[row][col][1] == 0:
                        #触雷
                        if saolei.matrix[row][col][0] == -1:
                            saolei.matrix[row][col][1] = 1
                            saolei.fail()
                            break
                        saolei.screen.blit(imageDict['button_ed'],(POSx0+col*30, POSy0+row*30))
                        pygame.display.update(pygame.rect.Rect((POSx0+col*30, POSy0+row*30), (30,30)))
                        pygame.time.wait(100)
                        saolei.click(col,row)
                        pygame.display.update(pygame.rect.Rect((POSx0+col*30, POSy0+row*30), (30,30)))
                        saolei.check()
            if mouse_pressed[2] == 1:
                mouse_pos = pygame.mouse.get_pos()
                if POSx0 <= mouse_pos[0] <= POSx0+gSIZE[LEVEL][0]*30 and POSy0 <= mouse_pos[1] <= POSy0+gSIZE[LEVEL][1]*30:
                    col = int((mouse_pos[0]-POSx0)/30)
                    row = int((mouse_pos[1]-POSy0)/30)
                    if saolei.matrix[row][col][1] == 0:
                        saolei.matrix[row][col][1] = -1
                        MARK += 1
                        saolei.count += 1
                        saolei.screen.blit(imageDict['mark'],(POSx0+col*30, POSy0+row*30))
                        pygame.display.update(pygame.rect.Rect((POSx0+col*30, POSy0+row*30), (30,30)))
                        text = saolei.font.render(u'旗杆:'+str(MARK)+'/'+str(gSIZE[LEVEL][2])+'   ',True,(0,0,0),(255,255,255))
                        saolei.screen.blit(text,(0,wSIZE[LEVEL][1]-25))
                        saolei.check()
                    elif saolei.matrix[row][col][1] == -1:
                        saolei.matrix[row][col][1] = 0
                        MARK -= 1
                        saolei.count -= 1
                        saolei.screen.blit(imageDict['button'],(POSx0+col*30, POSy0+row*30))
                        pygame.display.update(pygame.rect.Rect((POSx0+col*30, POSy0+row*30), (30,30)))
                        text = saolei.font.render(u'旗杆:'+str(MARK)+'/'+str(gSIZE[LEVEL][2])+'   ',True,(0,0,0),(255,255,255))
                        saolei.screen.blit(text,(0,wSIZE[LEVEL][1]-25))
    pygame.display.update()
