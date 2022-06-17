import os
import pygame 
import os
from sys import exit
from random import randint
pygame.init()

def display_score():

    current_time = int(pygame.time.get_ticks() /1000) - start_time
    score_surf = test_font.render(f'{current_time}', False,('Purple'))
    score_rect = score_surf.get_rect(center = (500,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(gummy_surface, obstacle_rect)

        return obstacle_list
    else: return[]

WIDTH, HEIGHT = (1000,500)
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption ('Rainbowdash Run')
clock = pygame.time.Clock()
test_font = pygame.font.SysFont('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0 
score = 0 

bg_surface = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'mlpbackground.png')), (WIDTH, HEIGHT)).convert()
ground_surface = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'mlpground.png')), (WIDTH, HEIGHT)).convert()


#score_surf = test_font.render('Rainbow Dash Run', True, (100,0,200))
#score_rect = score_surf.get_rect(center = (500,50))

#obstacles
gummy_surface = pygame.image.load(os.path.join('Assets','gummymob.png')).convert_alpha()
GUMMY = pygame.transform.scale(gummy_surface, (90,80))
gummy_rect = GUMMY.get_rect(topleft = (900,370))

obstacle_rect_list = []

rainbowdash_surf = pygame.image.load(os.path.join('Assets','Rainbow_Dash.png')).convert_alpha()
RAINBOWDASH = pygame.transform.scale(rainbowdash_surf, (150,100))
rainbowdash_rect = RAINBOWDASH.get_rect(topleft = (100,370))
rainbowdash_gravity = 0

#INTRO SCREEN
player_stand = pygame.image.load(os.path.join('Assets','Rainbow_Dash.png')).convert_alpha()
player_stand = pygame.transform.scale(player_stand,(150,100))
player_stand_rect = player_stand.get_rect (center = (500,300))

game_name = test_font.render('Rainbowdash Run', False, (90,0,120))
game_name_rect = game_name.get_rect(center = (500,100))
game_message  = test_font.render('Press space to run', False,(90,0,120))
game_message_rect = game_message.get_rect(center = (500,400))

 # timer 
obstacle_timer = pygame.USEREVENT +1 
pygame.time.set_timer(obstacle_timer, 1400)


while True: #draw elements, updates everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rainbowdash_rect.collidepoint(event.pos) and rainbowdash_rect.bottom >= 450:
                    rainbowdash_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and rainbowdash_rect.bottom >= 450:
                    rainbowdash_gravity = -20    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                gummy_rect.left = 900
                start_time = int(pygame.time.get_ticks() /1000) - start_time    

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(gummy_rect = GUMMY.get_rect(topleft = (1000,370)))
                                               
            
    if game_active:
        screen.blit(bg_surface, (0,0))
        screen.blit(ground_surface, (0,450))
        #pygame.draw.rect(screen, 'Pink', score_rect)
        #screen.blit(score_surf, score_rect)
        score = display_score()
    

        #gummy_rect.x -= 4.5
        #if gummy_rect.right <= 0: gummy_rect.left = 1000
        #screen.blit(GUMMY, gummy_rect)

        #PLAYER MECHANICS:
        rainbowdash_gravity += 0.6
        rainbowdash_rect.y += rainbowdash_gravity
        if rainbowdash_rect.bottom >= 450: rainbowdash_rect.bottom = 450
        screen.blit(RAINBOWDASH, rainbowdash_rect)

        #obstacle mechanics:
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
    # collision 
        if gummy_rect.colliderect(rainbowdash_rect):
            game_active = False
    else:
        screen.fill(('Pink'))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False,('Purple'))
        score_message_rect = score_message.get_rect(center = (500,400))
        screen.blit(game_name, game_name_rect)

    if score == 0: screen.blit(game_message, game_message_rect)
    else: screen.blit(score_message, score_message_rect)

    pygame.display.update()

    clock.tick(60)