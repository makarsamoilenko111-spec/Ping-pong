from pygame import *
from random import randint

display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()

finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))

        clock.tick(60)
        display.update()