import time

import cv2
import pygame
import Funciones_Globales
import imutils
from PIL import Image

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
letre = pygame.image.load('img/letrero.png')
estado_croma = None
transicion = pygame.image.load('img/black_screen.png')
equiz = pygame.image.load('img/equiz.png')

acueducto = pygame.image.load('img/Acueducto.png')
sombra_acueducto = pygame.image.load('img/acueductonegro.png')

templo = pygame.image.load('img/templo.png')
sombra_templo = pygame.image.load('img/templonegro.png')

coliseo = pygame.image.load('img/coliseo.png')
sombra_coliseo = pygame.image.load('img/coliseonegro.png')

estatua = pygame.image.load('img/estatua.png')
sombra_estatua = pygame.image.load('img/estatuanegra.png')

arbol = pygame.image.load('img/ARBOL.png')
sombra_arbol = pygame.image.load('img/arbolnegro.png')

croma1 = True
croma2 = False
croma3 = False
marco_au = False

pygame.mixer.init()
ini = pygame.mixer.Sound('music/revelation.mp3')
voz_ini = pygame.mixer.Sound('music/voz_init.mp3')
celeb = pygame.mixer.Sound('music/Sevilla.mp3')
celeb.set_volume(0.2)
no_celeb = pygame.mixer.Sound('music/Micronesia.mp3')
no_celeb.set_volume(0.2)
llorar = pygame.mixer.Sound('music/Whispers.mp3')
llorar.set_volume(0.2)
voz_dos = pygame.mixer.Sound('music/vandalos.mp3')
box = pygame.mixer.Sound('music/The_Music_Box.mp3')
voz_filo = pygame.mixer.Sound('music/epecula.mp3')
voz_ger = pygame.mixer.Sound('music/germanos.mp3')


def inicial(ventana, clock):
    py_image = None
    alpha = 0
    capture = cv2.VideoCapture('cine/animacioninit.mkv')
    ini.set_volume(0.2)
    ini.play()
    voz_ini.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ret, frame = capture.read()
        if ret:
            frame = imutils.resize(frame, width=1300, height=700)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            mode = im.mode
            size = im.size
            data = im.tobytes()
            py_image = pygame.image.fromstring(data, size, mode)

            ventana.blit(py_image, (0, 0))
        else:
            if alpha < 255:
                ventana.blit(py_image, (0, 0))
                transicion.set_alpha(alpha)
                ventana.blit(transicion, (0, 0))
                alpha += 25
            else:
                break

        pygame.display.update()
        clock.tick(9)  # va a 9


