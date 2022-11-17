import pygame
from importlib import resources


class Game:

    hero_image_path, hero_image_filename="shmup.assets.img","hero.png"
    font_path, font_filename= "shmup.assets.fonts","Sansation.ttf"
    screen_size=(640,480)
    
    def __init__(self):
        pass

    def run(self):
        pygame.init()

        screen= pygame.display.set_mode(Game.screen_size,0,32)
        pygame.display.set_caption("Hello")

        with resources.path(Game.font_path, Game.font_filename)as font_path:
            my_font= pygame.font.Font(font_path,20)
        
        text_sf= my_font.render("Hello!!", True, (0,0,0),(255,255,255))

        with resources.path(Game.hero_image_path, Game.hero_image_filename)as hero_path:
            hero_image= pygame.image.load(hero_path).convert_alpha()
            hero_image= pygame.transform.scale(hero_image, (60, 60))
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
            screen.blit(text_sf,(0,0))


            pygame.display.update()


        pygame.quit()
