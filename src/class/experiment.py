
import sys
sys.path.append('../tools')
import colors as Colors
import game
import textInputBox 
import pygame 

"""
Ce fichier permet de la gestion d'une experience, cad on peut :
    
"""

class Experiment:
    def __init__(self, width, height, color=Colors.BLACK, bg_color=Colors.WHITE, bg_color_text=Colors.WHITE):
        self.font = pygame.font.SysFont("aerial", 60)
        self.screen    = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Experiment")
    
        self.width = width
        self.height = height
        self.text_input_box = textInputBox.TextInputBox((width/2, height/2), width, height, self.font, self.screen, color=color, bg_color_text=bg_color_text)
        self.game = game.Game(width, height, self.font, self.screen)

        #information du participant :
        self.nom_participant = "" 
        self.prenom_participant = "" 
        
    


    def insert_name(self):
        """
            Le participant doit ecrire son nom puis son prenom
            Remarque : fin d'appel de la fonction si le participant a mis son nom ET son prenom   
        """
        group = pygame.sprite.Group(self.text_input_box) 
        running = True
        while running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:    
                    if (self.text_input_box.button_ok.isInside(pygame.mouse.get_pos())):
                        if self.nom_participant == "":
                            self.nom_participant = self.text_input_box.text 
                            self.text_input_box.set_text()
                            print("nom : ", self.nom_participant)
                        elif self.prenom_participant == "":
                            self.prenom_participant = self.text_input_box.text
                            print("prenom : ", self.prenom_participant)
                        if self.nom_participant != "" and self.prenom_participant !="" :
                            running = False
            group.update(event_list)
            group.draw(self.screen)
            pygame.display.flip()


    def play(self , mot="chooseMode"):
        """
            
        """
        self.insert_name()

        self.game.menu(mot)
        print(self.game.cursor_position_list)