def movimientos_hunos(ventana, clock):
    done = False
    alpha = 255
    ilum = 255

    cont = 0

    anim = True
    pt_1 = True
    destello = False
    pt_2 = False

    fondo = pygame.image.load('img/mapa.png')
    rio = pygame.image.load('img/rio.png')
    romanos = pygame.image.load('img/tokenromano.png')
    hunos = pygame.image.load('img/token_huno.png')

    h_d_x = 950
    h_d_y = 50
    huno_dos = (h_d_x, h_d_y)

    h_u_x = 900
    h_u_y = 100
    huno_uno = (h_u_x, h_u_y)

    r_d_x = 565
    r_d_y = 300
    romano_dos = (r_d_x, r_d_y)

    r_u_x = 625
    r_u_y = 350
    romano_uno = (r_u_x, r_u_y)

    while not done:
        if alpha > 0 and anim:
            alpha -= 25
            ventana.blit(fondo, (0, 0))
            ventana.blit(rio, (0, 0))

            transicion.set_alpha(alpha)
            ventana.blit(transicion, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if anim:
            ventana.blit(fondo, (0, 0))
            ventana.blit(rio, (0, 0))

            ventana.blit(hunos, huno_uno)
            ventana.blit(hunos, huno_dos)

            ventana.blit(romanos, romano_uno)
            ventana.blit(romanos, romano_dos)

            if pt_1:
                h_d_x -= 2
                h_d_y += 2
                huno_dos = (h_d_x, h_d_y)

                h_u_x -= 2
                h_u_y += 2
                huno_uno = (h_u_x, h_u_y)

                if h_u_y >= 250:
                    pt_1 = False
                    destello = True
            elif destello:
                equiz.set_alpha(ilum)
                ventana.blit(equiz, (h_u_x - 65, h_u_y - 35))
                if ilum > 0:
                    ilum -= 50
                else:
                    ilum += 255
                    cont += 1
                    if cont == 3:
                        destello = False
                        pt_2 = True
            elif pt_2:
                r_d_x += 2
                r_d_y -= 2
                romano_dos = (r_d_x, r_d_y)

                r_u_x += 2
                r_u_y -= 2
                romano_uno = (r_u_x, r_u_y)

                if r_u_y <= 300:
                    anim = False
        else:
            if alpha < 255:
                transicion.set_alpha(alpha)
                ventana.blit(transicion, (0, 0))
                alpha += 25
                ini.fadeout(30)
            else:
                done = True

        pygame.display.update()
        clock.tick(20)  # es 20
    voz_ini.stop()


def no_coherencia(ventana, clock):
    alpha = 255
    done = False
    click = False
    pos_y = 0
    fondo = pygame.image.load('img/paisajebeau.png')
    no_celeb.play()
    ay = 600
    ax = 1050

    while not done:
        alpha -= 5
        if alpha < 150:
            alpha = 150

        pos_y += 10
        if pos_y > 100:
            pos_y = 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        transicion.set_alpha(alpha)
        ventana.blit(transicion, (0, 0))

        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text(ventana, "Haz dado ordenes contradictorias", 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text(ventana, "Tus aliados desconfian de tu capacidad", 80, 100, pos_y + 60, WHITE)
        Funciones_Globales.draw_text(ventana, "como lider", 80, 100, pos_y + 140, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True
            no_celeb.stop()

        pygame.display.update()
        clock.tick(20)


def croma_init(ventana, clock, score):
    global estado_croma
    done = False
    click = False
    pos_y = 0
    ay = 600
    ax = 1050

    if score == 100:
        fondo = pygame.image.load('img/paisajebeau.png')
        estado_croma = "bonito"
        texto_caida = "Has superado el nivel con exito"
        secon_text = ""
        celeb.play()
    else:
        fondo = pygame.image.load('img/paisajeugly.png')
        estado_croma = "feo"
        texto_caida = "Tus desiciones no fueron las mejores"
        secon_text = "Construiras sobre malas bases"
        no_celeb.play()

    while not done:
        pos_y += 5
        if pos_y > 100:
            pos_y = 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text(ventana, texto_caida, 60, 100, pos_y, BLACK)
        Funciones_Globales.draw_text(ventana, secon_text, 80, 100, pos_y + 60, BLACK)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True
            no_celeb.stop()
            celeb.stop()

        pygame.display.update()
        clock.tick(20)


def movimientos_vandalos(ventana, clock):
    voz_dos.play()
    done = False
    alpha = 255
    ilum = 255
    cont = 0

    anim = True
    pt_1 = True
    destello = False
    pt_2 = False
    vanda = False
    desban = True
    inil = False
    entra_hun = False
    mov1_hun = False
    mov1_van = False
    ascen_van = False
    cont_vand = False
    destello_dos = False
    duerme = True

    fondo = pygame.image.load('img/mapa.png')
    rio = pygame.image.load('img/rio.png')
    romanos = pygame.image.load('img/tokenromano.png')
    hunos = pygame.image.load('img/token_huno.png')
    vandalos = pygame.image.load('img/token_vandalo.png')

    h_d_x = 950
    h_d_y = 50
    huno_dos = (h_d_x, h_d_y)

    h_u_x = 900
    h_u_y = 100
    huno_uno = (h_u_x, h_u_y)

    r_d_x = 565
    r_d_y = 300
    romano_dos = (r_d_x, r_d_y)

    r_u_x = 625
    r_u_y = 350
    romano_uno = (r_u_x, r_u_y)

    v_d_x = 600
    v_d_y = 50
    vandalo_dos = (v_d_x, v_d_y)

    v_u_x = 600
    v_u_y = 100
    vandalo_uno = (v_u_x, v_u_y)

    while not done:
        if desban:
            if alpha > 0 and anim:

                alpha -= 5
                ventana.blit(fondo, (0, 0))
                ventana.blit(rio, (0, 0))

                ventana.blit(hunos, huno_uno)
                ventana.blit(hunos, huno_dos)

                ventana.blit(romanos, romano_uno)
                ventana.blit(romanos, romano_dos)

                ventana.blit(vandalos, vandalo_uno)
                ventana.blit(vandalos, vandalo_dos)

                transicion.set_alpha(alpha)
                ventana.blit(transicion, (0, 0))

                if alpha <= 1:
                    desban = False
                    inil = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if inil:

            if anim:
                ventana.blit(fondo, (0, 0))
                ventana.blit(rio, (0, 0))

                ventana.blit(hunos, huno_uno)
                ventana.blit(hunos, huno_dos)

                ventana.blit(romanos, romano_uno)
                ventana.blit(romanos, romano_dos)

                ventana.blit(vandalos, vandalo_uno)
                ventana.blit(vandalos, vandalo_dos)

                if pt_1:
                    h_d_x -= 2
                    h_d_y += 2
                    huno_dos = (h_d_x, h_d_y)

                    h_u_x -= 2
                    h_u_y += 2
                    huno_uno = (h_u_x, h_u_y)

                    if h_u_y >= 250:
                        pt_1 = False
                        destello = True
                elif destello:
                    equiz.set_alpha(ilum)
                    ventana.blit(equiz, (h_u_x - 65, h_u_y - 35))
                    if ilum > 0:
                        ilum -= 50
                    else:
                        ilum += 255
                        cont += 1
                        if cont == 6:
                            destello = False
                            pt_2 = True
                elif pt_2:
                    r_d_x += 2
                    r_d_y -= 2
                    romano_dos = (r_d_x, r_d_y)

                    r_u_x += 2
                    r_u_y -= 2
                    romano_uno = (r_u_x, r_u_y)

                    if r_u_y <= 300:
                        pt_2 = False
                        vanda = True

                elif vanda:
                    v_d_x += 2
                    v_d_y += 2
                    vandalo_dos = (v_d_x, v_d_y)

                    v_u_x += 2
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)
                    if v_u_y >= 200:
                        r_d_x = -100
                        r_d_y = 0
                        romano_dos = (r_d_x, r_d_y)
                        r_u_x = -100
                        r_u_y = 0
                        romano_uno = (r_u_x, r_u_y)
                        vanda = False
                        entra_hun = True

                elif entra_hun:
                    h_d_x -= 2
                    h_d_y += 2
                    huno_dos = (h_d_x, h_d_y)

                    h_u_x -= 2
                    h_u_y += 2
                    huno_uno = (h_u_x, h_u_y)

                    if h_u_y >= 300:
                        entra_hun = False
                        mov1_hun = True
                elif mov1_hun:
                    h_u_x -= 3
                    h_u_y -= 2
                    huno_uno = (h_u_x, h_u_y)
                    if h_u_y <= 250:
                        h_u_y = 250

                        h_d_x -= 2
                        h_d_y += 2
                        huno_dos = (h_d_x, h_d_y)
                        if h_d_y >= 300:
                            h_d_y = 300
                            h_d_x = 700
                            huno_dos = (h_d_x, h_d_y)

                        if h_u_x <= 450:
                            h_u_x = 450
                            mov1_hun = False
                            mov1_van = True

                elif mov1_van:
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)

                    v_d_y += 2
                    vandalo_dos = (v_d_x, v_d_y)
                    if v_u_y >= 300:
                        v_d_y = 250
                        v_u_y = 300
                        vandalo_uno = (v_u_x, v_u_y)
                        vandalo_dos = (v_d_x, v_d_y)
                        mov1_van = False
                        ascen_van = True
                elif ascen_van:
                    v_u_x -= 3
                    v_u_y -= 2
                    vandalo_uno = (v_u_x, v_u_y)
                    v_d_x -= 3
                    v_d_y -= 2
                    vandalo_dos = (v_d_x, v_d_y)
                    if v_u_y <= 250:
                        v_u_y = 250
                        v_d_y = 200
                        if v_u_x <= 350:
                            ascen_van = False
                            cont_vand = True

                elif cont_vand:
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)

                    if v_u_y >= 400:
                        v_u_y = 400
                        cont_vand = False
                        destello_dos = True

                elif destello_dos:
                    equiz.set_alpha(ilum)
                    ventana.blit(equiz, (v_u_x - 65, v_u_y - 35))
                    ventana.blit(equiz, (v_d_x - 65, v_d_y - 35))
                    if ilum > 0:
                        ilum -= 50
                    else:
                        ilum += 255
                        cont += 1
                        if cont == 16:
                            destello_dos = False
                            anim = False

            else:
                if duerme:
                    time.sleep(9)
                    duerme = False
                if alpha < 255:
                    transicion.set_alpha(alpha)
                    ventana.blit(transicion, (0, 0))
                    alpha += 25
                    ini.fadeout(30)
                else:
                    done = True

        pygame.display.update()
        clock.tick(20)  # es 20
    voz_ini.stop()


