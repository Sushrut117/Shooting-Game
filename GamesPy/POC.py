from ast import Pass
from codecs import backslashreplace_errors
from operator import truediv
from pickle import FALSE, TRUE
import random
from turtle import distance
import pygame
import math
from pygame import mixer
import sys

# initliaze pygame module
pygame.init()

# Window creation
screen=pygame.display.set_mode((1920,1080))

#Adding Background
background=pygame.image.load('sea7a.jpg')

#Adding Background music
mixer.music.load('bgmusic.wav')
mixer.music.play(-1)


running=True

# Window title and icon
pygame.display.set_caption("PIRATES OF CARRIBEAN")
icon=pygame.image.load('CapSparrow.png')
pygame.display.set_icon(icon)

#*****************PLAYER*********************
player_img=pygame.image.load('BlackPearl.png')
X=896
Y=1000
new_X=0
new_Y=0

#*****************ENEMY*******************

enemy_img = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemies = 18

for i in range(num_of_enemies):

    enemy_img.append(pygame.image.load('hmsnavy.png'))
    enemy_X.append( random.randint(0,1790)) 
    enemy_Y.append(random.randint(0,400))
    enemy_X_change.append(1) 
    enemy_Y_change.append(40)

#*****************CANON BALLS*******************
canonball_img=pygame.image.load('canonball.png')
canonball_X=896
canonball_Y=1000
canonball_state="ready"


#SCORE

score_value = 0

font = pygame.font.Font('freesansbold.ttf',32)

game_over_font = pygame.font.Font('freesansbold.ttf',200)

# you_lost_font = pygame.font.Font('freesansbold.ttf',200)

you_won_font = pygame.font.Font('freesansbold.ttf',200)


textX = 1775
textY = 20

def show_score(x,y):
    score = font.render("SCORE:" + str(score_value), True,(0,0,0))
    screen.blit(score,(x-16,y))


 
def player(x,y):

    screen.blit(player_img,(x,y))



def enemy(enemy_X,enemy_Y,i):
    
    screen.blit(enemy_img[i],(enemy_X,enemy_Y))



def fire_canonball(x,y):

    global canonball_state
    canonball_state = "fire"
    screen.blit(canonball_img,(canonball_X + 40,canonball_Y + 75))



def collision(canonball_X,canonball_Y,enemy_X,enemy_Y):

    distance = math.sqrt(math.pow(canonball_X - enemy_X,2) + (math.pow(canonball_Y - enemy_Y,2)))
    
    if distance <= 60:
        return TRUE
    else:
        return FALSE

clock = pygame.time.Clock()

# def paused():

#     game_pause = game_over_font.render("PAUSED", True,(0,0,0))
#     screen.blit(game_pause,(321,420))
    

#     while pause:
#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
                
#         #gameDisplay.fill(white)
        

#         # button("Continue",150,450,100,50,green,bright_green,unpause)
#         # button("Quit",550,450,100,50,red,bright_red,quitgame)

#         pygame.display.update()
#         clock.tick(15) 



def game_over():

    g_over_font = game_over_font.render("GAME OVER", True,(0,0,0))
    screen.blit(g_over_font,(321,420))


def you_won():

    u_won_font = you_won_font.render("YOU WON", True,(0,0,0))
    screen.blit(u_won_font,(445,420))


# Event handling loop
while running:
    
    #RGB
    screen.fill((0,0,0))
    #Background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #Identification of keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_X = -2.1
            if event.key == pygame.K_RIGHT:
                new_X = +2.1
            if event.key == pygame.K_DOWN:
                new_Y = +2.1
            if event.key == pygame.K_UP:
                new_Y = -2.1
            # if event.key == pygame.K_p:
            #     pause = True
            #     paused()
            if event.key == pygame.K_SPACE:
                if canonball_state == "ready":
                    fire=mixer.Sound('fire.wav')
                    fire.play()
                    canonball_X = X
                    canonball_Y = Y + 20
                    fire_canonball(canonball_X,canonball_Y)


        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                new_X= 0
            if  event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                new_Y= 0


   #Restriction of movement out of bounds of player

    if X >= 1790:
        X = 1790
    elif X <= 0:
        X = 0    
    
    if Y >= 950:
        Y = 950
    elif Y <= 700:
        Y = 700 

   


    #Restriction of boundaries of enemy and manipulation of enemy movement
    for i in range(num_of_enemies):


        if int(score_value) == 18:
            
            you_won()


        if enemy_Y[i] >580:
            
          # GAME OVER

          for j in range(num_of_enemies):

            enemy_Y[j] = 3000

                
            game_over()

            break     

                        
        enemy_X[i] += enemy_X_change[i]

        if enemy_X[i] >= 1790:
            enemy_X_change[i] += -2
            enemy_Y[i] += enemy_Y_change[i] 
        elif enemy_X[i] <= 0:
            enemy_X_change[i] += +2
            enemy_Y[i] += enemy_Y_change[i] 
    
    # if enemy_Y >= 550:
    #     new_enemy_Y += -0.8
    # elif enemy_Y <= 0:
    #     new_enemy_Y += +0.8


        #Collision detection

        collisioncheck = collision(canonball_X,canonball_Y,enemy_X[i],enemy_Y[i])

        if collisioncheck is TRUE:
            canonball_state = "ready"
            canonball_Y = 1075
            score_value += 1
            
            enemy_Y[i] = -1000
            # enemy_Y[i] = 0

            explosion=mixer.Sound('explosion.wav')
            explosion.play()

        enemy(enemy_X[i],enemy_Y[i],i)

    #CanonBall movement

    if canonball_Y <= 0:

        canonball_Y = 1075
        canonball_state = "ready"

    if canonball_state is "fire":

        canonball_Y -= 7
        fire_canonball(canonball_X,canonball_Y)



    X += new_X
    Y += new_Y

    # enemy_X += new_enemy_X
    # enemy_Y += new_enemy_Y

    player(X,Y)

    show_score(textX,textY)

    

    pygame.display.update()