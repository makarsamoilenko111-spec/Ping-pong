from pygame import *
from random import randint

display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
  #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ball = GameSprite('ball.png', 350, 250, 5, 55, 55)


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <395:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <395:
            self.rect.y += self.speed

font.init()

platform_left = Player('platform_left.png', 0, 150, 10, 55, 105)
platform_right = Player('platform_right.png', 650, 150, 10, 55, 105)

font1 = font.Font(None, 32)
loose1 = font1.render('PLAYER1 LOOSE', True, (188, 0, 0))
loose2 = font1.render('PLAYER2 LOOSE', True, (188, 0 , 0))

finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))
        platform_left.reset()
        platform_right.reset()
        platform_left.update_left()
        platform_right.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0: 
            speed_y *= -1
        if sprite.collide_rect(ball, platform_left) or sprite.collide_rect(ball, platform_right):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loose1, (285, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(loose2, (285, 200))

        ball.reset()
        clock.tick(60)
        display.update()