def movimientos_germanos(ventana, clock):
    import anuncio
    voz_ger.play()
    done = False
    alpha = 255
    ilum = 255
    cont = 0

    anim = True
    pt_1 = True
    destello = False
    pt_2 = False
    vanda = False
    desban = True
    inil = False
    entra_hun = False
    mov1_hun = False
    mov1_van = False
    ascen_van = False
    cont_vand = False
    destello_dos = False
    ok = True
    tat = False

    mv_ger = False

    fondo = pygame.image.load('img/mapa.png')
    rio = pygame.image.load('img/rio.png')
    romanos = pygame.image.load('img/tokenromano.png')
    hunos = pygame.image.load('img/token_huno.png')
    vandalos = pygame.image.load('img/token_vandalo.png')
    germanos = pygame.image.load('img/germanos.png')

    h_d_x = 950
    h_d_y = 50
    huno_dos = (h_d_x, h_d_y)

    h_u_x = 900
    h_u_y = 100
    huno_uno = (h_u_x, h_u_y)

    r_d_x = 565
    r_d_y = 300
    romano_dos = (r_d_x, r_d_y)

    r_u_x = 625
    r_u_y = 350
    romano_uno = (r_u_x, r_u_y)

    v_d_x = 600
    v_d_y = 50
    vandalo_dos = (v_d_x, v_d_y)

    v_u_x = 600
    v_u_y = 100
    vandalo_uno = (v_u_x, v_u_y)

    g_d_x = 550
    g_d_y = 50
    germano_dos = (g_d_x, g_d_y)

    g_u_x = 550
    g_u_y = 100
    germano_uno = (g_u_x, g_u_y)

    while not done:
        if desban:
            if alpha > 0 and anim:

                alpha -= 5
                ventana.blit(fondo, (0, 0))
                ventana.blit(rio, (0, 0))

                ventana.blit(hunos, huno_uno)
                ventana.blit(hunos, huno_dos)

                ventana.blit(romanos, romano_uno)
                ventana.blit(romanos, romano_dos)

                ventana.blit(vandalos, vandalo_uno)
                ventana.blit(vandalos, vandalo_dos)

                ventana.blit(germanos, germano_uno)
                ventana.blit(germanos, germano_dos)

                transicion.set_alpha(alpha)
                ventana.blit(transicion, (0, 0))

                if alpha <= 1:
                    desban = False
                    inil = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if inil:

            if anim:
                ventana.blit(fondo, (0, 0))
                ventana.blit(rio, (0, 0))

                ventana.blit(hunos, huno_uno)
                ventana.blit(hunos, huno_dos)

                ventana.blit(romanos, romano_uno)
                ventana.blit(romanos, romano_dos)

                ventana.blit(vandalos, vandalo_uno)
                ventana.blit(vandalos, vandalo_dos)

                ventana.blit(germanos, germano_uno)
                ventana.blit(germanos, germano_dos)

                if pt_1:
                    h_d_x -= 2
                    h_d_y += 2
                    huno_dos = (h_d_x, h_d_y)

                    h_u_x -= 2
                    h_u_y += 2
                    huno_uno = (h_u_x, h_u_y)

                    if h_u_y >= 250:
                        pt_1 = False
                        destello = True
                elif destello:
                    equiz.set_alpha(ilum)
                    ventana.blit(equiz, (h_u_x - 65, h_u_y - 35))
                    if ilum > 0:
                        ilum -= 50
                    else:
                        ilum += 255
                        cont += 1
                        if cont == 6:
                            destello = False
                            pt_2 = True
                elif pt_2:
                    r_d_x += 2
                    r_d_y -= 2
                    romano_dos = (r_d_x, r_d_y)

                    r_u_x += 2
                    r_u_y -= 2
                    romano_uno = (r_u_x, r_u_y)

                    if r_u_y <= 300:
                        pt_2 = False
                        vanda = True

                elif vanda:
                    v_d_x += 2
                    v_d_y += 2
                    vandalo_dos = (v_d_x, v_d_y)

                    v_u_x += 2
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)
                    if v_u_y >= 200:
                        r_d_x = -100
                        r_d_y = 0
                        romano_dos = (r_d_x, r_d_y)
                        r_u_x = -100
                        r_u_y = 0
                        romano_uno = (r_u_x, r_u_y)
                        vanda = False
                        entra_hun = True

                elif entra_hun:
                    h_d_x -= 2
                    h_d_y += 2
                    huno_dos = (h_d_x, h_d_y)

                    h_u_x -= 2
                    h_u_y += 2
                    huno_uno = (h_u_x, h_u_y)

                    if h_u_y >= 300:
                        entra_hun = False
                        mov1_hun = True
                elif mov1_hun:
                    h_u_x -= 3
                    h_u_y -= 2
                    huno_uno = (h_u_x, h_u_y)
                    if h_u_y <= 250:
                        h_u_y = 250

                        h_d_x -= 2
                        h_d_y += 2
                        huno_dos = (h_d_x, h_d_y)
                        if h_d_y >= 300:
                            h_d_y = 300
                            h_d_x = 700
                            huno_dos = (h_d_x, h_d_y)

                        if h_u_x <= 450:
                            h_u_x = 450
                            mov1_hun = False
                            mov1_van = True

                elif mov1_van:
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)

                    v_d_y += 2
                    vandalo_dos = (v_d_x, v_d_y)
                    if v_u_y >= 300:
                        v_d_y = 250
                        v_u_y = 300
                        vandalo_uno = (v_u_x, v_u_y)
                        vandalo_dos = (v_d_x, v_d_y)
                        mov1_van = False
                        ascen_van = True
                elif ascen_van:
                    v_u_x -= 3
                    v_u_y -= 2
                    vandalo_uno = (v_u_x, v_u_y)
                    v_d_x -= 3
                    v_d_y -= 2
                    vandalo_dos = (v_d_x, v_d_y)
                    if v_u_y <= 250:
                        v_u_y = 250
                        v_d_y = 200
                        if v_u_x <= 350:
                            ascen_van = False
                            cont_vand = True

                elif cont_vand:
                    v_u_y += 2
                    vandalo_uno = (v_u_x, v_u_y)

                    if v_u_y >= 400:
                        v_u_y = 400
                        cont_vand = False
                        destello_dos = True

                elif destello_dos:
                    equiz.set_alpha(ilum)
                    ventana.blit(equiz, (v_u_x - 65, v_u_y - 35))
                    ventana.blit(equiz, (v_d_x - 65, v_d_y - 35))
                    if ilum > 0:
                        ilum -= 50
                    else:
                        ilum += 255
                        cont += 1
                        if cont == 16:
                            # destello_dos = False
                            mv_ger = True

                    while mv_ger:
                        tat = True
                        ventana.blit(fondo, (0, 0))
                        ventana.blit(rio, (0, 0))

                        ventana.blit(hunos, huno_uno)
                        ventana.blit(hunos, huno_dos)

                        ventana.blit(romanos, romano_uno)
                        ventana.blit(romanos, romano_dos)

                        ventana.blit(vandalos, vandalo_uno)
                        ventana.blit(vandalos, vandalo_dos)

                        ventana.blit(germanos, germano_uno)
                        ventana.blit(germanos, germano_dos)

                        Funciones_Globales.dialog(
                            "A sabiendas que esta cultura permea al imperio el emperador ",
                            "decide recordar cuales son los mayores avances de la cultura ",
                            "romana y es escrito en pergaminos para que se pueda perpetuar ese legado:")

                        if g_d_x > 350:
                            g_d_x -= 2
                            germano_dos = (g_d_x, g_d_y)
                        else:
                            mv_ger = False
                        if g_u_y < 250:
                            g_u_y += 2
                            germano_uno = (g_u_x, g_u_y)

                        pygame.display.update()
                        clock.tick(30)
                    if tat:
                        anim = False

            else:
                while ok:
                    Funciones_Globales.papoir2("", "H", (0, 0), anuncio.texto(0),
                                               anuncio.stext(0),
                                               anuncio.sstext(0),
                                               anuncio.ssstext(0),
                                               anuncio.sssstext(0),
                                               anuncio.ssssstext(0),
                                               anuncio.sssssstext(0),
                                               anuncio.ssssssstext(0),
                                               anuncio.sssssssstext(0),
                                               anuncio.ssssssssstext(0),
                                               anuncio.sssssssssstext(0),
                                               anuncio.ssssssssssstext(0),
                                               anuncio.sssssssssssstext(0))
                    pygame.display.update()
                    clock.tick(20)
                    ok = False
                    time.sleep(40)

                if alpha < 255:
                    transicion.set_alpha(alpha)
                    ventana.blit(transicion, (0, 0))
                    alpha += 25
                    ini.fadeout(20)
                else:
                    done = True

        pygame.display.update()
        clock.tick(20)  # es 20
    voz_ini.stop()


