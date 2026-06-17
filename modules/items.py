from .characters.hero import *

class Item(Sprite):
    def collect_item(self):
        item_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if item_rect.colliderect(main_hero.hero_rect):
            item_list.remove(self)
            if self.name == "heart.png":
                main_hero.count_heart += 1
            if self.name == "protect.png":
                main_hero.is_protect = True
            if self.name == "key.png":
                main_hero.has_key = True
            if "battery" in self.name and main_hero.count_battery < 5:
                main_hero.count_battery += 1
                main_hero.battery_image.image = main_hero.battery_image.animation_list[main_hero.count_battery]
            
            
            
item_list = [
    Item(425, 625, 25, 25, "heart.png"),
    Item(375, 275, 25, 25, "heart.png"),
    Item(625, 425, 25, 25, "protect.png"),
    Item(350, 500, 50, 50, "battery1.png"),
    Item(450, 500, 50, 50, "battery2.png"),
    Item(325, 275, 25, 25, "key.png"),
    
]