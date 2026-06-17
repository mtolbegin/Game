from .character import *
from .hero import *

class FlyEnemy(Character):
    def __init__(self, x, y, width, height, speed, finish_x):
        Character.__init__(self, x, y, width, height, "enemy1/fly/0.png", speed)

        self.list_fly = self.create_animation_list(folder_name = "enemy1/fly", count_image = 2, flip = False)
        self.list_fly_left = self.create_animation_list(folder_name = "enemy1/fly", count_image = 2, flip = True)
        
        self.list_death = self.create_animation_list("enemy1/death", 5, False)
        
        self.finish_x = finish_x
        self.start_x = x
        
        self.barrel = Character(x = 0, y = 0, width= 50, height= 50, speed= 3, name= "barrel/0.png")
        self.barrel.list_explosion = self.barrel.create_animation_list("barrel", 8, flip = False)
        self.attack_counter = 0
        self.explosion = False

    def move(self):
        if self.direction == "right":
            self.x += self.speed
            if self.x > self.finish_x:
                self.direction = "left"
        else:
            self.x -= self.speed
            if self.x <self.start_x:
                self.direction = "right"
                
    def attack(self):
        rect = pygame.Rect(self.x + self.width / 2, self.y + self.height * 0.75, 2, 700)
        # pygame.draw.rect(screen, "white", rect)
        if main_hero.hero_rect.colliderect(rect) and self.attack_counter == 0:
            
            self.attack_counter = 150
            self.barrel.x = self.x + 45
            self.barrel.y = self.y  + self.height * 0.75
        
        if self.attack_counter > 0:
            self.attack_counter -= 1 
            self.barrel.show_image()
            self.barrel.y += 5
            
            rect_barrel = pygame.rect.Rect(self.barrel.x, self.barrel.y, self.barrel.width, self.barrel.height)
            if rect_barrel.colliderect(main_hero.hero_rect):
                self.explosion = True
                self.attack_counter = -1
                if main_hero.is_protect:
                    main_hero.is_protect = False
                else:
                    main_hero.count_heart -= 1
                
            for platform in map1.collision_list:
                if rect_barrel.colliderect(platform):
                    self.explosion = True
                    self.attack_counter = -1
                
        if self.explosion == True:
            self.barrel.show_image()
            if self.barrel.image_counter == 30:
                self.attack_counter = 0
                self.explosion = False
            self.barrel.play_animation(4, 31, self.barrel.list_explosion)
                

    def animation(self):
        if self.is_death :
            self.play_animation(8, 39, self.list_death)
            self.y += 5
            if self.y >= 700:
                map1.enemy_list.remove(self)
                
        else:
            self.move()
            self.attack()
            self.play_animation(15, 29, self.list_fly, self.list_fly_left)

fly_enemy1 = FlyEnemy(100, 50, 140, 140, 3, 1000)
map1.enemy_list.append(fly_enemy1)