def filosofo(ventana, clock):
    star = pygame.image.load('img/door.jpg')
    mid = pygame.image.load('img/road.jpg')
    fin = pygame.image.load('img/montana.jpg')

    voz_filo.play()

    done = False
    cambio = False
    des_sta = False

    espe2 = False
    espe3 = False

    des_mi = False
    des_fi = False

    aux = True
    alfa = 255
    mi_al = 255
    fi_al = 255

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if espe3:
            time.sleep(23)
            espe3 = False
            des_fi = True

        if espe2:
            time.sleep(22)
            espe2 = False
            des_mi = True

        if cambio:
            time.sleep(22)
            cambio = False
            des_sta = True

        if des_sta:
            alfa -= 5
            if alfa <= 0:
                espe2 = True
                des_sta = False

        if des_mi:
            mi_al -= 5
            if mi_al <= 0:
                espe3 = True
                des_mi = False

        if des_fi:
            fi_al -= 5
            if fi_al <= 0:
                done = True

        fin.set_alpha(fi_al)
        mid.set_alpha(mi_al)
        star.set_alpha(alfa)
        ventana.blit(transicion, (0, 0))
        ventana.blit(fin, (0, 0))
        ventana.blit(mid, (0, 0))
        ventana.blit(star, (0, 0))

        if aux:
            cambio = True
            aux = False

        pygame.display.update()
        clock.tick(20)


