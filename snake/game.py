# importing libraries
import pygame
import time
import random
import pickle
from pathlib import Path
import os

#PATH
os.chdir("python/snake")

# ----------------------------------------------------------------------------------
"""variables"""

snake_speed = 8

# Window size
window_x = 300
window_y = 200

# initial score
score = 0

# defining colors
window_color = (0, 0, 0)
fruit_color = (255, 0, 0)
snake_color = (0, 179, 0)
text_color = (255, 255, 255)


try:
    with open("data", "rb") as file:
        my_unpickler = pickle.Unpickler(file)
        record = my_unpickler.load()

except :
    record = 0

# ----------------------------------------------------------------------------
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining snake body
snake_body = [[100, 50]]

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction
 
 
# displaying Score function
def show_score_record(choice, color, font, size):
   
    # creating font object score_font
    score_record_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_record_font.render(f"Score : {score}" , True, color)
    record_surface = score_record_font.render(f"Record : {record}", True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect(topleft=(5, 1))
    record_rect = record_surface.get_rect(topleft=(5,20))
     
    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(record_surface, record_rect)
 
# game over function
def Game_Over():
    
    if score > record :
        with open("data", "wb") as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(score)


    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 25)
     
    # creating a text surface on which text will be drawn
    game_over_surface = my_font.render(
        f"score : {score}     Record : {record} ", True, text_color)
     
    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
    
 

# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    """ If two keys pressed simultaneously
    we don't want snake to move into two
    directions simultaneously """
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    """Snake body growing mechanism
    if fruits and snakes collide then scores
    will be incremented by 1"""
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(window_color)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, snake_color,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, fruit_color, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        Game_Over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        Game_Over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            Game_Over()
 
    # displaying score countinuously
    show_score_record(1, text_color, 'times new roman', 15)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

