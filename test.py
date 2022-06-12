import pygame

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chimp_simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPEED = [2, 2]
radius = 10
FPS = 60


# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()
    # This line says "Draw surf onto the screen at the center"
    WIN.blit(surf, (WIDTH / 2, HEIGHT / 2))
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()