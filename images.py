import pygame

width = 960
height = 540

def getImages():
    imgs = {}

    q0 = pygame.image.load("images/q0.png") 
    q0 = pygame.transform.scale(q0, (width, height))
    imgs['q0'] = q0

    q1a = pygame.image.load("images/q1a.png")
    q1a = pygame.transform.scale(q1a, (width, height))
    imgs['q1a'] = q1a

    q1b = pygame.image.load("images/q1b.png") 
    q1b = pygame.transform.scale(q1b, (width, height))
    imgs['q1b'] = q1b

    q2a = pygame.image.load("images/q2a.png")
    q2a = pygame.transform.scale(q2a, (width, height))
    imgs['q2a'] = q2a

    q2c = pygame.image.load("images/q2c.png")
    q2c = pygame.transform.scale(q2c, (width, height))
    imgs['q2c'] = q2c

    q3a = pygame.image.load("images/q3a.png")
    q3a = pygame.transform.scale(q3a, (width, height))
    imgs['q3a'] = q3a

    q3d = pygame.image.load("images/q3d.png")
    q3d = pygame.transform.scale(q3d, (width, height))
    imgs['q3d'] = q3d

    q4a = pygame.image.load("images/q4a.png")
    q4a = pygame.transform.scale(q4a, (width, height))
    imgs['q4a'] = q4a

    q4e = pygame.image.load("images/q4e.png")
    q4e = pygame.transform.scale(q4e, (width, height))
    imgs['q4e'] = q4e

    q5c = pygame.image.load("images/q5c.png")
    q5c = pygame.transform.scale(q5c, (width, height))
    imgs['q5c'] = q5c

    q5f = pygame.image.load("images/q5f.png")
    q5f = pygame.transform.scale(q5f, (width, height))
    imgs['q5f'] = q5f

    q6c = pygame.image.load("images/q6c.png")
    q6c = pygame.transform.scale(q6c, (width, height))
    imgs['q6c'] = q6c

    q6g = pygame.image.load("images/q6g.png")
    q6g = pygame.transform.scale(q6g, (width, height))
    imgs['q6g'] = q6g

    return imgs