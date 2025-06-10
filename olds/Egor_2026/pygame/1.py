import pygame #библиотека pygame
pygame.init() #инициализируем игру
W = 600
H = 400
sc = pygame.display.set_mode((W, H)) #открываем окно 600x400
pygame.display.set_caption("Моя первая игра в PyGame")
#pygame.display.set_icon(pygame.image.load(r"C:\Users\Zarif\Downloads\game_icon_155348.png"))


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x = W // 2
y = H // 2
speed = 5

FPS = 60
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 20, 40))
    pygame.display.update()
    clock.tick(FPS)
