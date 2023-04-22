import pygame
import sys
from button import Button


pygame.init()
pygame.mixer.init()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1280
screen_height = 720


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
screen = pygame.display.set_mode((screen_width, screen_height))

left_selector = pygame.image.load("left-arrow-png-left-icon-1600-2971489872.png").convert_alpha()
right_selector = pygame.image.load("KTjAXb7Tq-2709733076.png").convert_alpha()

left_selector = pygame.transform.scale(left_selector, [selector_width, selector_height])
right_selector = pygame.transform.scale(right_selector, [selector_width, selector_height])

images = ["country images/japan/mfuji.png", 
        "country images/japan/sushi dai.png", 
        "country images/japan/mtokyo tower.png",
        "country images/japan/imperial palace.png",
        "country images/japan/ichiran.png",
        "country images/japan/sensoji temple.png"
        ]

image_data = [("Picture 1", (0, 0, 0)),   
            ("Picture 2", (255, 0, 0)),
            ("Picture 3", (0, 255, 0))]

current_image_index = 0
current_text_index = 0

current_image = pygame.image.load(images[current_image_index]).convert().convert_alpha()
current_image = pygame.transform.scale(current_image, [500, 500])
current_text_index = my_font.render('Cute Cat', False, (0, 0, 0))

image_position = (screen_width // 2 - current_image.get_width() // 2, screen_height // 2 - current_image.get_height() // 2)


def get_font(size, type): # Returns Press-Start-2P in the desired size
    if type == DBZ:
        return pygame.font.Font("assets/dbz.ttf", size)
    elif type == MC:
        return pygame.font.Font("assets/mc.otf", size)
    
def display_current_image():
    screen.blit(current_image, image_position)


def next_image():
    global current_image_index, current_image, current_text_index
    current_image_index = (current_image_index + 1) % len(images)
    #current_text_index = (current_text_index + 1) % len(image_data)
    current_image = pygame.image.load(images[current_image_index]).convert().convert_alpha()
    current_image = pygame.transform.scale(current_image, [500, 500])
    #current_text_index = my_font.render(image_data[current_text_index], False, image_data[current_text_index][1])
    display_current_image()

def previous_image():
    global current_image_index, current_image, current_text_index
    current_image_index = (current_image_index - 1) % len(images)
    # current_text_index = (current_text_index - 1) % len(image_data)
    current_image = pygame.image.load(images[current_image_index]).convert().convert_alpha()
    current_image = pygame.transform.scale(current_image, [500, 500])
    #current_text_index = my_font.render(image_data[current_text_index], False, image_data[current_text_index][1])
    display_current_image()

def visit():
    pygame.display.set_caption("Image Selector")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    previous_image()
                elif event.key == pygame.K_RIGHT:
                    next_image()
                elif event.key == pygame.K_ESCAPE:
                    running = False 

        screen.fill((255, 255, 255))
        display_current_image()
        screen.blit(left_selector, dest=(400, 540))
        screen.blit(right_selector, dest = (1400, 540))
        # screen.blit(current_text_index, dest=(900, 800))
        pygame.display.flip()

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
                    visit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


pygame.quit()
