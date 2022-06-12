import class_Dot
import global_setting
import pygame, random, math

WIDTH = global_setting.WIDTH
HEIGHT = global_setting.HEIGHT

BLUE = global_setting.BLUE

SQUARE_SPEED = global_setting.SQUARE_SPEED
DISTANCE_BETWEEN_SQUARE = global_setting.DISTANCE_BETWEEN_SQUARE
CVI = global_setting.CV_IMPORTANCE_TO_FEMALE

class Square(pygame.sprite.Sprite):
    def __init__(self): # run once
        super(Square, self).__init__()
        self.surf = pygame.Surface((20,20)) # size
        self.surf.fill(BLUE)    # color
        self.rect = self.surf.get_rect()    # get solid surface
        # start position
        self.pos = [random.randint(50, WIDTH), random.randint(50, HEIGHT)]
        self.speed_x = 0    # start speed x
        self.speed_y = 0    # start speed y
        self.closest_dot = []
        self.second_closest_dot = []
        self.chosen_dot = []
        self.closest_square = []

    def update(self, target_group, square_group):   # run every frame
        # if go too fast --> stay max speed
        if self.speed_x > SQUARE_SPEED:
            self.speed_x = SQUARE_SPEED
        if self.speed_x < -SQUARE_SPEED:
            self.speed_x = -SQUARE_SPEED
        if self.speed_y > SQUARE_SPEED:
            self.speed_y = SQUARE_SPEED
        if self.speed_y < -SQUARE_SPEED:
            self.speed_y = -SQUARE_SPEED
        # if position went out the border --> change direction
        if self.pos[0] < 50:
            self.speed_x += 1
        if self.pos[0] > WIDTH - 50:
            self.speed_x -=1
        if self.pos[1] < 50:
            self.speed_y += 1
        if self.pos[1] > HEIGHT - 50:
            self.speed_y -= 1

        # find the nearest 2 dots (constantly calculating)
        ## set initail value
        dist_closest = WIDTH + HEIGHT
        dist_2nd_closest = 2 * (WIDTH + HEIGHT)
        ## check every dot
        for object in target_group:
            # get the distance between 'this dot' and self (square)
            dist_current = math.sqrt((object.pos[0]-self.pos[0])**2
                                     + (object.pos[1]-self.pos[1])**2)
            # if 'this dot' is the closest
            if dist_current < dist_closest:
                # put the old closest dot to second closest
                self.second_closest_dot = self.closest_dot
                # assign 'this dot' to self 'closest_dot' attribute
                self.closest_dot = object
                # assign 'this dot' to closest dot
                dist_closest = dist_current
            # if 'this dot' is 2nd closest
            elif dist_2nd_closest > dist_current > dist_closest:
                # assign 'this dot' to self 'second_closest_dot' attribute
                self.second_closest_dot = object
                # assign 'this dot' to 2nd closest dot
                dist_2nd_closest = dist_current
        print(self.closest_dot, self.second_closest_dot)

        # CHOOSE FTOM 2 CLOSEST DOTS (CONSTANTLY CHOOSING)
        # probibility based on two dots' CV values
        # if there are more than 1 dot on the display --> choose
        if len(target_group) > 1:
            # choosing mechanism:
                    # higher CV, wider the range,
                    # random int is more likely to fall inside
            range = self.closest_dot.combat_value**CVI + \
                    self.second_closest_dot.combat_value**CVI
            rand_num = random.randint(0,range)
            # if choose the closest dot --> chosen dot = closest dot
            if rand_num < self.closest_dot.combat_value**CVI:
                self.chosen_dot = self.closest_dot
            # if choose the 2nd closest dot --> chosen dot = 2nd closest dot
            else:
                self.chosen_dot = self.second_closest_dot
        # if there is ony 1 dot --> chosen dot = closest dot
        else:
            self.chosen_dot = self.closest_dot

        # get the distance between self and chosen dot
        self.distance_x = ((self.chosen_dot.pos[0] +
                            self.chosen_dot.combat_value) - self.pos[0])
        self.distance_y = ((self.chosen_dot.pos[1] +
                            self.chosen_dot.combat_value) - self.pos[1])
        self.distance = math.sqrt(self.distance_x ** 2 + self.distance_y ** 2)

        # WHEN ENCOUNTER MALES
        # if the distance to chosen dot is far -> wander
        # (square isnt in chosen dot's territory)
        if self.distance > self.chosen_dot.combat_value:
            # random speed & direction
            self.speed_x += random.randint(-1, 1)
            self.speed_y += random.randint(-1, 1)
            self.pos[0] += self.speed_x
            self.pos[1] += self.speed_y
        # if too close to dot -> stop (or they will overlapse)
        elif self.distance < 40:
            self.speed_x = 0
            self.speed_y = 0
        # if self (square) is in chosen dot's territory -> follow
        else:
            # divide by distance in order to
            # make sure the speed of square only change by 1
            self.speed_x += self.distance_x / self.distance
            self.speed_y += self.distance_y / self.distance
            self.pos[0] += self.speed_x
            self.pos[1] += self.speed_y

        # WHEN ENCOUNTER OTHER FEMALES
        # identify the closest female, and move away
        dist_closest_square = HEIGHT + WIDTH
        for object in square_group:
            dist_current = math.sqrt((object.pos[0] - self.pos[0]) ** 2
                                     + (object.pos[1] - self.pos[1]) ** 2)
            if 0 < dist_current < dist_closest_square:
                self.closest_square = object
                dist_closest_square = dist_current
        ## move away
        if dist_closest_square < DISTANCE_BETWEEN_SQUARE:
            vector_to_other = [(self.closest_square.pos[0] - self.pos[0]),
                               (self.closest_square.pos[1] - self.pos[1])]
            self.speed_x += -vector_to_other[0]/dist_closest_square * 2
            self.speed_y += -vector_to_other[1]/dist_closest_square * 2
