import pygame
import sys
from datetime import datetime

pygame.init()
pygame.display.set_caption("Mickey Clock")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
screen.fill((255 ,255 ,255))

back = pygame.image.load("pp2/lab7/images/back.png")
minute = pygame.image.load("pp2/lab7/images/minute.png")
second = pygame.image.load("pp2/lab7/images/second.png")

running = True
while running:
    now = datetime.now()
    nowMin = now.minute
    nowSec = now.second
    minAng = nowMin * 6
    secAng = nowSec * 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    rot_min = pygame.transform.rotate(minute, -minAng)
    rot_sec = pygame.transform.rotate(second, -secAng)
    screen.blit(back, (0, 0))
    screen.blit(rot_min, (300 - int(rot_min.get_width()) // 2, 300 - int(rot_min.get_height()) // 2))
    screen.blit(rot_sec, (300 - int(rot_sec.get_width()) // 2, 300 - int(rot_sec.get_height()) // 2))
    pygame.display.flip()
    clock.tick(1)
    