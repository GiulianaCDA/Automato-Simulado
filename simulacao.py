import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
import pygame.freetype

pygame.init()

#DISPLAY WINDOW
sizeBackground = width, height = 1300, 650
screen = pygame.display.set_mode(sizeBackground)
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))
screen.blit(background, (0,0))

#FONT
myfont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 74)

#PLAY BUTTON
playbutton = pygame.Rect(450, 400, 120, 120)
playbuttonImg = pygame.image.load("playbutton.gif") 
playbuttonImg = pygame.transform.scale(playbuttonImg, (120, 120))
playfont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 50)
screen.blit(playbuttonImg, playbutton) 
text = myfont.render(' play ' , True , (255,255,255))

#CURSOR
handCursor = pygame.SYSTEM_CURSOR_HAND   
arrowCursor = pygame.SYSTEM_CURSOR_ARROW  

def home():

    text_surface, rect = myfont.render("Bem vindo ao", (255, 255, 255))
    screen.blit(text_surface, (430, 140))

    text_surface, rect = myfont.render("caixa eletrônico", (255, 196, 224))
    screen.blit(text_surface, (350, 200))

    text_surface, rect = playfont.render("iniciar ", (255, 196, 224))
    screen.blit(text_surface, (580, 420))

    text_surface, rect = playfont.render("simulação", (255, 196, 224))
    screen.blit(text_surface, (580, 465))

    pygame.display.update() 
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        pygame.display.flip()
    
    home()
    
    mouse = pygame.mouse.get_pos()
    if playbutton.collidepoint(mouse):
        pygame.mouse.set_cursor(handCursor)
          
    else:
        pygame.mouse.set_cursor(arrowCursor)
        
    pygame.display.update() 