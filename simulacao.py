import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
import pygame.freetype
from time import sleep
from images import getImages

pygame.init()

def home():
    text_surface, rect = homeFont.render("Bem vindo ao", (255, 255, 255))
    screen.blit(text_surface, (430, 140))

    text_surface, rect = homeFont.render("caixa eletrônico", (255, 196, 224))
    screen.blit(text_surface, (350, 200))

    text_surface, rect = playfont.render("iniciar ", (255, 196, 224))
    screen.blit(text_surface, (580, 420))

    text_surface, rect = playfont.render("simulação", (255, 196, 224))
    screen.blit(text_surface, (580, 465))

    pygame.display.update() 

def options():

    optionFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 50)
    optionsButtons = {}
    
    saqueButton = pygame.Rect(160, 240, 160, 40) 
    optionsButtons["saque"] = saqueButton
    text, rect = optionFont.render('Saque', purpleColor)
    screen.blit(text, saqueButton) 

    pagamentoButton = pygame.Rect(160, 310, 160, 40) 
    optionsButtons["pagamento"] = pagamentoButton
    text, rect = optionFont.render('Pagamento', purpleColor)
    screen.blit(text, pagamentoButton)
    
    emprestimoButton = pygame.Rect(160, 370, 160, 40) 
    optionsButtons["emprestimo"] = emprestimoButton
    text, rect = optionFont.render('Empréstimo', purpleColor)
    screen.blit(text, emprestimoButton)

    saldoButton = pygame.Rect(160, 450, 160, 40) 
    optionsButtons["saldo"] = saldoButton
    text, rect = optionFont.render('Verificar saldo', purpleColor)
    screen.blit(text, saldoButton)

    pygame.display.update()
    return optionsButtons

def pagamentoPage():
    optionFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 50)
    pagamentoButtons = {}

    descFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 30) 
    text_surface, rect = descFont.render('Voltar', purpleColor)
    screen.blit(text_surface, backButton) 

    pagamentoButtons["total"] = totalButton
    text, rect = optionFont.render('Pagamento total', purpleColor)
    screen.blit(text, totalButton) 

    pagamentoButtons["parcial"] = parcialButton
    text, rect = optionFont.render('Pagamento parcial', purpleColor)
    screen.blit(text, parcialButton) 

    return pagamentoButtons

def pageOption(text):
    optionFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 80)
    descFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 30) 

    text_surface, rect = optionFont.render(text, purpleColor)

    if text == 'pagamento':
        pagamentoPage()
    elif text == 'saque':
        screen.blit(text_surface, (200, 300)) 
    elif text == 'pagamento parcial' or text == 'pagamento total':
        optionFont = pygame.freetype.Font('Bobby-Jones-Soft.otf', 50)
        text_surface, rect = optionFont.render(text, purpleColor)
        screen.blit(text_surface, (140, 300)) 
    else:
        screen.blit(text_surface, (120, 300)) 

    if text != 'pagamento':
        desc = "Seu " + text + " será realizado!"
        desc_surface, rect = descFont.render(desc, (255, 255, 255))
        if text != 'pagamento parcial' and text != 'pagamento total':
            screen.blit(desc_surface, (120, 380)) 
        else:
            screen.blit(desc_surface, (80, 350)) 

                       
    text_surface, rect = descFont.render('Voltar', purpleColor)
    screen.blit(text_surface, backButton) 


#DISPLAY WINDOW
pygame.display.set_caption('Simulação de caixa eletrônico') 
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon) 
sizeBackground = width, height = 1300, 650
screen = pygame.display.set_mode(sizeBackground)
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (width, height))
background2 = pygame.image.load("images/background2.png") 
background2 = pygame.transform.scale(background2, (width, height))
screen.blit(background, (0,0))
page = 'home'


#FONT
homeFont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 74)
purpleColor = (50, 47, 93)

#BUTTONS
playbutton = pygame.Rect(450, 400, 120, 120)
playbuttonImg = pygame.image.load("images/playbutton.gif") 
playbuttonImg = pygame.transform.scale(playbuttonImg, (120, 120))
playfont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 50)
screen.blit(playbuttonImg, playbutton) 

backButton = pygame.Rect(30, 60, 160, 40)  

totalButton = pygame.Rect(100, 260, 350, 40) 

parcialButton = pygame.Rect(100, 350, 350, 40) 

#CURSOR
handCursor = pygame.SYSTEM_CURSOR_HAND   
arrowCursor = pygame.SYSTEM_CURSOR_ARROW  

#IMAGES
imgs = getImages()
x = 730
y = 100

home()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        pygame.display.flip()
    
    mouse = pygame.mouse.get_pos()

    if page == 'home':
        if playbutton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                page = 'options'
                screen.blit(background2, (0,0))
                screen.blit(imgs['q0'], (x, y))                
                optionsButtons = options()
        else:
            pygame.mouse.set_cursor(arrowCursor)

    elif page == 'options':
        if optionsButtons['saque'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q1b'], (x, y))
                prevState = 'saque'
                pageOption('saque')
                page = 'pageOption'

        elif optionsButtons['emprestimo'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q3d'], (x, y))
                prevState = 'emprestimo'
                pageOption('empréstimo')
                page = 'pageOption'
        
        elif optionsButtons['saldo'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q4e'], (x, y))
                prevState = 'saldo'
                pageOption('Ver saldo')
                page = 'pageOption'
        
        elif optionsButtons['pagamento'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q2c'], (x, y))
                prevState = 'pagamento'
                pageOption('pagamento')
                page = 'pagamento'
        else:
            pygame.mouse.set_cursor(arrowCursor)

    if page == 'pageOption':
        if backButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                page = 'options'
                screen.blit(background2, (0,0))
                if prevState == 'saque':
                    screen.blit(imgs['q1a'], (x, y)) 
                elif prevState == 'emprestimo':
                    screen.blit(imgs['q3a'], (x, y)) 
                elif prevState == 'pagamento':  
                    screen.blit(imgs['q2a'], (x, y)) 
                elif prevState == 'saldo':
                    screen.blit(imgs['q4a'], (x, y))    
                optionsButtons = options()
        else:
            pygame.mouse.set_cursor(arrowCursor)

    if page == 'pagamento':
        if totalButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q5f'], (x, y))
                pageOption('pagamento total')
                page = 'total'

        elif parcialButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q6g'], (x, y))
                pageOption('pagamento parcial')
                page = 'parcial'

        elif backButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(imgs['q2a'], (x, y)) 
                options()
                page = 'options'
        else:
            pygame.mouse.set_cursor(arrowCursor)
    if page == 'total' or page == 'parcial':
        if backButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                pagamentoPage()
                if page == 'total':
                    screen.blit(imgs['q5c'], (x, y))
                else:
                    screen.blit(imgs['q6c'], (x, y))
                sleep(0.2)
                page = 'pagamento'
        else:
            pygame.mouse.set_cursor(arrowCursor)
    pygame.display.update()