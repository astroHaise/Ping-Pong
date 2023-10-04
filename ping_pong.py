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


font.init()
win_l('Выиграла левая сторона',)
win_r('Выиграла правая сторона',)



window_size = [700,500]
window = display.set_mode(window_size)
display.set_caption("background")
background = transform.scale(image.load('background.jpg'), window_size)

player_l = Player(60,60,3, 'player1')
player_r = Player(60,60,3, 'player2')
ball = GameSprite(200,200,3, '')

speed_x = 5
speed_y = 5



FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player_l.update()
        player_r.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y >= 450 or ball.rect.y <= 0:
            speed_y *= 1

        if ball.rect.x >= 650 or ball.rect.x <= 0:
            speed_x *= 1
        
        if ball.rect.x <= 0:
            window.blit(win_l,(200,200))
        if ball.rect.y >= 700:
            window.blit(win_r,(200,200  ))
        
