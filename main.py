from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, x, y, speed):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pl_image), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.x < 450:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 450:
            self.rect.y += self.speed


font.init()
font = font.Font(None, 50)
win_l = font.render('Выиграла левая сторона', True, (255, 0,0) )
win_r = font.render('Выиграла правая сторона', True, (255, 0, 0))

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption("ping-pong")
background = transform.scale(image.load('background.jpg'), window_size)

player_l = Player('racket.png', 50, 200, 3)
player_r = Player('racket.png', 600, 200, 3)
ball = GameSprite('ball.png', 200, 200, 3)

speed_x = 5
speed_y = 5

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player_l.update_l()
        player_r.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y >= 450 or ball.rect.y <= 0:
            speed_y *= 1

        if ball.rect.x >= 650:
            finish = True
            window.blit(win_l, (200, 200))

        if ball.rect.x <= 0:
            finish = True
            window.blit(win_r, (200, 200))

        player_l.reset()
        player_r.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
