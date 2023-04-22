import pygame
import sys
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordview Wanderer")
clock = pygame.time.Clock()
running = True

WINDOW_SIZE = (1280, 720)
BG = pygame.image.load("assets/country_road.jpg")
BG = pygame.transform.scale(BG, WINDOW_SIZE)
DBZ = 0
MC = 1

def get_font(size, type): # Returns Press-Start-2P in the desired size
    if type == DBZ:
        return pygame.font.Font("assets/dbz.ttf", size)
    elif type == MC:
        return pygame.font.Font("assets/mc.otf", size)

def search():
    return

def main_menu():
    while True:
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100, DBZ).render("Worldview Wanderer", True, "#c6e2ff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        VISIT_BUTTON = Button(image=pygame.image.load("assets/blue_rect.png"), pos=(640, 400), 
                            text_input="Visit a Country", font=get_font(40, MC), base_color="#d8dfe5", hovering_color="White", scale = .22)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/blue_rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(25, MC), base_color="#d7fcd4", hovering_color="White", scale = .1)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [VISIT_BUTTON, QUIT_BUTTON]:
            # if button is VISIT_BUTTON:
            #     color = "black"
            #     pygame.draw.rect(SCREEN, color, pygame.Rect(470, 365, 350, 60))
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VISIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    search()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
pygame.quit()
