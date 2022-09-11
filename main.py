from pygame import *
from random import randrange as rnd
speed_x = 3
speed_y = 3
window = display.set_mode((800, 601))
backgraund = transform.scale(image.load('лес.jpg'), (800, 700))
fps = 60
clock = time.Clock()
run = True
font.init()
font1 = font.Font(None, 50)
lose = font1.render('Правый выйграл', True, (0, 100, 0))
lose1 = font1.render('Левый выйграл', True, (0, 100, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, plaer_image, plare_speed, plaer_x, plaer_y, wedhe = 65, heid = 150):
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
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 4
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += 4
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > -10:
            self.rect.y -= 4
        if keys_pressed[K_s] and self.rect.y < 465:
            self.rect.y += 4
class Ball(GameSprite):
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


finish = False

plaer_l = Plaer('плотформа-PhotoRoom.png', 50, 700, 205)
plaer_r = Plaer('плотформа-PhotoRoom2.png', 50, 20, 205)
sphere = Ball ('сфера.png', 0, 390, 265, 45, 45)
while run != False:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if sphere.rect.x < 0:
        window.blit(lose1, (300, 200))
        finish = True
    if sphere.rect.x > 700:
        window.blit(lose, (300, 200))
        finish = True
    if finish != True:
        if sprite.collide_rect(plaer_l, sphere) or sprite.collide_rect(plaer_r, sphere):
            speed_x *= -1
        if sphere.rect.y < 0 or sphere.rect.y > 601 - 45:
            speed_y *= -1


        sphere.rect.x += speed_x
        sphere.rect.y += speed_y
        window.blit(backgraund, (0, 0))
        plaer_r.update_r()
        plaer_l.update_l()
        plaer_l.reset()
        plaer_r.reset()
        sphere.reset()
    display.update()
    clock.tick(fps)
