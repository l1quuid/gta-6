import pygame
from random import randint

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
back = (0, 0, 0)
win_height = 500
win_width = 500
win = pygame.display.set_mode((win_height, win_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')

class GameSprite:
    def __init__(self, image, x, y, width, height, speed):
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_d] and self.rect.x + self.rect.width < 500:
            self.rect.x += self.speed

class Player1(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.x + self.rect.width < 500:
            self.rect.x += self.speed

speedb = 2
randomspeed = randint(0, 1)
if randomspeed == 0:
    speedb *= -1

ballx = 235
bally = 225
p1x = 200
p1y = 450
p2x = 200
p2y = 30
ball = GameSprite("m.jpg", ballx, bally, 30, 30, speedb)
platform = Player("platf.jpg", p1x, p1y, 100, 20, 3)
platform1 = Player1("platf.jpg", p2x, p2y, 100, 20, 3)
backg = GameSprite("back.jpg", 0, -10, 0, 0, 0)
startwin = GameSprite("startwin.jpg", 0, -10, 0, 0, 0)

FPS = 60
game = True

score1 = 0
score2 = 0

FONT_PATH = pygame.font.match_font("Vendeta")
FONT_SIZE = pygame.font.Font(FONT_PATH, 58)
FONT1_SIZE = pygame.font.Font(FONT_PATH, 28)

speed_x = ball.speed
speed_y = -ball.speed
gamerun = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    startwin.draw()
    starttext = FONT1_SIZE.render('PRESS E TO START', True, WHITE)
    win.blit(starttext, (160, 400))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] and not gamerun:
        gamerun = True

    if gamerun:
        win.fill(back)
        backg.draw()
        ball.draw()
        platform.update()
        platform.draw()
        platform1.update()
        platform1.draw()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.x <= 0:
            speed_x *= -1

        if ball.rect.x + ball.rect.width >= 500:
            speed_x *= -1

        if platform.rect.colliderect(ball.rect):
            speed_y *= -1
        if platform1.rect.colliderect(ball.rect):
            speed_y *= -1

        score2_surface = FONT_SIZE.render(str(score2), True, WHITE)
        win.blit(score2_surface, (40, 160))
        score1_surface = FONT_SIZE.render(str(score1), True, WHITE)
        win.blit(score1_surface, (40, 280))

        if ball.rect.y > 500:
            score2 += 1
            score2_surface = FONT_SIZE.render(str(score2), True, WHITE)
            win.blit(score2_surface, (40,160))
            ball.rect.x = 235
            ball.rect.y = 225
            platform.rect.x = 200
            platform.rect.y = 450
            platform1.rect.x = 200
            platform1.rect.y = 30

        if ball.rect.y < 0:
            score1 += 1
            score1_surface = FONT_SIZE.render(str(score1), True, WHITE)
            win.blit(score1_surface, (40,280))
            ball.rect.x = 235
            ball.rect.y = 225
            platform.rect.x = 200
            platform.rect.y = 450
            platform1.rect.x = 200
            platform1.rect.y = 30

    pygame.display.update()
    clock.tick(FPS)






