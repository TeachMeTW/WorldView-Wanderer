import pygame

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1920
screen_height = 1080

# pygame.init()
current_image_index = 0
screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Image Selector")

# left_selector = pygame.image.load("left-arrow-png-left-icon-1600-2971489872.png").convert_alpha()
# right_selector = pygame.image.load("KTjAXb7Tq-2709733076.png").convert_alpha()

# left_selector = pygame.transform.scale(left_selector, [selector_width, selector_height])
# right_selector = pygame.transform.scale(right_selector, [selector_width, selector_height])

canada_images = [
            "countryimages/canada/malo.png",
            "countryimages/canada/Chateau_Frotenac.png",
            "countryimages/canada/CN_tower.png",
            "countryimages/canada/Niagara Falls.png",
            "countryimages/canada/Poutineville.png",
            "countryimages/canada/Stanley Park.png",
        ]

canada_data = [
    "Alo Restaurant",
    "Chateau Frotenac",
    "CN Tower",
    "Niagara Falls",
    "Poutineville Restaurant",
    "Stanley Park"
]
images_usa = [
    "countryimages/usa/GGB.png",
    "countryimages/usa/gateway.png",
    "countryimages/usa/in out.png",
    "countryimages/usa/katz.png",
    "countryimages/usa/rushmore.png",
    "countryimages/usa/yellowstone.png",
    ]


images_france = [
    "countryimages/france/arc de trimophe.png",
    "countryimages/france/comptoir.png",
    "countryimages/france/eiffel.png",
    "countryimages/france/notre dame.png",
    "countryimages/france/tour.png",
    "countryimages/france/versailles.png"  
    ]


images_italy = [
    "countryimages/italy/coloseeum.png",
    "countryimages/italy/duomo.png",
    "countryimages/italy/enzo.png",
    "countryimages/italy/Osteria.png",
    "countryimages/italy/pisa.png"
    "countryimages/italy/cinque.png"
]


images_korea = [
    "countryimages/korea/gwanghwaum.png",
    "countryimages/korea/gwangjang.png",
    "countryimages/korea/jeju.png",
    "countryimages/korea/kyoja.png",
    "countryimages/korea/namsan.png",
    "countryimages/korea/palace.png"
    ]

images_mexico = [
    "countryimages/mexico/Cancun.png",
    "countryimages/mexico/Chichen Itza.png",
    "countryimages/mexico/La-Carnita.png",
    "countryimages/mexico/Palacio-De-Bellas-Artes.png",
    "countryimages/mexico/Pujol.png",
    "countryimages/mexico/Teotihuacan-022.jpg"
]

japan_images = ["countryimages/japan/mfuji.png", 
          "countryimages/japan/sushi dai.png", 
          "countryimages/japan/mtokyo tower.png",
          "countryimages/japan/imperial palace.png",
          "countryimages/japan/ichiran.png",
          "countryimages/japan/sensoji temple.png"
          ]

india_images = ["countryimages/india/bukhara.png",
                "countryimages/india/gateway of india.png",
                "countryimages/india/india gate.png",
                "countryimages/india/karim.png",
                "countryimages/india/red fort.png",
                "countryimages/india/taj mahal.png"]

def makeCountry(country_index):
    country_dict = {0: canada_images, 1: images_usa, 2: images_france, 3: images_italy, 4: images_korea, 5: images_mexico, 6: japan_images, 7: india_images}
    chosen_country = country_dict[country_index]
    countryMap = CountryMap(chosen_country)
    return countryMap

class CountryMap():
    index = 0
    img = []
    data = []
    def __init__(self, image_list):

        for i in image_list:
            self.img.append(i)
        # for x in data_list:
        #     self.data.append(i)
        self.index = 0
        
    def left(self):
        if self.index < len(self.img)-1:
            self.index+=1
            current_image = pygame.image.load(self.img[self.index]).convert().convert_alpha()
            screen.blit(current_image, (100,100))
    def right(self):
        if self.index > 0:
            self.index -= 1
            current_image = pygame.image.load(self.img[self.index]).convert().convert_alpha()
            screen.blit(current_image, (100, 100))

    def display(self):
        current_image = pygame.image.load(self.img[self.index])
        current_image = pygame.transform.scale(current_image, (500,500))
        image_rect = current_image.get_rect()    
        image_rect.center = (640, 360)
        screen.blit(current_image, (400, 150))
    
    # def renderText(self):
    #     font = pygame.font.Font(None, 36)
    #     self.index += 1
    #     text_render = font.render(self.data, True, (255,255,255))
    #     text_rect = text_render.get_rect()
    #     text_rect.center = (400, 670)
    #     screen.blit(text_render, text_rect)
    #     pygame.display.update() 


image_data = [("Picture 1", (0, 0, 0)),   
              ("Picture 2", (255, 0, 0)),
              ("Picture 3", (0, 255, 0))]


# canmap = CountryMap(canada_images)




# running = True


# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 canmap.left()
#             elif event.key == pygame.K_RIGHT:
#                 canmap.right()
#             elif event.key == pygame.K_ESCAPE:
#                 running = False 

#     screen.fill((255, 255, 255))
#     canmap.display()
#     screen.blit(left_selector, dest=(400, 540))
#     screen.blit(right_selector, dest = (1400, 540))
#     # screen.blit(current_text_index, dest=(900, 800))
#     pygame.display.flip()

# pygame.quit()
