from ..image import *
from ..map import *

class Character(Sprite):
    def __init__(self, x, y, width, height, name, speed):
        Sprite.__init__(self, x, y, width, height, name)
        self.speed = speed
        self.jump_counter = 0
        self.image_counter = 0
        self.direction = "right"
        self.is_crawl = False
        self.is_death = False
    
    def check_collision(self):
        self.hero_rect = pygame.Rect(self.x+15, self.y+10, self.width-30, self.height-10)
        if self.is_crawl == True:
            self.hero_rect = pygame.Rect(self.x+15, self.y+30, self.width-30, self.height-30)
        # pygame.draw.rect(screen, "blue", self.hero_rect)
        self.can_move_right = True
        self.can_move_left = True
        self.can_fall = True
        self.can_stand_up = True
        
        for platform in map1.collision_list:
            left_rect = pygame.Rect(platform.x,platform.y + 8,1,platform.height - 16)
            # pygame.draw.rect(screen,"red",left_rect)
            right_rect = pygame.Rect(platform.x+platform.width,platform.y + 8,1,platform.height- 16)
            # pygame.draw.rect(screen,"red",right_rect)
            top_rect = pygame.Rect(platform.x + 8,platform.y,platform.width - 16,1)
            # pygame.draw.rect(screen,"red",top_rect)
            bottom_rect = pygame.Rect(platform.x + 8,platform.y+platform.height,platform.width - 16, 2)
            # pygame.draw.rect(screen,"red",bottom_rect)
            
            if self.hero_rect.colliderect(left_rect):
                self.can_move_right = False
            if self.hero_rect.colliderect(right_rect):
                self.can_move_left = False
            if self.hero_rect.colliderect(top_rect):
                self.can_fall = False
                self.y = platform.y - self.height + 1
            if self.hero_rect.colliderect(bottom_rect):
                self.jump_counter = 0
                self.can_stand_up = False
    def play_animation(self, time,max_count,list_right,list_left = None):
        self.image_counter += 1
        if self.image_counter >= max_count:
            self.image_counter = 0
        index = self.image_counter // time
        if self.direction == "left" and list_left:
            self.image = list_left[index]
        else:
            self.image = list_right[index]
            