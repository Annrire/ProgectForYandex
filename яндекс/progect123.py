import pygame
from moviepy.editor import VideoFileClip 
pygame.init()

clip = VideoFileClip('66918_movie.mp4')
clip_resized = clip.resize((1024, 768))
clip_resized.preview()

pygame.display.set_caption('Добро пожаловать в игру!') 
sc = pygame.display.set_mode((1024, 768))
sc.fill((255, 0, 0))
background_position = [0, 0]
background_image = pygame.image.load("начало.gif").convert()
sc.blit(background_image, background_position)
y1 = 0
x1 = 0
pygame.display.update()
running = True
start = False
record = False
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
        background_position = [0, 0]
        background_image = pygame.image.load("начало.gif").convert()
        sc.blit(background_image, background_position)
    #if y <= 314 and y >= 199 тогда старт
        if y1 <= 451 and y1 >= 330:
            record = True 
            running = False
        if y1 <= 577 and y1 >= 459:
            running = False
            game = False
        if start:        
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        
        pygame.display.flip()
 
    while record: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos        
                start = True
                image = pygame.image.load("arrow.png").convert_alpha()
                sc.blit(background_image, background_position)
                pygame.mouse.set_visible(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
        if x1 >= 425 and x1 <= 556 and y1 <= 700 and y1 >= 666:
            running = True        
            record = False 
        
        background_position = [0, 0]
        background_image = pygame.image.load("рекорды.gif").convert()
        sc.blit(background_image, background_position)
        if start:        
            dr1 = image.get_rect(bottomright=(x + 44, y + 40))
            sc.blit(image, dr1)
        pygame.display.flip()
pygame.quit()