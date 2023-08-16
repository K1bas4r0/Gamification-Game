import pygame
import random

ANCHO = 1300
ALTO = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ventana = pygame.display.set_mode((ANCHO, ALTO))
font_name = pygame.font.match_font('comic.ttf')
rands = []
rands2 = []
correctas = []
correctas2 = []


def centro_x(sizeimx, coorx):
    sizeimx /= 2
    coorx -= sizeimx
    return coorx


def acept():
    letre = pygame.image.load('img/letrero.png')
    ventana.blit(letre, (centro_x(200, 650), 620))
    draw_text(ventana, "Aceptar", 50, 580, 635, BLACK)


def draw_text(Superficie, taxt, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(taxt, True, color)
    Superficie.blit(text_surface, (x, y))


def draw_text2(Superficie, taxt, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(taxt, True, color, BLACK)
    Superficie.blit(text_surface, (x, y))


def papoir(mensage, tipo, coordpar, content, s, ss, sss, ssss, sssss):
    paper = pygame.image.load('img/papiro{}.png'.format(tipo))
    ventana.blit(paper, coordpar)
    draw_text(ventana, mensage, 50, coordpar[0] + 120, coordpar[1] + 38, BLACK)
    draw_text(ventana, content, 40, coordpar[0] + 535, coordpar[1] + 150, BLACK)
    draw_text(ventana, s, 40, coordpar[0] + 535, coordpar[1] + 190, BLACK)
    draw_text(ventana, ss, 40, coordpar[0] + 535, coordpar[1] + 230, BLACK)
    draw_text(ventana, sss, 40, coordpar[0] + 535, coordpar[1] + 270, BLACK)
    draw_text(ventana, ssss, 40, coordpar[0] + 535, coordpar[1] + 310, BLACK)
    draw_text(ventana, sssss, 40, coordpar[0] + 535, coordpar[1] + 350, BLACK)


def papoir2(mensage, tipo, coordpar, content, s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12):
    paper = pygame.image.load('img/papiro{}.png'.format(tipo))
    ventana.blit(paper, coordpar)
    draw_text(ventana, mensage, 50, coordpar[0] + 120, coordpar[1] + 38, BLACK)
    draw_text(ventana, content, 30, coordpar[0] + 250, coordpar[1] + 150, BLACK)
    draw_text(ventana, s_1, 30, coordpar[0] + 250, coordpar[1] + 180, BLACK)
    draw_text(ventana, s_2, 30, coordpar[0] + 250, coordpar[1] + 210, BLACK)
    draw_text(ventana, s_3, 30, coordpar[0] + 250, coordpar[1] + 240, BLACK)
    draw_text(ventana, s_4, 30, coordpar[0] + 250, coordpar[1] + 270, BLACK)
    draw_text(ventana, s_5, 30, coordpar[0] + 250, coordpar[1] + 300, BLACK)
    draw_text(ventana, s_6, 30, coordpar[0] + 250, coordpar[1] + 330, BLACK)
    draw_text(ventana, s_7, 30, coordpar[0] + 250, coordpar[1] + 360, BLACK)
    draw_text(ventana, s_8, 30, coordpar[0] + 250, coordpar[1] + 390, BLACK)
    draw_text(ventana, s_9, 30, coordpar[0] + 250, coordpar[1] + 420, BLACK)
    draw_text(ventana, s_10, 30, coordpar[0] + 250, coordpar[1] + 450, BLACK)
    draw_text(ventana, s_11, 30, coordpar[0] + 250, coordpar[1] + 480, BLACK)
    draw_text(ventana, s_12, 30, coordpar[0] + 250, coordpar[1] + 510, BLACK)


def dess(si_o_no, coordpar):
    letre = pygame.image.load('img/letrero.png')
    ventana.blit(letre, coordpar)
    draw_text(ventana, si_o_no, 50, coordpar[0] + 50, coordpar[1] + 20, WHITE)


def dess2(une, doe, coordpar):
    letre = pygame.image.load('img/gran_letre.PNG')
    ventana.blit(letre, coordpar)
    draw_text(ventana, une, 50, coordpar[0] + 50, coordpar[1] + 20, BLACK)
    draw_text(ventana, doe, 50, coordpar[0] + 50, coordpar[1] + 70, BLACK)


def dialog(dialogo, s, ss):
    cuadro = pygame.image.load('img/cuadrotexto.png')
    ventana.blit(cuadro, (0, 500))
    draw_text(ventana, dialogo, 45, 35, 535, BLACK)
    draw_text(ventana, s, 45, 35, 580, BLACK)
    draw_text(ventana, ss, 45, 35, 625, BLACK)


def lista_resp1():
    global rands
    it_is_ok = False
    while not it_is_ok:
        while len(rands) != 4:
            rand1 = random.randint(0, 7)
            if rand1 in rands:
                pass
            else:
                if (rand1 == 7 or rand1 == 6) and (7 in correctas or 6 in correctas):
                    pass
                elif rand1 == 7 or rand1 == 6:
                    correctas.append(rand1)
                    rands.append(rand1)
                else:
                    rands.append(rand1)
        if (6 in rands) or (7 in rands):
            it_is_ok = True
        else:
            rands = []
    return rands


def lista_resp2():
    while len(rands2) != 4:
        rand1 = random.randint(0, 7)
        if (rand1 in rands) or (rand1 in rands2):
            pass
        else:
            if (rand1 == 7 or rand1 == 6) and (7 in correctas2 or 6 in correctas2):
                pass
            elif rand1 == 7 or rand1 == 6:
                correctas2.append(rand1)
                rands2.append(rand1)
            else:
                rands2.append(rand1)
    return rands2


def barra_progreso(score):
    if score > 100:
        score = 100
    elif score < 1:
        score = 1
    bar = pygame.image.load('img/barra/{}.png'.format(score))
    ventana.blit(bar, (1250, 100))


def lista_nivel_dos():
    rands_n_dos = []

    while len(rands_n_dos) != 4:
        rand1 = random.randint(0, 3)
        if rand1 in rands_n_dos:
            pass
        else:
            rands_n_dos.append(rand1)
    return rands_n_dos


def lista_arco():
    rarco = []

    while not (0 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(0, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def lista_acueducto():
    rarco = []

    while not (1 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(1, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def lista_templo():
    rarco = []

    while not (2 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(2, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def lista_termas():
    rarco = []

    while not (3 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(3, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def lista_coliseo():
    rarco = []

    while not (4 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(4, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def lista_teatro():
    rarco = []

    while not (5 in rarco):
        rarco = []
        while len(rarco) != 4:
            rand1 = random.randint(5, 8)
            if rand1 in rarco:
                pass
            else:
                rarco.append(rand1)

    return rarco


def done():
    don = False
    return don
