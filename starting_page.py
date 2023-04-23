import pygame
import sys
from button import Button
import os
import re
import PIL
import random
from background_selector import makeCountry, get_country_name, food_images, get_text, CountryMap
from drop_down import *


selector_width = 100
selector_height = 100
screen_width = 1280
screen_height = 720
country_dict = {0: "usa", 1: "canada", 2: "china", 3: "france", 4: "india", 5: "italy", 6: "japan", 7: "korea", 8: "mexico"}
   


running = True
MUSIC_END = pygame.USEREVENT+1
CURRENT_SONG = ' '
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
fr = Playlist('assets/France')
ca = Playlist('assets/Canada')
mx = Playlist('assets/Mexico')
kr = Playlist('assets/Korea')
ity = Playlist('assets/Italy')
ind = Playlist('assets/India')
ch = Playlist('assets/China')


playlists = [jp,usa,fr, ca, mx,kr,ity,ind,ch]



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
    
def get_font_cjk(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/cjk.ttf", size)



def visit(country_map, country):
    
    country_dict = {0: "usa", 1: "canada", 2: "china", 3: "france", 4: "india", 5: "italy", 6: "japan", 7: "korea", 8: "mexico"}
    country_dict2 = { country_dict[k]:k for k in country_dict}
    
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    FOOD_BUTTON = Button(image = None, pos=(200, 525), 
        text_input="Cuisine of this Country", font=get_font(30, MC), base_color="black", hovering_color="blue", scale = .2)
   
    clock = pg.time.Clock()

    window_size = (1280, 720)
    screen = pg.display.set_mode(window_size)
    font = pg.font.Font("assets/font.ttf", 45)
    font_date = pg.font.Font("assets/font.ttf", 40)

    COLOR_ACTIVE = (148, 208, 242)
    COLOR_INACTIVE = (16, 109, 163)
    COLOR_LIST_INACTIVE = (98, 156, 102)
    COLOR_LIST_ACTIVE = (108, 186, 122)




    list1 = DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        30, 30, 200, 40, 
        font,
        "Select Destination", ["canada", "china", "france", "india", "italy", "japan", "mexico", "korea","usa"])

    #timezone dictionary 
    timezone_dict = {0:0,"canada": 3, "china":15, "france":9, "germany": 9, 
                 "india":12.5, "italy":9, "japan":16, "mexico":1, 
                 "korea":16, "usa":3}

    date_timezone_dict={0:"America/Los_Angeles","japan":"Asia/Tokyo", "india":"Asia/Calcutta", "china":"Asia/Chongqing", "france":"Europe/Paris", "germany":"Europe/Paris", 
                    "italy":"Europe/Paris", "canada":"Canada/Atlantic", "mexico":"America/Mexico_City", "korea":"Asia/Seoul", "usa":"America/Fort_Wayne"}
    
    CURRENT_LOC = country
    change(CURRENT_LOC)
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Wordview Wanderer")
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((screen_width, screen_height))

    left_selector = pygame.image.load("left-arrow-png-left-icon-1600-2971489872.png").convert_alpha()
    right_selector = pygame.image.load("KTjAXb7Tq-2709733076.png").convert_alpha()

    left_selector = pygame.transform.scale(left_selector, [selector_width, selector_height])
    right_selector = pygame.transform.scale(right_selector, [selector_width, selector_height])


    pygame.display.set_caption("Country Map")
    screen.fill((255, 255, 255))
    P=0
    I = 0
    running = True
    MUTE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/volume.png'), (100,100)), pos=(50,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    TEST_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/mbut.png'), (100,100)), pos=(1230,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    #print('here')
    screen.blit(left_selector, dest=(200, 540))
    screen.blit(right_selector, dest = (1000, 540))
    #country_map.display()
    #print(country_map.img)
    food_counter = 0
    valid_dish = None
    while running:
        img = country_map.display()
        screen.fill((255, 255, 255))
        screen.blit(img,(400, 60))
        current_text = get_text(country, country_map.get_index())
        print("country: " + str(country))
        print("get index: " + str(country_map.get_index()))
        print("current text: " + str(current_text))
        TEXT_BUTTON = Button(image=None, pos=(700,600),  text_input=current_text, font=get_font(50, MC), base_color="black", hovering_color="black")
        if valid_dish is not None:
            screen.blit(valid_dish, (30, 200))

        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        curr = f"NOW PLAYING: {CURRENT_SONG}"
        w = get_font_cjk(40)
        text = w.render(curr, True, 'black')
        length = text.get_size()
        NOW_PLAYING = Button(image=pygame.transform.scale(pygame.image.load("assets/Quit Rect.png"), (1.1*length[0], 1.1*length[1]) ), pos=(640, 650), 
            text_input=f"{curr}", font=get_font_cjk(40), base_color="#d7fcd4", hovering_color="White")


   
        
        #pygame.display.update()
        for button in [TEST_BUTTON, MUTE_BUTTON, NOW_PLAYING, FOOD_BUTTON, TEXT_BUTTON]:
            # if button is VISIT_BUTTON:
            #     color = "black"
            #     pygame.draw.rect(SCREEN, color, pygame.Rect(470, 365, 350, 60))
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        #pygame.display.update()
        list1.draw(screen)
                #pg.display.flip()
                
                #continue

            #pygame.display.update()
            #screen.fill((255, 255, 255))
        clock_surface = render_pst_clock(font, -7+(timezone_dict[country]))
        date_surface = render_date(font_date, date_timezone_dict[country])
        screen.blit(date_surface, (1110, 80))
        screen.blit(clock_surface, (screen.get_width() - clock_surface.get_width() - 30, 30))
        eventlist = pygame.event.get()    
        for event in eventlist:
            
            selected_option = list1.update(eventlist)
            
            if str(selected_option) != '-1':
                pg.init()
                
                list1.main = 'Select Destination' 
                temp = selected_option
                #pygame.display.update()
                country_map.img.clear()
                country_map.img=0
                cindex=(country_dict2[temp])
                print(cindex)
                cmap = makeCountry(cindex)
                print(cmap.img)
                visit(cmap,temp)
                temp = selected_option
                continue
            
            
            #pygame.display.update()
            
            
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    country_map.left()
                    country_map.display()
                if event.key == pygame.K_RIGHT:
                    country_map.right()
                    country_map.display()
                if event.key == pygame.K_ESCAPE:
                    running = False 
                #pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                if FOOD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    food_pics = food_images(country)
                    current_dish = pygame.image.load(food_pics[food_counter]).convert_alpha()
                    current_dish = pygame.transform.scale(current_dish, [250, 250])
                    valid_dish = current_dish
                    #screen.blit(current_dish, dest = (1000, 300))
                    if food_counter == len(food_pics) - 1:
                        food_counter = 0
                    else:
                        food_counter += 1
                #pygame.display.update()
                    
                    
            for p in playlists:
                #pygame.display.update()
                if event.type == MUSIC_END and len(p.songs) == 0:
                    p.play()
                        
            pygame.display.update()
        
        
        pygame.display.update()
        # screen.blit(current_text_index, dest=(900, 800))
    pygame.display.update()
    country_map.img.clear()
    country_map.img=0
    return

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
    if dir == 'japan':
        jp.play()
    if dir == 'france':
        fr.play()
    if dir == 'canada':
        ca.play()
    if dir == 'india':
        ind.play()
    if dir == 'korea':
        kr.play()
    if dir == 'mexico':
        mx.play()
    if dir == 'italy':
        ity.play()
    if dir == 'usa':
        usa.play()
    if dir == 'china':
        ch.play()
    pass


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Wordview Wanderer")
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    BG = pygame.image.load("assets/lake.jpg")
    BG = pygame.transform.scale(BG, WINDOW_SIZE)
    BG  = blurSurf(BG, 10)
    pygame.init()
    pygame.mixer.init()

    pygame.font.init()
    startbackground()
    P=0
    I = 0
    Flip = True
    BG = pygame.image.load("assets/lake.jpg")
    BG = pygame.transform.scale(BG, WINDOW_SIZE)
    BG  = blurSurf(BG, 10)
    
    MUTE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/volume.png'), (100,100)), pos=(50,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    TEST_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/mbut.png'), (100,100)), pos=(1230,670),  text_input="", font=get_font(0, MC), base_color="#d7fcd4", hovering_color="White")
    
    
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
                    country_index = random.randint(0,8)
                    country_map = makeCountry(country_index)
                    global CURRENT_LOC
                    CURRENT_LOC = country_dict[country_index]
                    change(country_dict[country_index])
                    visit(country_map, country_dict[country_index])
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
                if MUTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if P==1:
                        MUTE_BUTTON.image = pygame.transform.scale(pygame.image.load('assets/muted.png'),(100,100))
                        MUTE_BUTTON.update(SCREEN)
                        pause()
                        P=0
                    else:
                        MUTE_BUTTON.image = pygame.transform.scale(pygame.image.load('assets/volume.png'),(100,100))
                        MUTE_BUTTON.update(SCREEN)
                        resume()
                        P=1
                if TEST_BUTTON.checkForInput(MENU_MOUSE_POS):
                    change(CURRENT_LOC)
                    
                    
            for p in playlists:
                    if event.type == MUSIC_END and len(p.songs) == 0:
                        p.play()


        pygame.display.update()

if __name__ == "__main__":
    
    print(__name__)
    main()

else:
    pygame.quit()