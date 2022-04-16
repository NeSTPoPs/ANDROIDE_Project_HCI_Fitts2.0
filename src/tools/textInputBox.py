from cgitb import text
import sys
from tkinter import Button
sys.path.append('./tools')
import pygame
import colors as Colors
from button import * 


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, font, screen, width_texte=400, height_texte=10, color=Colors.BLACK, bg_color=Colors.WHITE, bg_color_text = Colors.WHITE):
        super().__init__()
        self.color = color
        self.bg_color = bg_color
        self.bg_color_text = bg_color_text
        self.pos = pos
        self.width = width
        self.height = height
        self.width_texte = width_texte
        self.height_texte = height_texte
        self.font = font
        self.screen = screen
        self.active = False
        self.text = ""
        self.render_text()
        #self.rect = None
        self.button_ok = Button((int(self.width/2),int(self.height/2 + 100)), 1, 200, 60 , (200, 50, 50), Colors.RED, "Ok")
        self.have_name = False

    def set_text(self, mot = "", have_name = True):
        self.text = mot
        self.have_name = have_name

    def render_text(self):
        texte = self.font.render(self.text, True, self.color, self.bg_color_text)
        self.width_texte = max(self.width_texte, texte.get_width()+10)
        self.height_texte = max(self.height_texte, texte.get_height()+10)
        self.image = pygame.Surface((self.width_texte, self.height_texte), pygame.SRCALPHA)
        self.image.fill(self.bg_color_text)
        self.image.blit(texte, (5, 2))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-5, -5), 2) 
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        self.screen.fill(self.bg_color)
        
        if self.have_name == False :
            phrase = self.font.render("Veuillez mettre votre nom", True, Colors.BLACK)
        else : 
            phrase = self.font.render("Veuillez mettre votre prenom", True, Colors.BLACK)
        self.screen.blit(phrase,(self.pos[0]-30, self.pos[1]-50))
        
        self.button_ok.draw(self)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if (self.button_ok.isInside(pygame.mouse.get_pos())):
                    self.active = False
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.text = self.text
                else:
                    self.text += event.unicode
            self.render_text() 