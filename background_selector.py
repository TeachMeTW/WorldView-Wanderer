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

china_images = ["countryimages/china/forbidden_city.jpeg",
                "countryimages/china/great_wall.jpeg",
                "countryimages/china/quanjude.jpeg",
                "countryimages/china/summer_palace.jpeg",
                "countryimages/china/terracotta-army.jpg",
                "countryimages/china/south_beauty.jpeg"
                ]
american_food_images = ["food/american_food/lobster_rolls.jpg",
                        "food/american_food/ny_pizza.jpg",
                        "food/american_food/philly.jpg",
                        "food/american_food/tx_brisket.webp"]

canadian_food_images = ["food/canadian_food/bannock.jpg", 
                        "food/canadian_food/poutine.jpg",
                        "food/canadian_food/saskatoon_bpie.jpg",
                        "food/canadian_food/smoked_meats.jpg"]

chinese_food_images = ["food/chinese_food/bao_zi.jpg",
                       "food/chinese_food/dim_sum.webp",
                       "food/chinese_food/fried_rice.webp",
                       "food/chinese_food/peking_duck.webp"]

french_food_images = ["food/french_food/beef_bourguignon.webp",
                      "food/french_food/bouillabaisse.jpg",
                      "food/french_food/escargot.jpg.webp",
                      "food/french_food/french_onion.jpg.webp",
                      "food/french_food/ratatouille.jpg.webp"
                      ]

indian_food_images = ["food/indian_food/idli.webp",
                      "food/indian_food/palak_paneer.webp",
                      "food/indian_food/tandoori.webp",
                      "food/indian_food/tikka_masala.webp",
                      "food/indian_food/vindaloo.webp"]

italian_food_images = ["food/italian_food/bolognese.webp",
                       "food/italian_food/carbonara.webp",
                       "food/italian_food/fettuccine_alfredo.webp",
                       "food/italian_food/lasagna.webp",
                       "food/italian_food/stuffed_peppers.webp"]

japanese_food_images = ["food/japanese_food/Hambagu.webp",
                        "food/japanese_food/onigiri.webp",
                        "food/japanese_food/sushi.webp",
                        "food/japanese_food/takoyaki.webp",
                        "food/japanese_food/tempura.webp",
                        "food/japanese_food/tonkatsu.webp",
                        "food/japanese_food/yakitori.webp"]

korean_food_images = ["food/korean_food/bibimbap.webp",
                      "food/korean_food/bulgolgi.webp",
                      "food/korean_food/jiajiamian.jpg.webp",
                      "food/korean_food/kfc.webp",
                      "food/korean_food/kimchi.webp",
                      "food/korean_food/teokboki.webp"]

mexican_food_images = ["food/mexican_food/birri_taco.jpg",
                       "food/mexican_food/churro.jpg",
                       "food/mexican_food/enchilada.jpg",
                       "food/mexican_food/huevo_ranchero.jpg",
                       "food/mexican_food/tamale.jpg",
                       "food/mexican_food/tostada.jpg"]


def food_images(country_name):
    country_dict = {"usa": american_food_images, "canada": canadian_food_images, "china": chinese_food_images, "france": french_food_images, "india": indian_food_images, "italy": italian_food_images,
                    "japan": japanese_food_images, "korea": korean_food_images, "mexico": mexican_food_images}
    return country_dict[country_name]

def get_country_name(country_index):
    country_dict = {0: "usa", 1: "canada", 2: "china", 3: "france", 4: "india", 5: "italy", 6: "japan", 7: "korea", 8: "mexico"}
    return country_dict[country_index]

def makeCountry(country_index):
    country_dict = {0: images_usa, 1: canada_images, 2: china_images, 3: images_france, 4: india_images, 5: images_italy, 6: japan_images, 7: images_korea, 8: images_mexico}
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
       
        self.index = 0

    def left(self):
        if self.index < len(self.img)-1:
            self.index+=1
            current_image = pygame.image.load(self.img[self.index]).convert().convert_alpha()
            
    def right(self):
        if self.index > 0:
            self.index -= 1
            current_image = pygame.image.load(self.img[self.index]).convert().convert_alpha()
            

    def display(self):
        current_image = pygame.image.load(self.img[self.index])
        current_image = pygame.transform.scale(current_image, (500,500))
        image_rect = current_image.get_rect()    
        image_rect.center = (screen_width/2, screen_height/2)
        return current_image




