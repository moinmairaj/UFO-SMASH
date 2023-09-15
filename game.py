import sys, random
import pygame

#from pygame.locals import *
from time import sleep
# intialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 600))
#Title and Icon
pygame.display.set_caption('UFO SMASH')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# adding player icon or image
player_img = pygame.image.load('ufo.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))
#enemy
enemy_img = pygame.image.load('ufo copy.png')
enemy_x = random.randint(50, 700)
enemy_y = random.randint(50, 500)
enemy_x_change = 0.4
enemy_y_change = 0.4
def enemy(x, y):
    screen.blit(enemy_img, (x, y))
font = pygame.font.Font('freesansbold.ttf', 20)
def left(val):
    text = font.render(val, True, (0, 255, 0), (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (600, 40)
    screen.blit(text, text_rect)
def score(val):
    text = font.render(val, True, (0, 255, 0), (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (400, 40)
    screen.blit(text, text_rect)
#moving image using arrow keys on keyboard or mechanics of movement
# game loop
running = True
val_int = 0
lef_int = 100
while running:
    screen.fill((0, 255, 255))  #RGB
    pygame.draw.rect(screen, (0, 100, 100), (50, 50, 700, 500))
    value = str(val_int)
    l_value = str(lef_int)
    score(value)
    left(l_value)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
  #if keystroke is pressed and is it left or right side
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_DOWN:
                player_y_change = 0.5
            if event.key == pygame.K_UP:
                player_y_change = -0.5
  #      if event.type == KEYUP:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_x_change = 0
                player_y_change = 0
    player_x += player_x_change
    player_y += player_y_change
    if player_x <= 50 or player_x >= 700 or player_y <= 50 or player_y >= 500:
        player_x = 370
        player_y = 480
    enemy_x += enemy_x_change
    enemy_y += enemy_y_change
    if enemy_x <= 50 or enemy_x >= 700 or enemy_y <= 50 or enemy_y >= 500:
        enemy_x = random.randint(60, 700)
        enemy_y = random.randint(60, 500)
    if abs(player_x - enemy_x) <= 64 and abs(player_y - enemy_y) <= 64:
        val_int += 1
        enemy_x = random.randint(60, 700)
        enemy_y = random.randint(60, 500)
    if enemy_y >= 499.8 or enemy_x >= 699.6:
        lef_int -= 1
    if lef_int == 0:
        sleep(2)
        running = False
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
print('*'*10, 'GAME ENDED', '*'*10)
print('Your Score:', value)