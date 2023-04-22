import pygame
import sys
from button import Button


pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordview Wanderer")
clock = pygame.time.Clock()
running = True

BG = pygame.image.load("assets/background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def search():
    return

def startbackground():
    bckgr = pygame.mixer.Sound('assets/jazz.wav')
    pygame.mixer.Sound.play(bckgr)
    
def pause():
    pygame.mixer.pause()
    
def resume():
    pygame.mixer.unpause()
    


def main_menu():
    startbackground()
    P=0
    while True:
        
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Worldview Wanderer", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SEARCH_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Search for a Country", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        

        # FInally works bruv
        SONGBUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/mbut.png'), (200,200)), pos=(640,300),  text_input="", font=get_font(0), base_color="#d7fcd4", hovering_color="White")



        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [SEARCH_BUTTON, QUIT_BUTTON, SONGBUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SEARCH_BUTTON.checkForInput(MENU_MOUSE_POS):
                    search()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if SONGBUTTON.checkForInput(MENU_MOUSE_POS):
                    if P==0:
                        pause()
                        P=1
                    else:
                        resume()
                        P=0
                
                    
                    

        pygame.display.update()

main_menu()
pygame.quit()
