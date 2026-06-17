from .character import *
from .hero import *

class PlantEnemy(Character):
    def __init__(self, x, y, width, height, direction):
        Character.__init__(self, x , y, width, height, "enemy2/atack/0.png", 0 )
        
        
        self.list_death = self.create_animation_list("enemy2/death", 6, False)
        self.list_death_left = self.create_animation_list("enemy2/death", 6, True)
        
        self.direction = direction
        self.list_attack_right = self.create_animation_list("enemy2/atack", 6, False)
        self.list_attack_left = self.create_animation_list("enemy2/atack", 6, True)

        if self.direction == "left":
            self.image = self.list_attack_left[0]
        
    def atack(self):
        if self.direction == "right":
            enemy_rect = pygame.Rect(self.x + self.width / 2, self.y, self.width * 0.75, self.height)
        else:
            enemy_rect = pygame.Rect(self.x - self.width / 4, self.y, self.width * 0.75, self.height)
        
        if main_hero.hero_rect.colliderect(enemy_rect) and self.image_counter == 0:
            self.image_counter = 1

        if self.image_counter == 58 and main_hero.hero_rect.colliderect(enemy_rect):
            if main_hero.is_protect:
                main_hero.is_protect = False
            else:
                main_hero.count_heart -= 1
    
    def animation(self):
        if self.is_death:
            self.play_animation(10 ,60 , self.list_death , self.list_death_left)
            if self.image_counter == 59:
                map1.enemy_list.remove(self)
        else:
            
            self.atack()
            if self.image_counter > 0:
                self.play_animation(10, 59, self.list_attack_right, self.list_attack_left)
            
plant_enemy1 = PlantEnemy(x = 730, y=370, width = 80, height = 80, direction = "right")
map1.enemy_list.append(plant_enemy1)

plant_enemy2 = PlantEnemy(x = 180, y=570, width = 80, height = 80, direction = "left")
map1.enemy_list.append(plant_enemy2)