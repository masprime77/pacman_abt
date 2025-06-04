import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, (0, 0, 0), [(400, 300), (420, 280), (440, 300), (420, 320)])
    pygame.display.flip()