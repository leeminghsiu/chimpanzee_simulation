import pygame, random, math
import numpy
import global_setting
pygame.font.init()

font = global_setting.font

WIDTH = global_setting.WIDTH
HEIGHT = global_setting.HEIGHT
WHITE = global_setting.WHITE
BLACK = global_setting.BLACK
RED = global_setting.RED

DOT_SPEED = global_setting.DOT_SPEED
COMBAT_VALUE_CENTER = global_setting.COMBAT_VALUE_CENTER
COMBAT_VALUE_SPREAD = global_setting.COMBAT_VALUE_SPREAD

class Dot(pygame.sprite.Sprite):
    def __init__(self): # run once
        super(Dot, self).__init__()
        # get its own combat value based on random normal distribution value
        my_value = abs(math.floor(numpy.random.normal(COMBAT_VALUE_CENTER,
                                                      COMBAT_VALUE_SPREAD)))
        if my_value < 10:
            my_value = 10
        self.combat_value = my_value
        self.image = pygame.Surface((self.combat_value*2,
                                     self.combat_value*2)) # set rect size
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE) # make background transparent
        pygame.draw.circle(self.image, BLACK,   # draw a circle on the rect
                           [self.combat_value, self.combat_value], 10, )
        self.text = font.render(f"{self.combat_value}", False, BLACK)
        self.rect = self.image.get_rect()
        self.pos = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
        self.speed_x = 0
        self.speed_y = 0
        self.can_mate = 0   # default as cant mate

    def update(self, all_squares):
        # wandering (random speed and direction)
        self.speed_x += random.randint(-1, 1)
        self.speed_y += random.randint(-1, 1)
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y

        # if go too fast --> stay max speed
        if self.speed_x > DOT_SPEED:
            self.speed_x = DOT_SPEED
        if self.speed_x < -DOT_SPEED:
            self.speed_x = -DOT_SPEED
        if self.speed_y > DOT_SPEED:
            self.speed_y = DOT_SPEED
        if self.speed_y < -DOT_SPEED:
            self.speed_y = -DOT_SPEED
        # if position went out the border --> change direction
        if self.pos[0] <= -self.combat_value + 50:
            self.speed_x += 1
        if self.pos[0] >= WIDTH - self.combat_value -50:
            self.speed_x -= 1
        if self.pos[1] <= -self.combat_value + 50:
            self.speed_y += 1
        if self.pos[1] >= HEIGHT - self.combat_value - 50:
            self.speed_y -= 1

        # start with 'cant mate' again
        # needs to update when female leaves
        self.can_mate = 0

        # SEE IF ANY FEMALE INSIDE TERRITORY
        for square in all_squares:
            dis = (self.pos[0]+self.combat_value - square.pos[0]-10)**2 \
                  + (self.pos[1]+self.combat_value - square.pos[1]-10)**2
            if dis < self.combat_value**2:
                self.can_mate = 1
                print("yes")


# Territory (red circle)
class Territory(pygame.sprite.Sprite):
    def __init__(self, target):
        super(Territory, self).__init__()
        self.surf = pygame.Surface((target.combat_value*2, target.combat_value*2))
        self.surf.fill(WHITE)
        self.surf.set_colorkey(WHITE)
        pygame.draw.circle(self.surf, RED, [target.combat_value, target.combat_value], target.combat_value, )
        self.surf.set_alpha(155)
        self.rect = self.surf.get_rect()
        # follow dot
        self.pos = target.pos
