import pygame
import piano_lists as pl
from pygame import mixer


pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('Terserah.ttf', 48)
medium_font = pygame.font.Font('Terserah.ttf', 28)
small_font = pygame.font.Font('Terserah.ttf', 16)
real_small_font = pygame.font.Font('Terserah.ttf', 10)

FPS = 60
timer = pygame.time.Clock()
WIDTH = 1820
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Piano')

run = True
while run:
    timer.tick(FPS)
    screen.fill('gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
