import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20  # Размер блока змейки и еды

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Скорость игры
clock = pygame.time.Clock()
speed = 10

# Инициализация змейки
snake = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]]  # Список сегментов змейки
direction = "RIGHT"  # Начальное направление движения

# Случайная позиция еды
def generate_food():
    while True:
        food_x = random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
        # Проверка, чтобы еда не появлялась на змейке
        if [food_x, food_y] not in snake:
            return food_x, food_y

food_x, food_y = generate_food()

# Счётчик очков и уровень
score = 0
level = 1

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    # Обновление позиции змейки
    head = snake[0]
    if direction == "UP":
        new_head = [head[0], head[1] - BLOCK_SIZE]
    elif direction == "DOWN":
        new_head = [head[0], head[1] + BLOCK_SIZE]
    elif direction == "LEFT":
        new_head = [head[0] - BLOCK_SIZE, head[1]]
    elif direction == "RIGHT":
        new_head = [head[0] + BLOCK_SIZE, head[1]]

    # Добавление нового сегмента и удаление хвоста
    snake.insert(0, new_head)
    if new_head == [food_x, food_y]:
        score += 1
        food_x, food_y = generate_food()
        # Увеличение уровня и скорости
        if score % 3 == 0:  # Например, каждые 3 очка уровень увеличивается
            level += 1
            speed += 2
    else:
        snake.pop()

    # Проверка на столкновение со стенами или с самой собой
    if (
        new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake[1:]
    ):
        running = False  # Конец игры

    # Отображение элементов на экране
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Отображение очков и уровня
    score_text = font.render(f"Очки: {score}", True, WHITE)
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
