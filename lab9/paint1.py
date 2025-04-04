import pygame

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Extended Paint Project")

clock = pygame.time.Clock()

# Параметры рисования
radius = 30
mode = 'blue'  # Цвет
drawing_shape = 'circle'  # Текущая форма рисования
eraser_mode = False

# Список сохранённых фигур
shapes = []

# Основной игровой цикл
def main():
    global radius, mode, drawing_shape, eraser_mode

    while True:
        pressed_keys = pygame.key.get_pressed()

        # Управление цветами
        if pressed_keys[pygame.K_r]:
            mode = 'red'
        elif pressed_keys[pygame.K_g]:
            mode = 'green'
        elif pressed_keys[pygame.K_b]:
            mode = 'blue'
        elif pressed_keys[pygame.K_y]:
            mode = 'yellow'

        # Выбор формы
        if pressed_keys[pygame.K_1]:
            drawing_shape = 'square'
        elif pressed_keys[pygame.K_2]:
            drawing_shape = 'right_triangle'
        elif pressed_keys[pygame.K_3]:
            drawing_shape = 'equilateral_triangle'
        elif pressed_keys[pygame.K_4]:
            drawing_shape = 'rhombus'
        elif pressed_keys[pygame.K_5]:
            drawing_shape = 'circle'
        elif pressed_keys[pygame.K_6]:
            eraser_mode = True
        else:
            eraser_mode = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Если удерживается левая кнопка мыши
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            shapes.append((position, mode, drawing_shape, radius, eraser_mode))

        # Отрисовка сохранённых фигур
        screen.fill((0, 0, 0))  # Фон экрана
        for shape in shapes:
            position, color, shape_type, size, is_eraser = shape

            if is_eraser:
                pygame.draw.circle(screen, (0, 0, 0), position, size)  # Ластик
            elif shape_type == 'circle':
                pygame.draw.circle(screen, pygame.Color(color), position, size)
            elif shape_type == 'square':
                pygame.draw.rect(screen, pygame.Color(color), (position[0], position[1], size, size))
            elif shape_type == 'right_triangle':
                pygame.draw.polygon(screen, pygame.Color(color),
                                    [position,
                                     (position[0] + size, position[1]),
                                     (position[0], position[1] + size)])
            elif shape_type == 'equilateral_triangle':
                pygame.draw.polygon(screen, pygame.Color(color),
                                    [position,
                                     (position[0] - size // 2, position[1] + size),
                                     (position[0] + size // 2, position[1] + size)])
            elif shape_type == 'rhombus':
                pygame.draw.polygon(screen, pygame.Color(color),
                                    [(position[0], position[1] - size // 2),
                                     (position[0] - size // 2, position[1]),
                                     (position[0], position[1] + size // 2),
                                     (position[0] + size // 2, position[1])])

        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()
