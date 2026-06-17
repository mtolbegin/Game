from .character import *

class Hero(Character):
    def __init__(self, x, y, width, height, name, speed):
        Character.__init__(self, x, y, width, height, name, speed)
        
        self.list_run = self.create_animation_list("hero/run", 6, False)
        self.list_run_left = self.create_animation_list("hero/run", 6, True)

        self.list_jump = self.create_animation_list("hero/jump", 2, False)
        self.list_jump_left = self.create_animation_list("hero/jump", 2, True)
        self.list_breath = self.create_animation_list("hero/breath", 11, False)

        self.is_hold_blaster = False
        self.list_run_shoot = self.create_animation_list("hero/shooting_run", 6, False)
        self.list_run_shoot_left = self.create_animation_list("hero/shooting_run", 6, True)

        self.count_heart = 3
        self.heart_image = Sprite(0,0,40,40,"heart.png")
        self.empty_heart_image = Sprite(0,0,40,40,"empty_heart.png")
        
        self.list_crawl = self.create_animation_list("hero/crawl", 5, False)
        self.list_crawl_left = self.create_animation_list("hero/crawl", 5, True)

        self.bullet = Sprite(x = 0, y = 0, width = 20, height = 20, name = "hero/bullet.png")
        self.attack_counter = 0

        self.count_battery = 5
        self.battery_image = Sprite(25, 30, 40, 40, "battery/5.png")
        self.battery_image.animation_list = self.battery_image.create_animation_list('battery', 6, False)
        
        self.list_climb = self.create_animation_list("hero/climb", 2, False)
        self.on_ladder = False
        
        self.has_key = False
        self.is_protect = False
        self.protect_image = Sprite(25, 80, 40, 40, "protect.png")
        
        self.hero_rect = pygame.Rect(0, 0, 0, 0)
    def move(self):
        self.check_collision()
        self.list_key = pygame.key.get_pressed()
        print(self.can_stand_up)
        if self.list_key[pygame.K_LSHIFT]:
            self.is_crawl = True
        elif self.can_stand_up == True:
            self.is_crawl = False
            
        if self.list_key[pygame.K_d] == True and self.can_move_right == True:
            self.direction = "right"
            if self.is_crawl == False:
                self.x += self.speed
                if self.is_hold_blaster == True:
                    self.play_animation(5, 29, self.list_run_shoot, self.list_run_shoot_left)
                else:
                    self.play_animation(5, 29, self.list_run, self.list_run_left)
            else:
                self.x += self.speed / 3
                self.play_animation(15, 74, self.list_crawl,self.list_crawl_left)
        elif self.list_key[pygame.K_a] == True and self.can_move_left == True:
            self.direction = "left"
            if self.is_crawl == False:
                self.x -= self.speed
                if self.is_hold_blaster == True:
                    self.play_animation(5, 29, self.list_run_shoot, self.list_run_shoot_left)
                else:
                    self.play_animation(5, 29, self.list_run, self.list_run_left)
            else:
                self.x -= self.speed / 3
                self.play_animation(15, 74, self.list_crawl,self.list_crawl_left)
        elif self.can_fall == False and self.jump_counter == 0:
            if self.is_crawl:
                if self.direction == "right":
                    self.image = self.list_crawl[0]
                else:
                    self.image = self.list_crawl_left[0]
            else:
                self.play_animation(15, 164, self.list_breath)
            
            
        if self.can_fall and self.jump_counter == 0 and self.on_ladder == False:
            self.y += 5
            if self.direction == "right":
                self.image = self.list_jump[1]
            else:
                self.image = self.list_jump_left[1]

        self.jump()
        self.attack()
        self.climb()
        
    def climb(self):
        self.on_ladder = False
        for ladder in map1.ladder_list:
            if self.hero_rect.colliderect(ladder):
                self.on_ladder = True
        if self.on_ladder and self.list_key[pygame.K_w] and self.can_stand_up:
            self.y -= 3
            self.play_animation(10, 19, self.list_climb)
        if self.on_ladder and self.list_key[pygame.K_s] and self.can_fall:
            self.y += 3
            self.play_animation(10, 19, self.list_climb)
            
    def attack(self):
        if self.list_key[pygame.K_q] and self.attack_counter == 0 and self.is_hold_blaster and self.count_battery > 0:
            self.count_battery -= 1
            self.battery_image.image = self.battery_image.animation_list[self.count_battery]
            
            self.attack_counter = 200
            self.bullet.x = self.x + self.width / 2
            self.bullet.y = self.y + self.height / 2
            self.bullet.direction = self.direction
            if self.direction == "right":
                self.bullet.image = self.bullet.load_image("hero/bullet.png", False)
            else:
                self.bullet.image = self.bullet.load_image("hero/bullet.png", True)
                
        if self.attack_counter > 0:
            if self.bullet.direction == "right":
                self.bullet.x += 8
            else:
                self.bullet.x -= 8
            
            self.attack_counter -= 1
            self.bullet.show_image()

            bullet_rect = pygame.Rect(self.bullet.x, self.bullet.y, self.bullet.width, self.bullet.height)
            for platform in map1.collision_list:
                if bullet_rect.colliderect(platform):
                    self.attack_counter = -40

            for enemy in map1.enemy_list:
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                if bullet_rect.colliderect(enemy_rect):
                    self.attack_counter = -40
                    enemy.is_death = True
                    enemy.image_counter = 0

        if self.attack_counter < 0:
            self.attack_counter += 1
    
    def jump(self):
        if self.list_key[pygame.K_SPACE] == True and self.can_fall == False and self.on_ladder == False:
            self.jump_counter = 23
        if self.jump_counter > 0:
            self.y -= 6  
            self.jump_counter -= 1
            if self.direction == "right":
                self.image = self.list_jump[0]
            else:
                self.image = self.list_jump_left[0]
    def show_stats(self):
        for num in range(3):
            if num < self.count_heart:
                screen.blit(self.heart_image.image, ((num + 2) *50,20))
            else:
                screen.blit(self.empty_heart_image.image, ((num + 2) *50,20))
                
        self.battery_image.show_image()
        if self.is_protect:
            self.protect_image.show_image()
                
main_hero = Hero(20, 570, 80, 80, "hero.png", 3)