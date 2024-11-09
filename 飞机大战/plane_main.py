import pygame.mixer

from plane_sprites import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1# 英雄发射子弹事件
CREATE_ENEMY_TWO = pygame.USEREVENT +2

pygame.init()
class Plane_main(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)# 1. 创建游戏的窗口
        self.clock = pygame.time.Clock()# 2. 创建游戏的时钟
        self.__create_sprites()# 3. 调用私有方法，精灵和精灵组的创建
        pygame.time.set_timer(HERO_FIRE_EVENT, 80)# 每隔 ？ 秒发射一次子弹
        pygame.time.set_timer(CREATE_ENEMY, 1000)
        pygame.time.set_timer(CREATE_ENEMY1, 3000)
        pygame.time.set_timer(CREATE_ENEMY2, 8000)
        pygame.time.set_timer(CREATE_ENEMY_TWO, 8000)
        self.paused = False  # 游戏是否暂停
        self.game_over = False #游戏是否结束
        self.score = 0
        self.supp = False #判断是否供应
        # 加载暂停按钮图片
        self.pause_image = pygame.image.load('./images/pause_nor.png')
        self.pause_rect = self.pause_image.get_rect()
        self.pause_rect.center = (SCREEN_RECT.width - 50, 50)  # 设置暂停按钮位置

        self.pause_pressed_image = pygame.image.load('./images/resume_nor.png')
        self.resume_rect = self.pause_pressed_image.get_rect()
        self.resume_rect.x = SCREEN_RECT.width - 150
        self.resume_rect.y = 30

        # 加载重新开始按钮图片
        self.restart_image = pygame.image.load('./images/again.png')
        self.restart_rect = self.restart_image.get_rect()
        self.restart_rect.center = (SCREEN_RECT.width // 2, SCREEN_RECT.height // 2)  # 设置重新开始按钮位置

        # 加载结束游戏按钮图片
        self.quit_image = pygame.image.load('./images/gameover.png')
        self.quit_rect = self.quit_image.get_rect()
        self.quit_rect.center = (SCREEN_RECT.width // 2, SCREEN_RECT.height // 2 + 100)  # 设置结束游戏按钮位置

    def __create_sprites(self):
        # 背景组
        self.groups = []
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.groups.append(self.back_group)

        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        self.groups.append(self.enemy_group)
        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.groups.append(self.hero_group)
        self.groups.append(self.hero.bullets)
        self.groups.append(self.hero.hero_bullets2)
        #生命组
        self.life1 = Life1()
        self.life1_group = pygame.sprite.Group(self.life1)
        self.groups.append(self.life1_group)

        self.life2 = Life2()
        self.life2_group = pygame.sprite.Group(self.life2)
        self.groups.append(self.life2_group)

        self.life3 = Life3()
        self.life3_group = pygame.sprite.Group(self.life3)
        self.groups.append(self.life3_group)
        #补给组
        self.supply_group = pygame.sprite.Group()
        self.groups.append(self.supply_group)
        self.supply2_group = pygame.sprite.Group()
        self.groups.append(self.supply2_group)
        #爆炸组
        self.bombs = pygame.sprite.Group()
        self.groups.append(self.bombs)

    def __update_sprites(self):
        """更新精灵组"""
        for group in self.groups:
            group.update()
            group.draw(self.screen)
        self.screen.blit(self.pause_image, self.pause_rect)
        self.screen.blit(self.pause_pressed_image, self.resume_rect)
        if self.game_over:
            self.screen.blit(self.restart_image, self.restart_rect)
            self.screen.blit(self.quit_image, self.quit_rect)

    def start_game(self):
        self.game_music()
        print("开始游戏")
        while True:
            self.clock.tick(120)
            self.__event_handler()
            if not self.paused and not self.game_over:  # 如果游戏没有暂停且没有结束才执行以下操作
                self.__cheak_collide()
                self.__update_sprites()
            self.text(0,0)
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type == HERO_FIRE_EVENT:
                if self.supp == True:
                    self.Bullet_music()
                    self.hero.fire2()

                else:
                    self.Bullet_music()
                    self.hero.fire()
            if event.type == CREATE_ENEMY:
                self.enemy1 = Enemy()
                self.enemy_group.add(self.enemy1)
            if event.type == CREATE_ENEMY1:
                self.enemy2 = Enemy1()
                self.enemy_group.add(self.enemy2)
            if event.type == CREATE_ENEMY2:
                self.enemy3 = Enemy2()
                self.enemy_group.add(self.enemy3)
            #补给定时器
            if event.type == CREATE_ENEMY_TWO:
                self.supply = Supply()
                self.supply2 = Supply2()
                self.supply_group.add(self.supply)
                self.supply2_group.add(self.supply2)
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = True
                    elif event.key == pygame.K_ESCAPE:
                        self.paused = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #点击暂停按钮
                if self.pause_rect.collidepoint(event.pos):
                    self.paused = True
                #点击继续按钮
                elif self.resume_rect.collidepoint(event.pos):
                    self.paused = False
                #点击重新开始按钮
                if self.game_over and self.restart_rect.collidepoint(event.pos):
                    self.__restart_game()
                # 点击退出游戏按钮
                elif self.game_over and self.quit_rect.collidepoint(event.pos):
                    self.__game_over()
        keys = pygame.key.get_pressed()
        if  keys[K_UP]:
            self.hero.speed1 = -5
        elif keys[K_DOWN]:
            self.hero.speed1 = 5
        else:
            self.hero.speed1 = 0
        if keys[K_LEFT]:
            self.hero.speed = -5
        elif keys[K_RIGHT]:
            self.hero.speed = 5
        else:
            self.hero.speed = 0

    #bgm背景音乐
    def game_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("game_music.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    def bomb_music(self):
        self.bomb = pygame.mixer.Sound("get_bomb.wav")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.Sound.play(self.bomb)

    def Bullet_music(self):
        self.bullet_music = pygame.mixer.Sound("bullet.wav")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.Sound.play(self.bullet_music)

    # 积分显示
    def text(self,x,y,textHeight=30,fontcolor=(255,0,0),image_name=None):
        font = pygame.font.Font('ZhouZiSongTi/ZhouZiSongTi7000Zi-2.otf',textHeight)
        #配置要显示的文字
        text_ojb = font.render('score:'+str(self.score),True,fontcolor,image_name)
        text_rect = text_ojb.get_rect()
        # 设置对象坐标
        text_rect.topleft = (x,y)
        self.screen.blit(text_ojb,text_rect)

    def weihzi(self):
        self.hero.rect.centerx = SCREEN_RECT.centerx
        self.hero.rect.y = SCREEN_RECT.bottom - 200
    def __cheak_collide(self):
        eb1 = pygame.sprite.groupcollide( self.enemy_group,self.hero.bullets,False, True)
        for enemy in eb1:
            enemy.enemy_life -= 1
            if enemy.enemy_life == 0:
                self.explosion = Bomb(self.screen, enemy.rect.center, "enemy")
                self.bombs.add(self.explosion)
                self.bomb_music()
                self.score += enemy.Score()
                enemy.kill()



        # 蓝色子弹
        eb11 = pygame.sprite.groupcollide(self.enemy_group,self.hero.hero_bullets2,  False, True)
        for enemy in eb11:
            enemy.enemy_life -= 2
            if enemy.enemy_life <= 0:
                self.explosion = Bomb(self.screen, enemy.rect.center, "enemy")
                self.bombs.add(self.explosion)
                self.bomb_music()
                self.score += enemy.Score()
                enemy.kill()
        #补给
        supply1 = pygame.sprite.spritecollide(self.hero, self.supply_group,True)
        supply2 = pygame.sprite.spritecollide(self.hero, self.supply2_group,True)
        if len(supply2) >0:
            self.supp = True
        elif len(supply1) >0:
            self.supp = False

        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group,True)
        if len(enemys) >0:

            self.hero.life -= 1
            if self.hero.life == 2:
                self.life3.kill()
                self.weihzi()
            elif self.hero.life == 1:
                self.life2.kill()
                self.weihzi()
            elif self.hero.life == 0:
                self.life1.kill()
                self.weihzi()
            else:
                self.explosion2 = Bomb(self.screen, self.hero.rect.center, "hero")
                self.bombs.add(self.explosion2)
                self.bomb_music()
                self.hero.kill()
                self.game_over = True

    def __restart_game(self):
        # 重新初始化游戏
        self.__init__()
    def __game_over(self):
        pygame.mixer.music.stop()
        pygame.quit()
        exit()
main = Plane_main()
main.start_game()














