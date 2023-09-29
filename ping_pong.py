from pygame import *
from random import randint
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self,x,y, speed, img)
    super().__init__()
    self.speed = speed
    self.image = transform.scale(image.load(image),(65,65))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 0:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.x < 0:
            self.rect.x -= self.speed

            
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 0:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 0:
            self.rect.x -= self.speed


window_size = [700,500]
window = display.set_mode(window_size)
display.set_caption("background")
background = transform.scale(image.load('background.jpg'), window_size)



FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

