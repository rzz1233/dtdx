import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY = pygame.USEREVENT
CREATE_ENEMY1 = pygame.USEREVENT+3
CREATE_ENEMY2 = pygame.USEREVENT+4
from pygame.locals import *

class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,image_path,speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        #设置图片位置
        self.rect = self.image.get_rect()

        self.speed = speed
    def update(self):
        self.rect.y += self.speed
class Background(Gamesprite):
    def __init__(self,is_alt = False):
        image_name = 'images/background.png'
        super().__init__(image_name,1)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Hero(Gamesprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./images/me1.png",0)
        self.life = 3

    # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.bottom - 200
        self.speed1 = 0
        self.bullets = pygame.sprite.Group()
        self.hero_bullets2 = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed1
        if self.rect.y < 0 :
            self.rect.y = 0
        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 1. 创建子弹精灵
        self.bullet = Bullet()
        # 2. 设置精灵的位置
        self.bullet.rect.bottom = self.rect.top-20
        self.bullet.rect.centerx = self.rect.centerx
        # 3. 将精灵添加到精灵组
        self.bullets.add(self.bullet)
    def fire2(self):
        self.hero_bullet2= hero_Bullet2()
        self.hero_bullet2.rect.bottom = self.rect.top - 20
        self.hero_bullet2.rect.centerx = self.rect.centerx
        # 3. 将精灵添加到精灵组
        self.hero_bullets2.add(self.hero_bullet2)
#hero的子弹类
class Bullet(Gamesprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-5)
        self.damage = 1  # 英雄的子弹伤害值
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
class hero_Bullet2(Gamesprite):
    def __init__(self):
        super().__init__("./images/bullet2.png",-5)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()


class Enemy(Gamesprite):
    def __init__(self):
        super().__init__("./images/enemy1.png",1)
        self.speed = random.randint(1,4)
        self.rect.center=(random.randint(50,SCREEN_RECT.width-self.rect.width),0)
        self.enemy_life = 1

    def update(self):
        super().update()
        if self.rect.bottom > SCREEN_RECT.height:
            self.kill()
    def Score(self):

        return 100
class Enemy1(Gamesprite):
    def __init__(self):
        super().__init__("./images/enemy2.png",1)
        self.speed = random.randint(1, 2)
        self.rect.center=(random.randint(70, SCREEN_RECT.width - self.rect.width),0)

        self.enemy_life = 6
    def update(self):
        super().update()
        if self.rect.bottom > SCREEN_RECT.height:
            self.kill()
    def Score(self):
        return 200
class Enemy2(Gamesprite):
    def __init__(self):
        super().__init__("./images/enemy3_n1.png",1)
        self.speed = 1
        self.rect.center = (random.randint(100, SCREEN_RECT.width - self.rect.width),0)

        self.enemy_life = 20
    def update(self):
        super().update()
        if self.rect.bottom > SCREEN_RECT.height:
            self.kill()
    def Score(self):
         return 500
class Life1(Gamesprite):
    def __init__(self):
        super().__init__("./images/life.png",1)
    def update(self):
        self.rect.x = SCREEN_RECT.width - self.rect.width
        self.rect.bottom = SCREEN_RECT.height
class Life2(Gamesprite):
    def __init__(self):
        super().__init__("./images/life.png",1)
    def update(self):
        self.rect.x = SCREEN_RECT.width - self.rect.width-50
        self.rect.bottom = SCREEN_RECT.height
class Life3(Gamesprite):
    def __init__(self):
        super().__init__("./images/life.png",1)
    def update(self):
        self.rect.x = SCREEN_RECT.width - self.rect.width-100
        self.rect.bottom = SCREEN_RECT.height
class Supply(Gamesprite):
    def __init__(self):
        super().__init__("./images/bomb_supply.png",1)
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.bottom > SCREEN_RECT.height:
            self.kill()
class Supply2(Gamesprite):
    def __init__(self):
        super().__init__("./images/bullet_supply.png",1)
        self.speed = random.randint(3, 5)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.bottom > SCREEN_RECT.height:
            self.kill()

#爆炸类
class Bomb(pygame.sprite.Sprite):
    def __init__(self, screen, pos, type):
        super().__init__()
        self.screen = screen
        if type == "enemy":
            self.images = [pygame.image.load(f"./images/enemy1_down{v}.png") for v in range(1, 5)]
        else:
            self.images = [pygame.image.load(f"./images/me_destroy_{v}.png") for v in range(1, 5)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.visible = True
        self.last_update = pygame.time.get_ticks()  # 记录上一次更新时间
        self.frame_rate = 80  # 每秒帧数

    def update(self):
        now = pygame.time.get_ticks()
        if self.visible:
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.visible = False
                    self.kill()  # 删除自己从精灵组中
                else:
                    self.image = self.images[self.index]






















        
