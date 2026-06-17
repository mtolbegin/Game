import pygame
from .settings import *
from .map import *
from .items import *
from .characters import *

def start_game():
    run = True
    fps = pygame.time.Clock()
    rect_win = pygame.Rect(1450, 600, 50, 50)

    win = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    main_hero.is_hold_blaster = not main_hero.is_hold_blaster
                
        fps.tick(60)
        screen.fill("black")

        if main_hero.count_heart > 0 and win == False:
            bg.show_image()
            map1.show()
            
            for enemy in map1.enemy_list:
                enemy.animation()
                enemy.show_image()
                
            for item in item_list:
                item.show_image()
                item.collect_item()

            main_hero.show_image()
            main_hero.move()
            main_hero.show_stats()

            if main_hero.hero_rect.colliderect(rect_win) and main_hero.has_key: 
                win = True
                
        elif main_hero.count_heart <= 0:
            screen.blit(lose_text, (540, 330))
        elif win == True:
            screen.blit(win_text, (520, 330))

            
        pygame.display.flip()