import pygame, os
from .settings import *

class Sprite():
    def __init__(self, x , y , width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.image = self.load_image(self.name)

    def load_image(self, name, flip=False):
        path = os.path.join(__file__, "..", "..", "images", name)
        path = os.path.abspath(path)
        image = pygame.image.load(path)
        image = pygame.transform.scale(image,(self.width,self.height))
        if flip == True:
            image = pygame.transform.flip(image, True, False)
        return image
    def show_image(self):
        screen.blit(self.image, (self.x, self.y))
        
    def create_animation_list(self, folder_name, count_image, flip):
        animation_list=[]
        for count in range(count_image):
            name = f"{folder_name}/{count}.png"
            image = self.load_image(name, flip)
            animation_list.append(image)
        return animation_list
bg = Sprite(x = 0, y = 0, width = 1500, height = 700, name = "bg.png")