import pygame

FPS = 60

pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('ôûâ.MPG')
screen = pygame.display.set_mode((1024, 768))
movie_screen = pygame.Surface((1024, 768)).convert()

movie.set_display(movie_screen)
movie.play()


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()