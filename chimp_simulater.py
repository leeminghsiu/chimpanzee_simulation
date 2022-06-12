import class_Dot
import math
import class_Square
import global_setting
import pygame, random
pygame.font.init()

font = global_setting.font2
pygame.init()

FPS = global_setting.FPS
WIDTH, HEIGHT = global_setting.WIDTH, global_setting.HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chimp_simulator")

WHITE = global_setting.WHITE
BLACK = global_setting.BLACK
RED = global_setting.RED
BLUE = global_setting.BLUE

DOT_QUANTITY = global_setting.DOT_QUANTITY
SQUARE_QUANTITY = global_setting.SQUARE_QUANTITY
DOT_SPEED = global_setting.DOT_SPEED
SQUARE_SPEED = global_setting.SQUARE_SPEED
DISTANCE_BETWEEN_SQUARE = global_setting.DISTANCE_BETWEEN_SQUARE


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


# CREATE
# create sprite groups (empty container)
all_dots = pygame.sprite.Group()
all_territory = pygame.sprite.Group()
all_squares = pygame.sprite.Group()

# create sprites (actual shapes)
for i in range(DOT_QUANTITY):
    new_dot = class_Dot.Dot()
    new_territory = class_Dot.Territory(new_dot)
    all_dots.add(new_dot)
    all_territory.add(new_territory)

for i in range(SQUARE_QUANTITY):
    new_square = class_Square.Square()
    all_squares.add(new_square)


def main():
    # BASIC GAME SETTING
    clock = pygame.time.Clock()
    run = True
    # run the loop every frame
    while run:
        clock.tick(FPS)
        # make sure user can quit the game by clicking 'x'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        # DISPLAY
        # display territory (red circle)
        for entity in all_territory:
            WIN.blit(entity.surf, entity.pos)
        # display dots
        for entity in all_dots:
            WIN.blit(entity.image, entity.pos)
            WIN.blit(entity.text, [entity.pos[0] + entity.combat_value - 10,
                                   entity.pos[1] + entity.combat_value - 30])
        # display squares
        for entity in all_squares:
            WIN.blit(entity.surf, entity.pos)

        # mating count
        male_who_can_mate = 0
        ## go through each dot, check its "can_mate" attribute
        for dot in all_dots:
            if dot.can_mate == 1:
                male_who_can_mate += 1
        print('mate_rate =', male_who_can_mate / DOT_QUANTITY)
        ## create the text item
        mate_rate_text = font.render(f"{male_who_can_mate}/{DOT_QUANTITY} "
                                     f"of male can mate", False, BLACK)
        ## put the text onto the display
        WIN.blit(mate_rate_text, [100, 100])

        # UPDATE
        all_dots.update(all_squares)
        all_squares.update(all_dots, all_squares)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
