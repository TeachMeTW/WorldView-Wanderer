import pygame
import sys
from button import Button
import os

pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordview Wanderer")
BG = pygame.image.load("assets/background.jpg")
clock = pygame.time.Clock()
running = True
MUSIC_END = pygame.USEREVENT+1


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
        print(self.static_songs)
        if len(self.songs) > 0:
            pygame.mixer.music.load(self.songs[0])
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

playlists = [jp,usa,fr]



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def search():
    return

def startbackground():
    #bckgr = pygame.mixer.Sound('assets/jazz.wav')
    pygame.mixer.music.load('assets/jazz.wav')
    pygame.mixer.music.play()
    
def pause():
    pygame.mixer.music.pause()
    
def resume():
    pygame.mixer.music.unpause()
    
# When changing countries, change the music.    
def change(dir):
    pygame.mixer.music.stop()
    if dir == 'Japan':
        jp.play()
    if dir == 'French':
        fr.play()
    pass




def main_menu():
   
    
    startbackground()
    P=0
    currentlocation = 'French'
    
    SEARCH_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Search for a Country", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    # FInally works bruv
    MUTE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/volume.png'), (100,100)), pos=(50,670),  text_input="", font=get_font(0), base_color="#d7fcd4", hovering_color="White")
    TEST_BUTTON = Button(image=pygame.transform.scale(pygame.image.load('assets/mbut.png'), (100,100)), pos=(1100,670),  text_input="", font=get_font(0), base_color="#d7fcd4", hovering_color="White")

    
    while True:
        
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Worldview Wanderer", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [SEARCH_BUTTON, QUIT_BUTTON, MUTE_BUTTON, TEST_BUTTON]:
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
                    change(currentlocation)
                    
            for p in playlists:
                    if event.type == MUSIC_END and len(p.songs) == 0:
                        p.play()

                    
                            
                
                    
                    

        pygame.display.update()

main_menu()
pygame.quit()
