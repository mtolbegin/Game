from .character import *
from .hero import *

class Enemy(Character):
    def __init__(self, x, y, width, height, speed, finish_x):
        Character.__init__(self, x, y, width, height, "enemy3/breath/0.png", speed)

        self.list_move = self.create_animation_list("enemy3/move", 5, False)
        self.list_move_left = self.create_animation_list("enemy3/move", 5, True)
        self.finish_x = finish_x
        self.start_x = x
        
        self.bullet = Sprite(0,0,20,20,"enemy3/bullet.png")
        self.attack_counter = 0

        self.list_death = self.create_animation_list("enemy3/death", 4, False)
        
    def move(self):
        self.check_collision()
        if self.direction == "right" and self.can_move_right:
            self.x += self.speed 
        elif self.direction == "left" and self.can_move_left:
            self.x -= self.speed
            
        if self.x > self.finish_x or not self.can_move_right:
            self.direction = "left"
        if self.x < self.start_x or not self.can_move_left:
            self.direction = "right"
            
    def attack(self):
        if self.direction == "right":
            rect = pygame.Rect(self.x + self.width, self.y, self.width * 4, self.height)
        else:
            rect = pygame.Rect(self.x - self.width * 4, self.y, self.width * 4, self.height)
        # pygame.draw.rect(screen, "red", rect, 5)
        
        if rect.colliderect(main_hero.hero_rect) and self.attack_counter == 0:
            self.attack_counter = 150
            self.bullet.x = self.x + self.width/2
            self.bullet.y = self.y + self.height/2
            
            self.bullet.direction = self.direction
            if self.direction == "right":
                self.bullet.image = self.bullet.load_image("enemy3/bullet.png", False)
            else:
                self.bullet.image = self.bullet.load_image("enemy3/bullet.png", True)

        if self.attack_counter > 0:
            self.move_bullet()
            
        if self.attack_counter < 0:
            self.attack_counter += 1

    def move_bullet(self):
        self.attack_counter -= 1
        if self.bullet.direction == "right":
            self.bullet.x += 8
        else:
            self.bullet.x -= 8
        self.bullet.show_image()     

        rect_bullet = pygame.Rect(self.bullet.x, self.bullet.y, self.bullet.width, self.bullet.height)
        
        if main_hero.hero_rect.colliderect(rect_bullet):
            if main_hero.is_protect:
                main_hero.is_protect = False
            else:
                main_hero.count_heart -= 1
            self.attack_counter = -50
        
        for platform in map1.collision_list:
            if platform.colliderect(rect_bullet):
                self.attack_counter = -50
        
    def animation(self):
        if self.is_death == False:
            self.play_animation(7, 34, self.list_move, self.list_move_left)
            self.attack()
            self.move()
        else:
            self.play_animation(10, 40, self.list_death)
            if self.image_counter == 39:
                map1.enemy_list.remove(self)

enemy1 = Enemy(900, 570, 80, 80, 2, 1150)
map1.enemy_list.append(enemy1)