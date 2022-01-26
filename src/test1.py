import pygame
import sys
import math
import random
sys.path.append('./class')
from cible import *

#window
WIDTH = 1080
HEIGHT = 920

#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#screen
BACKGROUND_COLOR = WHITE

targets_radius = 60
targets_number = 10
not_targets_color = BLUE
targets_color = RED


#Targets spawn on an invisible circle
play_circle = {
        "radius" : 300,
        "pos" : (WIDTH/2, HEIGHT/2), #Center of the circle
        "targets" : [] #List of targets
        }
        
# Mode :
mode_simple = 1
mode_max = 2

#game parameters
## mode simple
default_timer = 10.0 #timer default value when starting the 'game'
timer_bonus = 2.0 #add amount to timer when hitting a target
timer_miss  = -3.0 #remove amout to timer when missing a target
## mode maximise score 
limit_timer = 10.0 #qd limite d'une partie pour le jeu ou on maximise le score en peu de temps

def getpos():
    return pygame.mouse.get_pos()

def drawCircle(pos, color, r):
    pygame.draw.circle(screen, color, pos, r)

def addTarget(color, length):
    pos = getpos()
    play_circle["targets"].append(Cible(pos, length, color))
    drawCircle(pos, color, length) 

def drawTime(time, color):
    dimension = (115, 75, time*10, 30)
    pygame.draw.rect(screen, color, dimension )

def maj_score(): 
    """
        Retourne le temps et le point associee lorsqu'il appuie sur la map
    """
    pos = getpos()
    hit = False
    for t in play_circle["targets"]:
        if t.isInside(pos): #verifie s'il est dans le cercle
            if (t.isTarget): #verifie si c'est dans le cercle du target
                hit = True
                t.newColor(not_targets_color)
                t.isTarget = False
                assign_random_target()
            #drawCircle((t.x, t.y), t.color, t.r)
    if hit: 
        # a bien viser dans la cible
        return timer_bonus, 1
    return timer_miss, -1

def assign_random_target():
    i = random.randint(0,len(play_circle["targets"]) - 1)
    t = play_circle["targets"][i]
    t.isTarget = True
    t.color = targets_color
    drawCircle((t.x, t.y), t.color, t.r)

def init_targets(nb_of_target, t_color, t_size):

    for t in play_circle["targets"]:
        del t
    play_circle["targets"] = []

    theta = 0
    delta_theta = 2*math.pi / nb_of_target
    x,y = play_circle["pos"] #Center of the play circle
    r = play_circle["radius"]
    for i in range(nb_of_target):
        pos = (int(x + r*math.cos(theta)), int(y + r*math.sin(theta)))
        play_circle["targets"].append(Cible(pos, t_size, t_color))
        drawCircle(pos, t_color, t_size)
        theta += delta_theta
        
    assign_random_target()
    pygame.time.set_timer(pygame.USEREVENT, 100)
    
def refresh_screen():
    screen.fill(BACKGROUND_COLOR)
    for t in play_circle["targets"]:
        drawCircle((t.x, t.y), t.color, t.r)

def refresh_barre_time(time):
    if time >= 0:
        life_color = min(int( (time/5)*255) ,255) #level of red = 255 - level of green 
    else : 
        life_color = 0 #temps est negatif donc il n'y a plu de temps donc la barre est rouge
    drawTime(time, (255 - life_color,life_color,0))
    text = my_font.render("Time", True, BLACK)
    text_rect = text.get_rect(center=(60,90))
    screen.blit(text, text_rect)

def end_game(alive_time = -1.0, score=0):
    pygame.time.set_timer(pygame.USEREVENT, 0)
    for t in play_circle["targets"]:
        del t
    play_circle["target"] = []
    screen.fill(BACKGROUND_COLOR)
    text = my_font.render("Game over !", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
    screen.blit(text, text_rect)
    text = my_font.render("Score : "+str(score), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
    screen.blit(text, text_rect)
    if alive_time > 0 :
        text = my_font.render("You survived " + "{:.1f}".format(alive_time) + " seconds", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
    text = my_font.render("Press SPACE to retry !", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
    screen.blit(text, text_rect)

def choix_mode():
    screen.fill(BACKGROUND_COLOR)
    text = my_font.render("CHOOSE YOUR MODE on the terminal",True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    print("Veuillez choisir un mode : ")
    print(mode_simple , " : mode simple")
    print(mode_max, " : mode maximiser score en un temps constant")
    mode = int(input())
    return mode

def play(mode=mode_simple):
    global running, screen, timer, my_font
    pygame.init()
    my_font = pygame.font.SysFont("aerial", 60)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TEST CIBLES")
    screen.fill(BACKGROUND_COLOR)
    pygame.display.update()
    running = True
    isReleased = True
    text = my_font.render("PRESS SPACE TO BEGIN", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    game_started = False
    while running:
        ev = pygame.event.get()

        for event in ev:
            
            if event.type == pygame.MOUSEBUTTONDOWN and game_started:
                
                temps, point = maj_score()
                if mode == mode_simple:
                    timer += temps
                    score += point
                elif mode == mode_max: 
                    if point>0:
                        score += point
                pygame.display.update()
                isReleased = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                isReleased = True

            if isReleased == False:
                pygame.display.update()
      
            if event.type == pygame.USEREVENT:
                refresh_screen()

                # affiche la barre de temps
                refresh_barre_time(timer)
                if mode==mode_simple:
                    timer -= 0.1      
                    alive_time += 0.1
                elif mode==mode_max:
                    timer -= 0.1

                text_timer = my_font.render("{:.1f}".format(timer), True, RED)
                text_rect_timer = text.get_rect(center=(WIDTH/2 +200, HEIGHT/2))
                screen.blit(text_timer, text_rect_timer)
                text_score = my_font.render("Score : " + str(score), True, GREEN)
                text_rect_score = text.get_rect(center=(260,50))
                screen.blit(text_score, text_rect_score)

                pygame.display.update()

                if timer<=0: # temps ecoule, fin de la partie
                    game_started = False
                    if score < 0:
                        score = 0
                    end_game(alive_time, score)
                    pygame.display.update()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t: # permet de creer des nouveaux target avec la touche T
                    addTarget(BLUE, targets_radius)
                    pygame.display.update()
                      
                if event.key == pygame.K_SPACE and game_started == False: # permet de renouveler la partie
                    init_targets(targets_number, not_targets_color, targets_radius)
                    game_started = True
                    alive_time = 0
                    score = 0
                    
                    mode = choix_mode()
                    
                    if mode==mode_simple:
                        timer = default_timer
                    elif mode==mode_max:
                        timer = limit_timer
                    refresh_screen()
            if event.type == pygame.QUIT:
                running = False

def main():
    print("Bienvenue au jeu des cibles")
    #print("Veuillez choisir un mode : ")
    #print(mode_simple , " : mode simple")
    #print(mode_max, " : mode maximiser score en un temps constant")

    #mode = int(input())
    play()
    
    print("Fin de la game")
    
main()
