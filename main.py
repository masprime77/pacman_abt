import math
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

#Other constants
PI = math.pi

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
        mouth_angle = PI / 4  # 45 degrees
        direction = 0
        semi_circle_precision = 25  # Number of points to draw the mouth

        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius)

        if self.dx == 0 and self.dy == 0:
            pass
        else:
            if self.dx > 0:
                direction = 0
            elif self.dx < 0:
                direction = PI
            elif self.dy > 0:
                direction = 0.5 * PI
            elif self.dy < 0:
                direction = 1.5 * PI

            start_angle = direction + mouth_angle
            end_angle = direction - mouth_angle        

            points = [(self.x, self.y)]
            
            for angle in range(semi_circle_precision):
                theta = start_angle + angle * (end_angle - start_angle) / semi_circle_precision
                x = self.x + self.radius * math.cos(theta)
                y = self.y + self.radius * math.sin(theta)
                points.append((x, y))

            pygame.draw.polygon(surface, BLACK, points)


class Heart:
    def __init__(self, x, y, radius=15):
        self.x = x
        self.y = y
        self.radius = radius
        self.found = False

    def draw(self, surface):
        if not self.found:
            pygame.draw.circle(surface, (255, 0, 100), (self.x, self.y), self.radius)
            pygame.draw.circle(surface, (255, 0, 100), (self.x + self.radius * 1.5, self.y), self.radius)
            pygame.draw.polygon(surface, (255, 0, 100), [
                (self.x - self.radius, self.y + 4.95),
                (self.x + self.radius * 2.5, self.y + 4.95),
                (self.x + self.radius * 0.75, self.y + self.radius * 1.75),
            ])

        
    def is_colliding(self, pacman):
        distance = math.hypot(self.x - pacman.x, self.y - pacman.y)

        return distance < self.radius + pacman.radius


#Initialize Pac-Man
pacman = Pacman(WIDTH // 2, HEIGHT // 2)

# Initialize Heart
heart = Heart(WIDTH - 50, 40)

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
    heart.draw(screen)

    heart.draw(screen)

    if heart.is_colliding(pacman):
        screen.fill(BLACK)
        heart.found = True
        font = pygame.font.SysFont(None, 36)
        text = font.render("Te amo mucho princesa! Felices 4 meses <3", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    else:
        heart.found = False

    pygame.display.flip()

pygame.quit()
sys.exit()
