import pygame, sys
from button import Button
import os
from pygame import mixer
 

pygame.init()

SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background4.jpg")

def menu_bgm(wrd):
    if wrd == 1:
        mixer.music.load('menubgm.mp3')
        mixer.music.play(-1)
    else:
       mixer.music.stop()

menu_bgm(1)
    
        

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # PLAY_BACK = Button(image=None, pos=(640, 460), 
        #                     text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
            #         main_menu()

        pygame.display.update()
    
def options():
    while True:
        # OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # OPTIONS_BACK = Button(image=None, pos=(640, 460), 
        #                     text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        # OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        # OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     os.system("firstgame.py")
                # if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                #     main_menu()

        pygame.display.update()




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        GAME_TITLE = get_font(80).render("PIRATES OF CARIBBEAN", True, "#FF9912")
        GAME_RECT = GAME_TITLE.get_rect(center=(980, 80))

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "burlywood")
        MENU_RECT = MENU_TEXT.get_rect(center=(980, 250))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(970, 450), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(970, 625), 
                            text_input="1 VS 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(970, 800), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(GAME_TITLE, GAME_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu_bgm(0)
                    os.system('python POC.py')
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu_bgm(0)
                    os.system("python multiplayer.py")
                    
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()



