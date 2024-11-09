from plane_sprites import *
screen = pygame.display.set_mode((480,700),0,32)#创建窗口
clock = pygame.time.Clock()#创建游戏时钟对象
#加载图片
background = pygame.image.load('images/background.png')
feiji = pygame.image.load('images/me1.png')

hero_rect = pygame.Rect(200, 500, 102, 126)#定义英雄的初始位置

enemy1 = Gamesprite("./images/enemy1.png")
enemy2 = Gamesprite("./images/enemy2.png")
enemy2.rect.y = 200
enemy_group = pygame.sprite.Group(enemy1, enemy2)

while True:
    clock.tick(120)
    for event in pygame.event.get():
        # 判断事件类型
        if event.type == pygame.QUIT:
            # 执行退出
            pygame.quit()
            exit()
    hero_rect.y -= 5
    if hero_rect.y <= 0:
        hero_rect.y = 500
    # 绘制在屏幕

    screen.blit(background, (0, 0))
    screen.blit(feiji, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)


    # 更新显示
    pygame.display.update()