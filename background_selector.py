import pygame

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1920
screen_height = 1080

current_image_index = 0
screen = pygame.display.set_mode((screen_width, screen_height))


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
            #screen.blit(current_image, (100,100))
        #return current_image
    def right(self):
        if self.index > 0:
            self.index -= 1
            current_image = pygame.image.load(self.img[self.index]).convert().convert_alpha()
            #screen.blit(current_image, (100, 100))
        #return current_image

    def display(self):
        current_image = pygame.image.load(self.img[self.index])
        current_image = pygame.transform.scale(current_image, (500,500))
        image_rect = current_image.get_rect()    
        image_rect.center = (960, 540)
        #screen.blit(current_image, (400, 150))
        return current_image



