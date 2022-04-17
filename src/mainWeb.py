import sys
sys.path.append('./tools')
sys.path.append('./class')
from game import *
import webExtractor as webEx
import colors as Colors
import pygame

URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH = infoObject.current_w - 200
    HEIGHT = infoObject.current_h - 200
    font = pygame.font.SysFont("aerial", 60)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    game = Game(WIDTH, HEIGHT, font, screen)
    
    #Generating targets with URL
    game.listTarget = webEx.getTargetsFromUrl(URL, WIDTH, HEIGHT, displayInfo = True)
    
    game.infiniteTime = True
    
    game.menu("chooseMode")

if __name__ == "__main__":
    main()