def croma_level1(ventana, clock, bases):
    if bases == "bonito":
        fondo = pygame.image.load('img/paisajebeau.png')  # fondo
    else:
        fondo = pygame.image.load('img/paisajeugly.png')  # fondo

    alpha = 255
    alfa = 0
    ilum = 255

    done = False
    click = False
    pos_y = 0
    ay = 600
    ax = 1050

    texto_caida = "Felicidades, la ciudad empieza a ser construida"
    secon_text = "Nivel superado "

    pygame.mixer.music.pause()
    celeb.play()

    while not done:
        while alpha > 0:
            alpha -= 25
            ventana.blit(fondo, (0, 0))

            transicion.set_alpha(alpha)
            ventana.blit(transicion, (0, 0))

            pygame.display.update()
            clock.tick(20)

        pos_y += 5
        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))

        ventana.blit(acueducto, (0, 0))
        sombra_acueducto.set_alpha(ilum)
        ventana.blit(sombra_acueducto, (0, 0))

        ilum -= 10

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text2(ventana, texto_caida, 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text2(ventana, secon_text, 80, 100, pos_y + 60, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            while alfa < 255:
                transicion.set_alpha(alfa)
                ventana.blit(transicion, (0, 0))
                alfa += 25
                # ini.fadeout(30)
                pygame.display.update()
                clock.tick(20)
            done = True
            celeb.stop()

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()


def croma_level2(ventana, clock, bases):
    if bases == "bonito":
        fondo = pygame.image.load('img/paisajebeau.png')  # fondo
    else:
        fondo = pygame.image.load('img/paisajeugly.png')  # fondo

    alpha = 255
    alfa = 0
    ilum = 255

    done = False
    click = False
    pos_y = 0
    ay = 600
    ax = 1050

    texto_caida = "La arquitectura cada dia va aumentando"
    secon_text = "Nivel superado "

    pygame.mixer.music.pause()
    celeb.play()

    while not done:
        while alpha > 0:
            alpha -= 25
            ventana.blit(fondo, (0, 0))
            ventana.blit(acueducto, (0, 0))

            transicion.set_alpha(alpha)
            ventana.blit(transicion, (0, 0))

            pygame.display.update()
            clock.tick(20)

        pos_y += 5
        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        ventana.blit(acueducto, (0, 0))

        sombra_templo.set_alpha(ilum)
        ventana.blit(templo, (0, 0))
        ventana.blit(sombra_templo, (0, 0))

        ilum -= 10

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text2(ventana, texto_caida, 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text2(ventana, secon_text, 80, 100, pos_y + 60, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            while alfa < 255:
                transicion.set_alpha(alfa)
                ventana.blit(transicion, (0, 0))
                alfa += 25
                # ini.fadeout(30)
                pygame.display.update()
                clock.tick(20)
            done = True
            celeb.stop()

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()


def croma_level3(ventana, clock, bases, score):
    if bases == "bonito":
        fondo = pygame.image.load('img/paisajebeau.png')  # fondo
    else:
        fondo = pygame.image.load('img/paisajeugly.png')  # fondo

    alpha = 255
    alfa = 0
    ilum = 255

    done = False
    click = False
    pos_y = 0
    ay = 600
    ax = 1050

    texto_caida = "Que grandioso monumento hay ahora en la ciudad"
    secon_text = "Nivel superado "

    pygame.mixer.music.pause()
    celeb.play()

    while not done:
        while alpha > 0:
            alpha -= 25
            ventana.blit(fondo, (0, 0))
            ventana.blit(acueducto, (0, 0))
            ventana.blit(templo, (0, 0))

            transicion.set_alpha(alpha)
            ventana.blit(transicion, (0, 0))

            pygame.display.update()
            clock.tick(20)

        pos_y += 5
        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        ventana.blit(acueducto, (0, 0))
        ventana.blit(templo, (0, 0))

        sombra_coliseo.set_alpha(ilum)
        ventana.blit(coliseo, (0, 0))
        ventana.blit(sombra_coliseo, (0, 0))

        ilum -= 10

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text2(ventana, texto_caida, 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text2(ventana, secon_text, 80, 100, pos_y + 60, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            while alfa < 255:
                transicion.set_alpha(alfa)
                ventana.blit(transicion, (0, 0))
                alfa += 25
                # ini.fadeout(30)
                pygame.display.update()
                clock.tick(20)
            done = True
            celeb.stop()
            if score == 109:
                unlock_all_croma(ventana, clock, bases)

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()


def unlock_all_croma(ventana, clock, bases):
    global marco_au
    marco_au = True
    if bases == "bonito":
        fondo = pygame.image.load('img/paisajebeau.png')  # fondo
    else:
        fondo = pygame.image.load('img/paisajeugly.png')  # fondo

    alpha = 255
    alfa = 0
    ilum = 255

    done = False
    click = False
    pos_y = 0
    ay = 600
    ax = 1050

    texto_caida = "La ciudad ahora esta en su maximo esplendor"
    secon_text = "Juego superado "

    pygame.mixer.music.pause()
    celeb.play()

    while not done:
        while alpha > 0:
            alpha -= 25
            ventana.blit(fondo, (0, 0))
            ventana.blit(acueducto, (0, 0))
            ventana.blit(templo, (0, 0))
            ventana.blit(coliseo, (0, 0))

            transicion.set_alpha(alpha)
            ventana.blit(transicion, (0, 0))

            pygame.display.update()
            clock.tick(20)

        pos_y += 5
        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        ventana.blit(acueducto, (0, 0))
        ventana.blit(templo, (0, 0))
        ventana.blit(coliseo, (0, 0))

        sombra_estatua.set_alpha(ilum)
        ventana.blit(estatua, (0, 0))
        ventana.blit(sombra_estatua, (0, 0))

        ilum -= 10

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        Funciones_Globales.draw_text2(ventana, texto_caida, 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text2(ventana, secon_text, 80, 100, pos_y + 60, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            while alfa < 255:
                transicion.set_alpha(alfa)
                ventana.blit(transicion, (0, 0))
                alfa += 25
                # ini.fadeout(30)
                pygame.display.update()
                clock.tick(20)
            done = True
            celeb.stop()

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()


def lose(ventana, clock, score, bases):
    pygame.mixer.music.stop()
    if croma1:
        if bases == "bonito":
            fondo = pygame.image.load('img/Mapabonito.png')  # fondo
        else:
            fondo = pygame.image.load('img/Mapafeo.png')  # fondo
    else:
        if bases == "bonito":
            fondo = pygame.image.load('img/paisajebeau.png')  # fondo
        else:
            fondo = pygame.image.load('img/paisajeugly.png')
    global estado_croma

    llorar.play()

    alpha = 255
    alfa = pygame.image.load('img/black_screen.png')
    done = False
    click = False
    pos_y = 0

    ay = 600
    ax = 1050
    llorar.play()

    while not done:

        alpha -= 5
        if alpha < 150:
            alpha = 150

        pos_y += 5
        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        if croma1:
            pass
        elif croma2:
            ventana.blit(acueducto, (0, 0))
            ventana.blit(arbol, (0, 0))
        elif croma3:
            ventana.blit(acueducto, (0, 0))
            ventana.blit(templo, (0, 0))
        else:
            ventana.blit(acueducto, (0, 0))
            ventana.blit(templo, (0, 0))
            ventana.blit(coliseo, (0, 0))

        alfa.set_alpha(alpha)
        ventana.blit(alfa, (0, 0))

        Funciones_Globales.draw_text(ventana, "Haz Perdido", 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text(ventana, "Tus aliados desconfian de tu capacidad", 80, 100, pos_y + 60, WHITE)
        Funciones_Globales.draw_text(ventana, "como lider", 80, 100, pos_y + 140, WHITE)

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Volver", 40, ax + 60, ay + 20, WHITE)

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, WHITE)
        Funciones_Globales.barra_progreso(score)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True
            llorar.stop()

        pygame.display.update()
        clock.tick(20)


def win(ventana, clock):
    pygame.mixer.music.stop()
    box.play()
    fondo = pygame.image.load('img/spartan.jpg')
    import Conclusiones

    algo = 0

    derecha = False
    izquierda = False

    click = False
    done = False

    ay = 600
    ax = 1050

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    derecha = True
                elif event.key == pygame.K_LEFT:
                    izquierda = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    derecha = False
                elif event.key == pygame.K_LEFT:
                    izquierda = False

        if derecha:
            algo += 1
        elif izquierda:
            algo -= 1
        if algo < 0:
            algo = 0
        elif algo > 1:
            algo = 1

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))
        acept = ventana.blit(letre, (-100, -100))

        ventana.blit(fondo, (0, 0))

        Funciones_Globales.dialog(Conclusiones.texto(algo), Conclusiones.stext(algo), Conclusiones.sstext(algo))

        if algo == 1:
            pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

            acept = ventana.blit(letre, (ax, ay))
            Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True

        pygame.display.update()
        clock.tick(20)


def estado_final(ventana, clock, score, bases):
    if croma1:
        if bases == "bonito":
            fondo = pygame.image.load('img/Mapabonito.png')  # fondo
        else:
            fondo = pygame.image.load('img/Mapafeo.png')  # fondo
    else:
        if bases == "bonito":
            fondo = pygame.image.load('img/paisajebeau.png')  # fondo
        else:
            fondo = pygame.image.load('img/paisajeugly.png')
    global estado_croma

    alpha = 255
    alfa = pygame.image.load('img/black_screen.png')
    done = False
    click = False
    pos_y = 0

    ay = 600
    ax = 1050
    llorar.play()

    while not done:

        alpha -= 5

        if pos_y > 100:
            pos_y = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))

        ventana.blit(fondo, (0, 0))
        if marco_au:
            ventana.blit(acueducto, (0, 0))
            ventana.blit(templo, (0, 0))
            ventana.blit(coliseo, (0, 0))
            ventana.blit(estatua, (0, 0))
        else:

            if croma1:
                pass
            elif croma2:
                ventana.blit(acueducto, (0, 0))
                ventana.blit(arbol, (0, 0))
            elif croma3:
                ventana.blit(acueducto, (0, 0))
                ventana.blit(templo, (0, 0))
            else:
                ventana.blit(acueducto, (0, 0))
                ventana.blit(templo, (0, 0))
                ventana.blit(coliseo, (0, 0))

        alfa.set_alpha(alpha)
        ventana.blit(alfa, (0, 0))

        Funciones_Globales.draw_text(ventana, "Finalizado", 60, 100, pos_y, WHITE)
        Funciones_Globales.draw_text(ventana, "Estos son tus resultados", 80, 100, pos_y + 60, WHITE)
        Funciones_Globales.draw_text(ventana, "como lider", 80, 100, pos_y + 140, WHITE)

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))
        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Volver", 40, ax + 60, ay + 20, WHITE)

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, WHITE)
        Funciones_Globales.barra_progreso(score)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True
            box.stop()

        pygame.display.update()
        clock.tick(20)


def base():
    return estado_croma


def selec_croma(ventana, clock, bases):
    global croma1, croma2, croma3

    if croma1:
        croma_level1(ventana, clock, bases)  # acueducto
        croma1 = False
        croma2 = True
    elif croma2:
        croma_level2(ventana, clock, bases)  # templo
        croma2 = False
        croma3 = True


def descargo(ventana, clock):
    fondo = pygame.image.load('img/door.jpg')

    click = False
    done = False

    ay = 600
    ax = 1050

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))
        acept = ventana.blit(letre, (-100, -100))

        ventana.blit(fondo, (0, 0))
        transicion.set_alpha(150)
        ventana.blit(transicion, (0, 0))

        Funciones_Globales.draw_text(ventana, "Obra: Sevilla Música de https://www.fiftysounds.com/es/", 30, 0, 0, WHITE)
        Funciones_Globales.draw_text(ventana, "Obra: Micronesia Música de https://www.fiftysounds.com/es/", 30, 0, 0+30, WHITE)
        Funciones_Globales.draw_text(ventana, "Obra: La Revelación Música de https://www.fiftysounds.com/es/", 30, 0, 0+30+30, WHITE)
        Funciones_Globales.draw_text(ventana, "Obra: La Caja de Música Música de https://www.fiftysounds.com/es/", 30, 0, 0+30+30+30, WHITE)
        Funciones_Globales.draw_text(ventana, "Obra: Susurros Música de https://www.fiftysounds.com/es/", 30, 0, 0+30+30+30+30, WHITE)
        Funciones_Globales.draw_text(ventana, "Obra: Pasajeros Música de https://www.fiftysounds.com/es/", 30, 0, 0+30+30+30+30+30, WHITE)

        pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

        acept = ventana.blit(letre, (ax, ay))
        Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

        if mouse.colliderect(acept):
            ay = 600 - 5
            ax = 1050 - 5
            touch_a = True
        else:
            ay = 600
            ax = 1050
            touch_a = False

        if touch_a and click:
            done = True

        pygame.display.update()
        clock.tick(20)
