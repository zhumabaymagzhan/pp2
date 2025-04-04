import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball Move")

ball_x, ball_y = 800 // 2, 600 // 2
BALL_SPEED = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - 25 > 0:
        ball_y -= BALL_SPEED
    if keys[pygame.K_DOWN] and ball_y + 25 < 600:
        ball_y += BALL_SPEED
    if keys[pygame.K_LEFT] and ball_x - 25 > 0:
        ball_x -= BALL_SPEED
    if keys[pygame.K_RIGHT] and ball_x + 25 < 800:
        ball_x += BALL_SPEED
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 25)
    pygame.display.flip()

pygame.quit()
