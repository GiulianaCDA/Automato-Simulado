import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
import pygame.freetype
from time import sleep

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
sizeBackground = width, height = 1300, 650
screen = pygame.display.set_mode(sizeBackground)
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))
background2 = pygame.image.load("background3.png") 
background2 = pygame.transform.scale(background2, (width, height))
screen.blit(background, (0,0))
page = 'home'


#FONT
homeFont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 74)
purpleColor = (50, 47, 93)

#BUTTONS
playbutton = pygame.Rect(450, 400, 120, 120)
playbuttonImg = pygame.image.load("playbutton.gif") 
playbuttonImg = pygame.transform.scale(playbuttonImg, (120, 120))
playfont = pygame.freetype.Font("Bobby-Jones-Soft.otf", 50)
screen.blit(playbuttonImg, playbutton) 

backButton = pygame.Rect(30, 60, 160, 40)  

totalButton = pygame.Rect(100, 260, 350, 40) 

parcialButton = pygame.Rect(100, 350, 350, 40) 

#CURSOR
handCursor = pygame.SYSTEM_CURSOR_HAND   
arrowCursor = pygame.SYSTEM_CURSOR_ARROW  

#OPTIONS IMAGES
q0 = pygame.image.load("q0.png") 
q0 = pygame.transform.scale(q0, (768, 432))

q1a = pygame.image.load("q1a.png")
q1a = pygame.transform.scale(q1a, (768, 432))
q1b = pygame.image.load("q1b.png") 
q1b = pygame.transform.scale(q1b, (768, 432))

q2a = pygame.image.load("q2a.png")
q2a = pygame.transform.scale(q2a, (768, 432))
q2c = pygame.image.load("q2c.png")
q2c = pygame.transform.scale(q2c, (768, 432))

q3a = pygame.image.load("q3a.png")
q3a = pygame.transform.scale(q3a, (768, 432))
q3d = pygame.image.load("q3d.png")
q3d = pygame.transform.scale(q3d, (768, 432))

q4a = pygame.image.load("q4a.png")
q4a = pygame.transform.scale(q4a, (768, 432))
q4e = pygame.image.load("q4e.png")
q4e = pygame.transform.scale(q4e, (768, 432))

q5c = pygame.image.load("q5c.png")
q5c = pygame.transform.scale(q5c, (768, 432))
q5f = pygame.image.load("q5f.png")
q5f = pygame.transform.scale(q5f, (768, 432))

q6c = pygame.image.load("q6c.png")
q6c = pygame.transform.scale(q6c, (768, 432))
q6g = pygame.image.load("q6g.png")
q6g = pygame.transform.scale(q6g, (768, 432))


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
                screen.blit(q0, (660, 140))                
                optionsButtons = options()
        else:
            pygame.mouse.set_cursor(arrowCursor)

    elif page == 'options':
        if optionsButtons['saque'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q1b, (660, 140))
                prevState = 'saque'
                pageOption('saque')
                page = 'pageOption'

        elif optionsButtons['emprestimo'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q3d, (660, 140))
                prevState = 'emprestimo'
                pageOption('empréstimo')
                page = 'pageOption'
        
        elif optionsButtons['saldo'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q4e, (660, 140))
                prevState = 'saldo'
                pageOption('Ver saldo')
                page = 'pageOption'
        
        elif optionsButtons['pagamento'].collidepoint(mouse): 
            pygame.mouse.set_cursor(handCursor)
            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q2c, (660, 140))
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
                    screen.blit(q1a, (660, 140)) 
                elif prevState == 'emprestimo':
                    screen.blit(q3a, (660, 140)) 
                elif prevState == 'pagamento':  
                    screen.blit(q2a, (660, 140)) 
                elif prevState == 'saldo':
                    screen.blit(q4a, (660, 140))    
                optionsButtons = options()
        else:
            pygame.mouse.set_cursor(arrowCursor)

    if page == 'pagamento':
        if totalButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q5f, (660, 140))
                pageOption('pagamento total')
                page = 'total'

        elif parcialButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q6g, (660, 140))
                pageOption('pagamento parcial')
                page = 'parcial'

        elif backButton.collidepoint(mouse):
            pygame.mouse.set_cursor(handCursor)

            if event.type == MOUSEBUTTONDOWN:
                screen.blit(background2, (0,0))
                screen.blit(q2a, (660, 140)) 
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
                    screen.blit(q5c, (660, 140))
                else:
                    screen.blit(q6c, (660, 140))
                sleep(0.2)
                page = 'pagamento'
        else:
            pygame.mouse.set_cursor(arrowCursor)
    pygame.display.update()