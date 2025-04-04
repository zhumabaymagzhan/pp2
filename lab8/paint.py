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
drawing_shape = None  # Текущая форма для рисования ('rect', 'circle')
eraser_mode = False

# Список сохранённых точек и фигур
shapes = []

# Основной игровой цикл
def main():
    global radius, mode, drawing_shape, eraser_mode

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Проверка нажатых клавиш для выбора формы и цвета
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_1]:
            drawing_shape = 'rect'  # Выбор прямоугольника
        elif pressed_keys[pygame.K_2]:
            drawing_shape = 'circle'  # Выбор круга
        elif pressed_keys[pygame.K_3]:
            eraser_mode = True  # Включение ластика
        else:
            eraser_mode = False

        # Управление цветами
        if pressed_keys[pygame.K_r]:
            mode = 'red'  # Красный
        elif pressed_keys[pygame.K_g]:
            mode = 'green'  # Зеленый
        elif pressed_keys[pygame.K_b]:
            mode = 'blue'  # Синий
        elif pressed_keys[pygame.K_y]:
            mode = 'yellow'  # Желтый

        # Если удерживается левая кнопка мыши
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            shapes.append((position, mode, drawing_shape, radius, eraser_mode))

        # Отрисовка сохранённых фигур
        screen.fill((0, 0, 0))  # Очистка экрана (фон чёрный)
        for shape in shapes:
            position, color, shape_type, size, is_eraser = shape

            if is_eraser:
                pygame.draw.circle(screen, (0, 0, 0), position, size)  # Ластик (рисует чёрным)
            elif shape_type == 'rect':
                pygame.draw.rect(screen, pygame.Color(color), (position[0], position[1], size * 2, size))  # Прямоугольник
            elif shape_type == 'circle':
                pygame.draw.circle(screen, pygame.Color(color), position, size)  # Круг

        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()
