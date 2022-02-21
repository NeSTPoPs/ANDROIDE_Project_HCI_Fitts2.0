import sys
sys.path.append('./tools')
sys.path.append('./class')
from drawable import *
from game import *
from cible import *
from target_disposition import *
from healthBar import *
from colors import *

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH = infoObject.current_w - 200
    HEIGHT = infoObject.current_h - 200
    game = Game(WIDTH, HEIGHT)
    running = True
    game.addListenerDrawable(make_circle_target_list((WIDTH/2,HEIGHT/2), HEIGHT/3, 10, DARK_GREEN, 90))
    game.menu("chooseMode")
    
if __name__ == "__main__":
    main()
