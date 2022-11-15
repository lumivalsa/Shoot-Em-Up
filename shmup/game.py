import pygame
from importlib import resources

class Game:
    def __init__(self):
        pass

    def run(self):
        pygame.init()

        screen= pygame.display.set_mode((640,480),0,32)
        pygame.display.set_caption("Hello")

        with resources.path("assets.img","hero.png")as hero_path:
            hero_image= pygame.image.load(hero_path).convert_alpha()

        running= True 
        while running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    running=False

            screen.fill((0,0,0))

            x,y=pygame.mouse.get_pos()
            x -= hero_image.get_width()/2
            y -= hero_image.get_height()/2
            screen.blit(hero_image,(x,y))


            pygame.display.update()


        pygame.quit()
