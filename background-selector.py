import pygame

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1920
screen_height = 1080

pygame.init()
current_image_index = 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Selector")
images_japan = ["countryimages\\japan\\mfuji.png"]
left_selector = pygame.image.load("left-arrow-png-left-icon-1600-2971489872.png").convert_alpha()
right_selector = pygame.image.load("KTjAXb7Tq-2709733076.png").convert_alpha()

left_selector = pygame.transform.scale(left_selector, [selector_width, selector_height])
right_selector = pygame.transform.scale(right_selector, [selector_width, selector_height])
current_image = pygame.image.load(images_japan[current_image_index]).convert_alpha()


image_position = (screen_width // 2 - current_image.get_width() // 2, screen_height // 2 - current_image.get_height() // 2)

class japanMap():
    images_japan = ["countryimages\\japan\\mfuji.png", 
        "countryimages\\japan\\sushi dai.png", 
        "countryimages\\japan\\mtokyo tower.png",
        "countryimages\\japan\\imperial palace.png",
        "countryimages\\japan\\ichiran.png",
        "countryimages\\japan\\sensoji temple.png"
        ]
    current_image = pygame.image.load(images_japan[current_image_index]).convert().convert_alpha()
    current_image = pygame.transform.scale(current_image, [500, 500])
    def next_image():
        global current_image_index, current_image, images_japan
        current_image_index = (current_image_index + 1) % len(images_japan)
        current_image = pygame.image.load(images_japan[current_image_index]).convert().convert_alpha()
        current_image = pygame.transform.scale(current_image, [500, 500])

    def previous_image():
        global current_image_index, current_image, current_text_index
        current_image_index = (current_image_index - 1) % len(images_japan)
        current_image = pygame.image.load(images_japan[current_image_index]).convert().convert_alpha()
        current_image = pygame.transform.scale(current_image, [500, 500])
        display_current_image()

class canadaMap():
    images_canada = [
        "countryimages\\canada\\malo.png",
        "countryimages\\canada\\Chateau_Frotenac.png",
        "countryimages\\canada\\CN_tower.png",
        "countryimages\\canada\\Niagara Falls.png",
        "countryimages\\canada\\Poutineville.png",
        "countryimages\\canada\\Stanley Park.png",
        ]
class usaMap():
    images_usa = [
        "countryimages\\usa\\GGB.png",
        "countryimages\\usa\\gateway.png",
        "countryimages\\usa\\in out.png",
        "countryimages\\usa\\katz.png",
        "countryimages\\usa\\rushmore.png",
        "countryimages\\usa\\yellowstone.png",
        ]

class franceMap():
    images_france = [
        "countryimages\\france\\arc de trimophe.png",
        "countryimages\\france\\comptoir.png",
        "countryimages\\france\\eiffel.png",
        "countryimages\\france\\notre dame.png",
        "countryimages\\france\\tour.png",
        "countryimages\\france\\versailles.png"  
        ]

class italyMap(): 
    images_italy = [
        "countryimages\\italy\\coloseeum.png",
        "countryimages\\italy\\duomo.png",
        "countryimages\\italy\\enzo.png",
        "countryimages\\italy\\Osteria.png",
        "countryimages\\italy\\pisa.png"
        "countryimages\\italy\\cinque.png"
    ]

class koreaMap():
    images_korea = [
        "countryimages\\korea\\gwanghwaum.png",
        "countryimages\\korea\\gwangjang.png",
        "countrymages\\korea\\jeju.png",
        "countryimages\\korea\\kyoja.png",
        "countryimages\\korea\\namsan.png",
        "countryimages\\korea\\palace.png"
        ]
class mexicoMap(): 
        images_mexico = [
            "countryimages\\mexico\\Cancun.png",
            "countryimages\\mexico\\Chichen Itza.png",
            "countryimages\\mexico\\La-Carnita.png",
            "countryimages\\mexico\\Palacio-De-Bellas-Artes.png",
            "countryimages\\mexico\\Pujol.png",
            "countryimages\\mexico\\Teotihuacan-022.jpg"
        ]

images = ["country images\\japan\\mfuji.png", 
          "country images\\japan\\sushi dai.png", 
          "country images\\japan\\mtokyo tower.png",
          "country images\\japan\\imperial palace.png",
          "country images\\japan\\ichiran.png",
          "country images\\japan\\sensoji temple.png"
          ]

image_data = [("Picture 1", (0, 0, 0)),   
              ("Picture 2", (255, 0, 0)),
              ("Picture 3", (0, 255, 0))]

current_image_index = 0





def display_current_image():
    screen.blit(current_image, image_position)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                japanMap.previous_image()
            elif event.key == pygame.K_RIGHT:
                japanMap.next_image()
            elif event.key == pygame.K_ESCAPE:
                running = False 

    screen.fill((255, 255, 255))
    display_current_image()
    screen.blit(left_selector, dest=(400, 540))
    screen.blit(right_selector, dest = (1400, 540))
    # screen.blit(current_text_index, dest=(900, 800))
    pygame.display.flip()

pygame.quit()
