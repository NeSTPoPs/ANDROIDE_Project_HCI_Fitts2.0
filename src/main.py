import sys
sys.path.append('./tools')
sys.path.append('./class')
from drawable import *
from game import *
from cible import *
from target_disposition import *
from healthBar import *
import colors as Colors
import pygame 

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH = infoObject.current_w - 200
    HEIGHT = infoObject.current_h - 200

    font = pygame.font.SysFont("aerial", 60)
    screen    = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(WIDTH, HEIGHT, font, screen)
    running = True
    #game.addListenerDrawable(make_circle_target_list((WIDTH/2,HEIGHT/2), HEIGHT/3, 10, Colors.DARK_GREEN, 90))
    #game.addListenerDrawable(make_2D_distractor_target_list((WIDTH,HEIGHT), (int(WIDTH/2), int(HEIGHT/2) ), 3, 40, 0.25, Colors.BLACK))
    
    ## Experience avec Mode 
    game.menu("chooseMode")
    
    ## Experience avec Differents Types de disposition des cibles
    #nb_exp_circle = 3
    #key_circle = "circle"
    #game.addTest(nb_exp_circle, key_circle, make_circle_target_list((WIDTH/2,HEIGHT/2), HEIGHT/3, 10, Colors.DARK_GREEN, 90))
    #nb_exp_2D = 2
    #key_densite = "densite"
    #game.addTest(nb_exp_2D, key_densite, make_2D_distractor_target_list((WIDTH,HEIGHT), (int(WIDTH/2), int(HEIGHT/2) ), 3, 40, 0.25, Colors.BLACK))
    
    #game.menu("experienceMulti")
    print("==============")
    #print(game.cursor_position_list)
    
if __name__ == "__main__":
    main()
