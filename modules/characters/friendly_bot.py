from .character import *

class FriendlyBot(Character):
    def __init__(self, x, y, width, height):
        Character.__init__(self , x, y, width, height, "friendly_bot/breath/0.png", 0)
        self.list_breath = self.create_animation_list("friendly_bot/breath", 2, False)
        
        self.list_death = self.create_animation_list("friendly_bot/death", 4, False)
        
    def animation(self):
        if self.is_death == False:
            self.play_animation(12, 23 , self.list_breath)
        else:
            self.play_animation(10, 40, self.list_death)
            if self.image_counter == 39:
                map1.enemy_list.remove(self)
        
friendly_bot1 = FriendlyBot(x = 1100, y = 370, width = 80 , height = 80)
map1.enemy_list.append(friendly_bot1)