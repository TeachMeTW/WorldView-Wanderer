import pygame
import sys
from button import Button
import os
import re
import PIL
import random
from background_selector import makeCountry, CountryMap

pygame.init()
pygame.mixer.init()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1280
screen_height = 720
country_dict = {0: 'Canada', 1: 'USA', 2: 'French', 3: 'Italy', 4: 'Korea', 5: 'Mexico', 6: 'Japan', 7: 'India'}
   

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordview Wanderer")
clock = pygame.time.Clock()
running = True
MUSIC_END = pygame.USEREVENT+1
CURRENT_SONG = 'Main-Menu'
CURRENT_LOC = 'Japan'

class Playlist:
    def __init__(self, dir):
        self.songs = []
        self.static_songs = []
        for s in os.listdir(dir):
            f = os.path.join(dir, s)
            if os.path.isfile(f):
                self.songs.append(f)
                self.static_songs.append(f)
                

    def play(self):
        if len(self.songs) > 0:
            pygame.mixer.music.load(self.songs[0])
            
            global CURRENT_SONG
            
            title = (self.songs[0]).replace('assets', '')
            title = title.replace('.wav', '')
            title = re.sub('\/.*?\/','', title)
            CURRENT_SONG = title
        
            self.songs.pop(0)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(MUSIC_END)
        else:
            for s in (self.static_songs):
                self.songs.append(s)
     
         
    def next_song(playlist):
        pass
    
    def pause():
        pygame.mixer.pause()
    
    def resume():
        pygame.mixer.unpause()

jp = Playlist('assets/Japan')
usa = Playlist('assets/USA')
fr = Playlist('assets/French')
ca = Playlist('assets/Canada')
mx = Playlist('assets/Mexico')
kr = Playlist('assets/Korea')
ity = Playlist('assets/Italy')
ind = Playlist('assets/India')



playlists = [jp,usa,fr]



def blurSurf(surface, amt):
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

images = ["countryimages/japan/mfuji.png", 
        "countryimages/japan/sushi dai.png", 
        "countryimages/japan/mtokyo tower.png",
        "countryimages/japan/imperial palace.png",
        "countryimages/japan/ichiran.png",
        "countryimages/japan/sensoji temple.png"
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
    
def get_font_cjk(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/cjk.ttf", size)


    
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

def visit(country_map):
    pygame.display.set_caption("Country Map")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    country_map.left()
                elif event.key == pygame.K_RIGHT:
                    country_map.right()
                elif event.key == pygame.K_ESCAPE:
                    running = False 

        screen.fill((255, 255, 255))
        country_map.display()
        screen.blit(left_selector, dest=(200, 540))
        screen.blit(right_selector, dest = (1000, 540))
        # screen.blit(current_text_index, dest=(900, 800))
        pygame.display.flip()

def startbackground():
    #bckgr = pygame.mixer.Sound('assets/jazz.wav')
    pygame.mixer.music.load('assets/jazz.wav')
    pygame.mixer.music.play()
    
def pause():
    pygame.mixer.music.pause()
    
def resume():
    pygame.mixer.music.unpause()
    
def change(dir):
    pygame.mixer.music.stop()
    if dir == 'Japan':
        jp.play()
    if dir == 'French':
        fr.play()
    if dir == 'Canada':
        ca.play()
    if dir == 'India':
        ind.play()
    if dir == 'Korea':
        kr.play()
    if dir == 'Mexico':
        mx.play()
    if dir == 'Italy':
        ity.play()
    if dir == 'USA':
        usa.play()
    pass



def main_menu():
    startbackground()
    P=0
    I = 0
    Flip = True
    BG = pygame.image.load("assets/lake.jpg")
    BG = pygame.transform.scale(BG, WINDOW_SIZE)
    BG  = blurSurf(BG, 10)
    
    MUTE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/volume.png'), (100,100)), pos=(50,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    TEST_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/mbut.png'), (100,100)), pos=(1100,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    
    
    while True:
        
        # SCREEN.blit(BG, (0,0))
        SCREEN.fill((0,0,0))
        SCREEN.blit(BG,(I,0))
        flipBG = pygame.transform.flip(BG, True, False)
        SCREEN.blit(flipBG,(WIDTH + I,0))
        if (I==-WIDTH):
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

        curr = f"NOW PLAYING: {CURRENT_SONG}"
        w = get_font_cjk(40)
        text = w.render(curr, True, 'white')
        length = text.get_size()
        
        NOW_PLAYING = Button(image=pygame.transform.scale(pygame.image.load("assets/Quit Rect.png"), (1.1*length[0], 1.1*length[1]) ), pos=(640, 650), 
            text_input=f"{curr}", font=get_font_cjk(40), base_color="#d7fcd4", hovering_color="White")


        for button in [VISIT_BUTTON, QUIT_BUTTON, TEST_BUTTON, MUTE_BUTTON, NOW_PLAYING]:
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
                    country_index = random.randint(0,7)
                    country_map = makeCountry(country_index)
                    change(country_dict[country_index])
                    visit(country_map)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MUTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if P==0:
                        MUTE_BUTTON.image = pygame.transform.scale(pygame.image.load('assets/muted.png'),(100,100))
                        MUTE_BUTTON.update(SCREEN)
                        pause()
                        P=1
                    else:
                        MUTE_BUTTON.image = pygame.transform.scale(pygame.image.load('assets/volume.png'),(100,100))
                        MUTE_BUTTON.update(SCREEN)
                        resume()
                        P=0
                if TEST_BUTTON.checkForInput(MENU_MOUSE_POS):
                    change(CURRENT_LOC)
                    
                    
            for p in playlists:
                    if event.type == MUSIC_END and len(p.songs) == 0:
                        p.play()


        pygame.display.update()

main_menu()


pygame.quit()
