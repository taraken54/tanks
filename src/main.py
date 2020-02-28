import pygame
import random

WIDTH = 1200
HEIGHT = 800
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# Направление
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../res/tank.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.duration = UP

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        
#Управление и повороты
        old_duration = self.duration
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.duration = LEFT
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.duration = RIGHT
        elif keystate[pygame.K_UP]:
            self.speedy = -8
            self.duration = UP
        elif keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.duration = DOWN
        if old_duration != self.duration :
            if (self.duration == UP and old_duration == DOWN) or (self.duration == DOWN and old_duration == UP) or (self.duration == LEFT and old_duration == RIGHT) or (self.duration == RIGHT and old_duration == LEFT):
                self.image = pygame.transform.rotate(self.image, 180)
            if (old_duration == DOWN and self.duration == RIGHT) or (old_duration == RIGHT and self.duration == UP) or (old_duration == UP and self.duration == LEFT) or (old_duration == LEFT and self.duration == DOWN):
                self.image = pygame.transform.rotate(self.image, 90)
            if (old_duration == RIGHT and self.duration == DOWN) or (old_duration == UP and self.duration == RIGHT) or (old_duration == LEFT and self.duration == UP) or (old_duration == DOWN and self.duration == LEFT):
                self.image = pygame.transform.rotate(self.image, -90)
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
