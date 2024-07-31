import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
WIDTH, HEIGHT =400,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
running = True
RED =(255,0,0)
BLUE =(0,0,255)
clock = pygame.time.Clock()
background_img = pygame.image.load('background.png')
background_img = pygame.transform.scale(background_img,(400,600))
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img,(35,35))
tube_img = pygame.image.load('tube.png')
tube_op_img = pygame.image.load('tube_op.png')
sand_img = pygame.image.load('sand3.png')
sand_img = pygame.transform.scale(sand_img,(400,30))
TUBE_WIDTH = 50
TUBE_VELOCITY = 3
tube1_x =800
tube2_x =1000
tube3_x =1200
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
tube_gap = 150
x_bird =50
y_bird =350
bird_drop_velocity =0
gravity = 0.5
score = 0
font = pygame.font.SysFont('san',40)
font1 = pygame.font.SysFont('san',80)
font2 = pygame.font.SysFont('san',60)

tube1_pass =False
tube2_pass =False
tube3_pass =False
pausing = False


while running:
    clock.tick(60)
    screen.blit(background_img, (0,0))
    bird = screen.blit(bird_img, (x_bird,y_bird)) #vechim
    #chim roi
    sand = screen.blit(sand_img,(0,570))
    y_bird += bird_drop_velocity
    bird_drop_velocity+=gravity

    tube1_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x,0))
    tube2_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x,0))
    tube3_img = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x,0))

#ong doi dien
    tube1_op_img = pygame.transform.scale(tube_op_img,(TUBE_WIDTH,600-(tube1_height+tube_gap)))
    tube1_op = screen.blit(tube_op_img, (tube1_x,tube1_height+tube_gap))
    tube2_op_img = pygame.transform.scale(tube_op_img,(TUBE_WIDTH,600-(tube2_height+tube_gap)))
    tube2_op = screen.blit(tube_op_img, (tube2_x,tube2_height+tube_gap))
    tube3_op_img = pygame.transform.scale(tube_op_img,(TUBE_WIDTH,600-(tube3_height+tube_gap)))
    tube3_op = screen.blit(tube_op_img, (tube3_x,tube3_height+tube_gap))


    '''pygame.draw.rect(screen, tube1, (tube1_x,0,TUBE_WIDTH,tube1_height))
    pygame.draw.rect(screen, tube2, (tube2_x,0,TUBE_WIDTH,tube2_height))
    pygame.draw.rect(screen, tube3, (tube3_x,0,TUBE_WIDTH,tube3_height))'''
    

    '''pygame.draw.rect(screen, BLUE, (tube1_x,tube1_height+ tube_gap,TUBE_WIDTH,HEIGHT - (tube1_height+ tube_gap)))
    pygame.draw.rect(screen, BLUE, (tube2_x,tube2_height+ tube_gap,TUBE_WIDTH,HEIGHT - (tube2_height+ tube_gap)))
    pygame.draw.rect(screen, BLUE, (tube3_x,tube3_height+ tube_gap,TUBE_WIDTH,HEIGHT - (tube3_height+ tube_gap)))'''
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY
    
    if tube1_x < - TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False

    if tube2_x < - TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100,400)
        tube2_pass = False
    if tube3_x < - TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False
#ghi diem
    score_txt = font.render("Score: "+ str(score),True, RED)
    screen.blit(score_txt,(5,5))
#cong diem
    if tube1_x + TUBE_WIDTH<=x_bird and tube1_pass ==False:
        score+=1
        tube1_pass = True  
    if tube2_x + TUBE_WIDTH<=x_bird and tube2_pass ==False:
        score+=1
        tube2_pass = True 
    if tube3_x + TUBE_WIDTH<=x_bird and tube3_pass ==False:
        score+=1
        tube3_pass = True   
#  Kiem tra
    tubes = [tube1, tube2, tube3, tube1_op, tube2_op, tube3_op, sand]
    for tube in tubes:
        if bird.colliderect(tube):
            TUBE_VELOCITY =0
            bird_drop_velocity =0
            game_over_txt = font1.render("GAME OVER", True, RED)
            screen.blit(game_over_txt,(40,270))
            score_txt2 = font2.render("Score: "+ str(score), True, BLUE)
            screen.blit(score_txt2,(120,330))
            conti = font.render("Press Space to continue!", True, RED)
            screen.blit(conti,(40,370))
            pausing =True




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity =0
                bird_drop_velocity-=7 #nhay len
                if pausing:
                    TUBE_VELOCITY = 3
                    tube1_x =800
                    tube2_x =1000
                    tube3_x =1200
                    x_bird =50
                    y_bird =350
                    score = 0
                    pausing = False


    pygame.display.flip()

pygame.quit()