from pygame import *
from random import randint

display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()

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

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <420:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <420:
            self.rect.y += self.speed

platform_left = Player('platform_left.png', 0, 150, 10, 55, 105)
platform_right = Player('platform_right.png', 650, 150, 10, 55, 105)

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
        clock.tick(60)
        display.update()

