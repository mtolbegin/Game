import pygame

pygame.init()

screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("game")

font = pygame.font.Font(None, 100)
lose_text = font.render("Ви програли", True, "white")
win_text = font.render("Ви перемогли", True, "white")

# pygame.init() - налаштовує pygame (дозволяє текст та звуки)
# pygame.font.Font(None, розмір) - створює новий шрифт (замість None - може бути назва)
# font.render("Текст", True, "колір") - створює текст (True - згладжування)
# Щоб відобразити текст - blit (як і зображення)