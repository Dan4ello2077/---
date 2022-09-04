from pygame import *
from random import randrange as rnd

window = display.set_mode((700, 500))
backgraund = transform.scale(image.load('лес.jpg'), (700, 500))
fps = 60
clock = time.Clock()
run = True
class GameSprite(sprite.Sprite):
    def __init__(self, plaer_image, plare_speed, plaer_x, plaer_y, wedhe = 85, heid = 65):
        super(). __init__()
        self.step = 0
        self.image = transform.scale(image.load(plaer_image),(wedhe,heid))
        self.speed = plare_speed
        self.rect = self.image.get_rect()
        self.rect.x = plaer_x
        self.rect.y = plaer_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Plaer(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > -35:
            self.rect.y -= 9
        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += 9
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > -35:
            self.rect.y -= 9
        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += 9
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(backgraund, (0, 0))

    display.update()
    clock.tick(fps)
