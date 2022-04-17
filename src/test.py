import pygame 
import sys
sys.path.append('./class')
sys.path.append('./tools')
import colors as Colors
import experiment 

"""
Fichier test qui permet de faire une experience pour 1 partipicant
Remarque : la gestion des tests (choix des cibles, des modes, etc...) se fait dans le fichier experiment.py
"""

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH = infoObject.current_w - 200
    HEIGHT = infoObject.current_h - 200
    
    experience_1 = experiment.Experiment(WIDTH, HEIGHT, color=Colors.RED, bg_color=Colors.WHITE, bg_color_text=Colors.GREEN)
    
    #experienceMulti
    experience_1.play("experienceMulti")
    
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()