import pygame
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selector_width = 100
selector_height = 100
screen_width = 1920
screen_height = 1080

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Selector")

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

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

pygame.quit()
