import pygame as pg
import random
import datetime
import pytz
from starting_page import *
from background_selector import makeCountry, CountryMap

pg.font.init()
country_dict = {0: "usa", 1: "canada", 2: "china", 3: "france", 4: "india", 5: "italy", 6: "japan", 7: "korea", 8: "mexico"}
country_dict2 = { country_dict[k]:k for k in country_dict}
class DropDown():

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pg.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.display_options = []

    def draw(self, surf):
        pg.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.display_options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pg.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pg.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.display_options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.display_options = random.sample(self.options, 3)
                    

                    self.draw_menu = True
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.display_options[self.active_option]
        return -1


def render_pst_clock(font, st):
    pst = datetime.timezone(datetime.timedelta(hours= st))
    now = datetime.datetime.now(pst)
    time_str = now.strftime('%I:%M:%S %p')
    time_surface = font.render('Local Country Time: '+time_str, True, (0, 0, 0))
    return time_surface

def render_date(font, timezone):
    date = datetime.datetime.now(pytz.timezone(timezone))
    my_date = (str(date)).split()
    my_date = my_date[0].split('-')
    date_str = datetime.date(day=int(my_date[2]), month=int(my_date[1]), year=int(my_date[0])).strftime('%B %d, %Y')
    date_surface = font.render(date_str, True, (0, 0, 0))
    return date_surface


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
    "Select Destination", ["Canada", "China", "France", "India", "Italy", "Japan", "Mexico", "Korea","USA"])

#timezone dictionary 
timezone_dict = {0:0,"Canada": 3, "China":15, "France":9, "Germany": 9, 
                 "India":12.5, "Italy":9, "Japan":16, "Mexico":1, 
                 "Korea":16, "USA":3}

date_timezone_dict={0:"America/Los_Angeles","Japan":"Asia/Tokyo", "India":"Asia/Calcutta", "China":"Asia/Chongqing", "France":"Europe/Paris", "Germany":"Europe/Paris", 
                    "Italy":"Europe/Paris", "Canada":"Canada/Atlantic", "Mexico":"America/Mexico_City", "Korea":"Asia/Seoul", "USA":"America/Fort_Wayne"}
def main():
    pg.init()
    run = True
    temp = 0
    while run:
        clock.tick(30)

        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                pg.quit()
                run = False

        
        selected_option = list1.update(event_list)

        if str(selected_option) != '-1':
            pg.init()
            list1.main = 'Select Destination' 
            temp = selected_option
            cindex=(country_dict2[temp])
            print(cindex)
            cmap = makeCountry(cindex)
            print(cmap.img)
            visit(cmap,temp)
            
            continue
        else:
            list1.draw(screen)
            pg.display.flip()
            
            #continue


        screen.fill((255, 255, 255))
        clock_surface = render_pst_clock(font, -7+(timezone_dict[temp]))
        date_surface = render_date(font_date, date_timezone_dict[temp])
        screen.blit(date_surface, (1110, 80))
        screen.blit(clock_surface, (screen.get_width() - clock_surface.get_width() - 30, 30))

        #else:
        #screen.blit(render_pst_clock(font, -7), (screen.get_width() - clock_surface.get_width() - 15, 15))


        list1.draw(screen)
        pg.display.flip()
        



if __name__ == "__main__":
    main()