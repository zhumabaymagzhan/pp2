# Импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time
 
# Инициализация 
pygame.init()
 
# Настройка FPS (кадры в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Создание цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Другие переменные, используемые в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Скорость движения врагов
SCORE = 0  # Очки игрока
 
# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)  # Шрифт для надписей
font_small = pygame.font.SysFont("Verdana", 20)  # Маленький шрифт для счётчика очков
game_over = font.render("Game Over", True, BLACK)  # Текст "Game Over"
 
background = pygame.image.load("pp2/lab8/nn/AnimatedStreet.png")  # Загрузка фона игры
 
# Создание игрового экрана
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)  # Заполнение экрана белым цветом
pygame.display.set_caption("Game")  # Заголовок окна
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pp2/lab8/nn/Enemy.png")  # Загрузка изображения врага
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Случайная начальная позиция врага
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)  # Движение врага вниз с заданной скоростью
        if (self.rect.top > 600):  # Если враг вышел за пределы экрана
            SCORE += 1  # Увеличиваем счёт игрока
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Сбрасываем позицию врага
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pp2/lab8/nn/Player.png")  # Загрузка изображения игрока
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Начальная позиция игрока
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)  # Движение вверх
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)  # Движение вниз
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)  # Движение влево
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)  # Движение вправо
                   
# Настройка спрайтов        
P1 = Player()  # Игрок
E1 = Enemy()  # Враг
 
# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
# Добавление нового пользовательского события 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Увеличение скорости каждые 1000 мс
 
# Игровой цикл
while True:
       
    # Обработка всех событий
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5  # Увеличиваем скорость врагов
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))  # Отображение фона игры
    scores = font_small.render(str(SCORE), True, BLACK)  # Отображение счётчика очков
    DISPLAYSURF.blit(scores, (10,10))  # Рисуем текст счётчика на экране
 
    # Движение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # Выполняется при столкновении игрока и врага
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('pp2/lab8/nn/crash.wav').play()  # Звук столкновения
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)  # Экран становится красным
          DISPLAYSURF.blit(game_over, (30,250))  # Отображение текста "Game Over"
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill()  # Удаление всех спрайтов
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()  # Обновление экрана
    FramePerSec.tick(FPS)  # Ограничение FPS
