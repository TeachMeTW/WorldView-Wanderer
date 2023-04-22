import pygame as pg
import random
import datetime

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
    time_surface = font.render(time_str, True, (0, 0, 0))
    return time_surface

pg.init()
clock = pg.time.Clock()

window_size = (1280, 720)
screen = pg.display.set_mode(window_size)

font = pg.font.Font("assets/font.ttf", 40)

COLOR_ACTIVE = (148, 208, 242)
COLOR_INACTIVE = (16, 109, 163)
COLOR_LIST_INACTIVE = (98, 156, 102)
COLOR_LIST_ACTIVE = (37, 94, 150)

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    30, 30, 200, 40, 
    font,
    "Select Country", ["Canada", "China", "France", "Germany", "India", "Italy", "Japan", "Mexico", "South Korea","USA"])

#timezone dictionary 
timezone_dict = {0:0,"Canada": 3, "China":15, "France":9, "Germany": 9, 
                 "India":12.5, "Italy":9, "Japan":16, "Mexico":1, 
                 "South Korea":16, "USA":3}
run = True
temp = 0
while run:
    clock.tick(30)

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False

    
    selected_option = list1.update(event_list)

    if str(selected_option) != '-1':
        list1.main = 'Select Country' 
        temp = selected_option   
    else:
        list1.draw(screen)
        pg.display.flip()
        
        #continue


    screen.fill((255, 255, 255))
    clock_surface = render_pst_clock(font, -7+(timezone_dict[temp]))
    screen.blit(clock_surface, (screen.get_width() - clock_surface.get_width() - 30, 30))

    #else:
    #screen.blit(render_pst_clock(font, -7), (screen.get_width() - clock_surface.get_width() - 15, 15))


    list1.draw(screen)
    pg.display.flip()
    
pg.quit()
exit()
