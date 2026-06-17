import pytmx, os, pygame
from .settings import screen

class Map():
    def __init__(self, name):
        path = os.path.join(__file__, "..","..","tilemaps",name)
        path = os.path.abspath(path)
        self.tilemap = pytmx.load_pygame(path)
        self.width = self.tilemap.tilewidth 
        self.height = self.tilemap.tileheight
        self.collision_list = []
        self.ladder_list = []
        self.create_collision()

        self.enemy_list = []
     
    def show(self):
        for layer in self.tilemap.visible_layers:
            if layer.name != "Collision" and layer.name != "LadderCollision":
                for x, y, tile in layer:
                    if tile != 0:
                        image = self.tilemap.get_tile_image_by_gid(tile)
                        screen.blit(image, (x * self.width, y * self.height))
    
    def create_collision(self):
        self.collision_list = []
        layer = self.tilemap.get_layer_by_name("Collision")
        for element in layer:
            rect1 = pygame.Rect(element.x, element.y, element.width, element.height)
            self.collision_list.append(rect1)
        self.ladder_list = []
        layer = self.tilemap.get_layer_by_name("LadderCollision")
        for element in layer:
            rect1 = pygame.Rect(element.x, element.y, element.width, element.height)
            self.ladder_list.append(rect1)
            # tilemap.get_layer_by_name("назва") - отримує прошарок(слой) за назвою
            # pygame.Rect(x, y, ширина, висота) - створює прямокутник 

map1 = Map("lvl1.tmx")