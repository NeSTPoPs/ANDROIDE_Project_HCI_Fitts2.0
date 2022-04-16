import pygame 
import sys
sys.path.append('./tools')
sys.path.append('./class')
from drawable import *
from game import *
from cible import *
from target_disposition import *
from healthBar import *
from textInputBox import *
import colors as Colors


def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH = infoObject.current_w - 200
    HEIGHT = infoObject.current_h - 200
    
    
    game = Game(WIDTH, HEIGHT)
    running = True
   
    font = pygame.font.SysFont("aerial", 60)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    text_input_box = TextInputBox((WIDTH/2, HEIGHT/2), WIDTH, HEIGHT, font, screen, color=Colors.RED, bg_color_text=Colors.GREEN)
    group = pygame.sprite.Group(text_input_box)


    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if (text_input_box.button_ok.isInside(pygame.mouse.get_pos())):
                    running = False
        group.update(event_list)
        group.draw(screen)
        pygame.display.flip()

    game.menu("chooseMode")
    print(game.cursor_position_list)
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()