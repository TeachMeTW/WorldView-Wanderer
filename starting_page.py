import pygame
import sys
from button import Button


pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordview Wanderer")
clock = pygame.time.Clock()
running = True

def blurSurf(surface, amt):
    """
    Blur the given surface by the given 'amount'.  Only values 1 and greater
    are valid.  Value 1 = no blur.
    """
    if amt < 1.0:
        raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
    scale = 1.0/float(amt)
    surf_size = surface.get_size()
    scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
    surf = pygame.transform.smoothscale(surface, scale_size)
    surf = pygame.transform.smoothscale(surf, surf_size)
    return surf

WINDOW_SIZE = (1280, 720)
BG = pygame.image.load("assets/lake.jpg")
BG = pygame.transform.scale(BG, WINDOW_SIZE)
BG  = blurSurf(BG, 10)
DBZ = 0
MC = 1
WIDTH = 1280
HEIGHT = 720
I = 0



def get_font(size, type): # Returns Press-Start-2P in the desired size
    if type == DBZ:
        return pygame.font.Font("assets/dbz.ttf", size)
    elif type == MC:
        return pygame.font.Font("assets/mc.otf", size)

def search():
    return

def startbackground():
    bckgr = pygame.mixer.Sound('assets/jazz.wav')
    pygame.mixer.Sound.play(bckgr)
    
def endbackground():
    pygame.mixer.music.stop()

def main_menu():
    startbackground()
    I = 0
    Flip = True
    BG = pygame.image.load("assets/lake.jpg")
    BG = pygame.transform.scale(BG, WINDOW_SIZE)
    BG  = blurSurf(BG, 10)
    while True:
        
        # SCREEN.blit(BG, (0,0))
        SCREEN.fill((0,0,0))
        SCREEN.blit(BG,(I,0))
        flipBG = pygame.transform.flip(BG, True, False)
        SCREEN.blit(flipBG,(WIDTH + I,0))
        print("being hit")
        print(I)
        print(WIDTH)
        if (I==-WIDTH):
            print("HIT HIT HIT")
            # if Flip:
            #     BG = pygame.transform.flip(BG, True, False)
            #     SCREEN.blit(BG,(WIDTH+I,0))
            #     Flip = False
            # else:
            #     BG = pygame.transform.flip(BG, True, False)
            #     SCREEN.blit(BG,(WIDTH+I,0))
            #     Flip = True
            SCREEN.blit(BG,(I,0))
           
            I=0
        I-=1

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

class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('assets/lake.jpg')
            self.bgimage = BG = pygame.transform.scale(self.bgimage, WINDOW_SIZE)
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.moving_speed = 5
         
      def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         SCREEN.blit(self.bgimage, (self.bgX1, self.bgY1))
         SCREEN.blit(self.bgimage, (self.bgX2, self.bgY2))


main_menu()


pygame.quit()
