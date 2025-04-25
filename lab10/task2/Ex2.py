import pygame
import random
import time
import psycopg2

# ========= DATABASE FUNCTIONS ========= #

def connect():
    return psycopg2.connect(
        dbname="snake_game",
        user="postgres",
        password="123456",  # замени на свой пароль
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    print(f"Проверяем пользователя '{username}'")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        print("Пользователь найден")
        user_id = user[0]
    else:
        print("Пользователь не найден, создаем нового...")
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    data = cur.fetchone()
    print("Данные последней игры:", data)
    cur.close()
    conn.close()

    if data:
        return user_id, data[0], data[1]
    else:
        return user_id, 0, 1
    


def save_game_state(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

# ========= GAME INIT ========= #

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game with DB")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# ========= USERNAME & DB INIT ========= #

create_tables()
username = input("Введите имя пользователя: ")
user_id, score, level = get_or_create_user(username)
speed = 10 + (level - 1) * 2

# ========= GAME LOGIC ========= #

snake = [[(SCREEN_WIDTH // BLOCK_SIZE) // 2 * BLOCK_SIZE, (SCREEN_HEIGHT // BLOCK_SIZE) // 2 * BLOCK_SIZE]]

direction = "RIGHT"

# Стены для каждого уровня
LEVEL_WALLS = {
    1: [],
    2: [[x, 100] for x in range(100, 500, BLOCK_SIZE)],
    3: [[200, y] for y in range(50, 350, BLOCK_SIZE)] + [[400, y] for y in range(50, 350, BLOCK_SIZE)],
    4: [[x, 150] for x in range(0, SCREEN_WIDTH, BLOCK_SIZE)] + [[x, 250] for x in range(0, SCREEN_WIDTH, BLOCK_SIZE)],
}

def draw_walls(level):
    for wall in LEVEL_WALLS.get(level, []):
        pygame.draw.rect(screen, BLUE, (wall[0], wall[1], BLOCK_SIZE, BLOCK_SIZE))


def generate_food():
    while True:
        fx = random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        fy = random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
        if [fx, fy] not in snake:
            return fx, fy, random.randint(1, 5)
        

food_x, food_y, food_weight = generate_food()
food_timer = time.time()

running = True
paused = False

print("Игра начнётся через 3 секунды...")
time.sleep(3)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game_state(user_id, score, level)
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # P = Pause & Save
                save_game_state(user_id, score, level)
                print("Игра сохранена. Нажмите P, чтобы продолжить.")
                paused = True
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_p:
                            paused = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    elif keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    # Движение
    head = snake[0]
    if direction == "UP":
        new_head = [head[0], head[1] - BLOCK_SIZE]
    elif direction == "DOWN":
        new_head = [head[0], head[1] + BLOCK_SIZE]
    elif direction == "LEFT":
        new_head = [head[0] - BLOCK_SIZE, head[1]]
    elif direction == "RIGHT":
        new_head = [head[0] + BLOCK_SIZE, head[1]]

    snake.insert(0, new_head)
    if new_head == [food_x, food_y]:
        score += food_weight
        food_x, food_y, food_weight = generate_food()
        food_timer = time.time()
        if score // 10 > level - 1:
            level += 1
            speed += 2
    else:
        snake.pop()

    if time.time() - food_timer > 5:
        food_x, food_y, food_weight = generate_food()
        food_timer = time.time()

    # Столкновения
    if (
        new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake[1:]
    ):
        save_game_state(user_id, score, level)
        print("Игра окончена. Прогресс сохранён.")
        running = False
    if (
        new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake[1:] or
        new_head in LEVEL_WALLS.get(level, [])
    ):
        running = False
    

    # Рендеринг
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, YELLOW, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
    screen.blit(font.render(str(food_weight), True, WHITE),
                (food_x + BLOCK_SIZE // 2, food_y + BLOCK_SIZE // 2))

    score_text = font.render(f"Очки: {score}", True, WHITE)
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 150, 10))

    draw_walls(level)
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
