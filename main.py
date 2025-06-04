import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mini Pac-Man")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (320, 240), 20)  # Draw Pac-Man
    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
