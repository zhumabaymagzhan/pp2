# Импорт необходимых библиотек
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройка FPS (кадры в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)  # Золотой цвет для монет

# Переменные программы
SCREEN_WIDTH = 400  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
SPEED = 5  # Скорость движения врага
SCORE = 0  # Счет игрока
COINS_COLLECTED = 0  # Количество собранных монет
COIN_THRESHOLD = 5  # Количество монет для увеличения скорости врагов

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)  # Большой шрифт для текста
font_small = pygame.font.SysFont("Verdana", 20)  # Маленький шрифт для отображения счета
game_over = font.render("Game Over", True, BLACK)  # Текст "Game Over" при проигрыше

background = pygame.image.load("pp2/lab9/nn/AnimatedStreet.png")  # Загрузка изображения фона

# Создание окна игры
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)  # Заливка экрана белым цветом
pygame.display.set_caption("Game")  # Установка заголовка окна

# Класс Enemy (враг)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab9/nn/Enemy.png")  # Загрузка изображения врага
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Случайная начальная позиция

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Движение врага вниз
        if self.rect.top > 600:  # Если враг выходит за пределы экрана
            SCORE += 1  # Увеличиваем счет игрока
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Сбрасываем позицию врага

# Класс Player (игрок)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab9/nn/Player.png")  # Загрузка изображения игрока
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Начальная позиция игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if self.rect.left > 0:  # Проверка границ экрана (слева)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Движение влево
        if self.rect.right < SCREEN_WIDTH:  # Проверка границ экрана (справа)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Движение вправо

# Класс Coin (монета)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))  # Создание монеты размером 15x15
        self.image.fill(GOLD)  # Заливка монеты золотым цветом
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Стартовая позиция монеты сверху

    def move(self):
        # Движение монеты вниз
        self.rect.move_ip(0, 3)
        # Если монета выходит за пределы экрана, сбрасываем её позицию
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        # Сброс позиции монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update_speed(self, coins_collected):
        # Увеличиваем скорость монеты каждые 10 собранных монет
        if coins_collected % 10 == 0:
            self.speed += 0.5

# Настройка спрайтов
P1 = Player()  # Создание игрока
E1 = Enemy()  # Создание врага
coin = Coin()  # Создание монеты

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)

# Добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Увеличение скорости врагов каждые 1000 мс

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))  # Отображение фона

    # Отображение счетов на экране
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (10, 40))

    # Движение и отображение всех объектов
    for entity in enemies:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    for coin_entity in coins:
        coin_entity.move()
        DISPLAYSURF.blit(coin_entity.image, coin_entity.rect)

    DISPLAYSURF.blit(P1.image, P1.rect)
    P1.move()

    # Проверка столкновения игрока с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('pp2/lab9/nn/crash.wav').play()  # Проигрывание звука при столкновении
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)  # Экран становится красным
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображение текста "Game Over"
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаление всех спрайтов
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения игрока с монетами
    for coin in coins:
        if P1.rect.colliderect(coin.rect):  # Проверяем столкновение с монетой
            COINS_COLLECTED += 1  # Увеличиваем счетчик собранных монет
            coin.reset_position()  # Сбрасываем позицию монеты

            # Увеличиваем скорость врагов после сбора определенного количества монет
            if COINS_COLLECTED % COIN_THRESHOLD == 0:
                SPEED += 1

    pygame.display.update()  # Обновление экрана
    FramePerSec.tick(FPS)  # Ограничение FPS
