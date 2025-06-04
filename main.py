import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

class Pacman:
    def __init__(self, x, y, radius=20, speed=3):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.dx = 0
        self.dy = 0

    def move_keys(self):
        keys = pygame.key.get_pressed()
        self.dx, self.dy = 0, 0
        if keys[pygame.K_LEFT]:
            self.dx = -self.speed
        if keys[pygame.K_RIGHT]:
            self.dx = self.speed
        if keys[pygame.K_UP]:
            self.dy = -self.speed
        if keys[pygame.K_DOWN]:
            self.dy = self.speed

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Keep Pac-Man within the screen bounds
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (self.x, self.y), self.radius)

#Initialize Pac-Man
pacman = Pacman(WIDTH // 2, HEIGHT // 2)

# Main game loop
runinng = True
while runinng:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runinng = False
    
    pacman.move_keys()
    pacman.move()

    screen.fill(BLACK)
    pacman.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
