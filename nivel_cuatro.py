import pygame
import Funciones_Globales
import Master_cuatro

# import Respuestas_Desiciones

letre = pygame.image.load('img/letrero.png')
dark = pygame.image.load('img/papironegro.png')

siu = ""
nou = ""

sid = ""
nod = ""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

point = None
hablan = True
election = False


def hay_que_desidir(vamos_en):
    global siu, nou, sid, nod

    if vamos_en == "1":

        siu = "Presidente"
        sid = ""

        nou = "Monarca"
        nod = ""
    elif vamos_en == "2":

        siu = "Congreso de "
        sid = "la Republica"

        nou = "Senado romano"
        nod = ""
    elif vamos_en == "3":

        siu = "Voto Universal"
        sid = ""

        nou = "Voto solo para "
        nod = "ciudadanos Romanos"
    elif vamos_en == "4":

        siu = "Departamentos "
        sid = "y municipios"

        nou = "Provincias "
        nod = "Imperiales"
    elif vamos_en == "5":

        siu = "Libertad "
        sid = "de culto"

        nou = "Cristianismo"
        nod = ""


def desicion(ventana, clock, score):
    fondo = pygame.image.load('img/mapa.png')

    global point, hablan, election

    codsx = 0
    codsy = - 100

    mi_resp_es = None
    algo = 0

    cordpap1 = (100, 200)
    cordpap2 = (800, 200)

    izquierda = False
    derecha = False

    espacio = False
    n_uno = False
    n_dos = False

    estoy_en = None

    retu = False
    done = False

    if score >= 100:
        score -= 50
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    derecha = True
                elif event.key == pygame.K_LEFT:
                    izquierda = True
                elif event.key == pygame.K_SPACE:
                    espacio = True
                elif event.key == pygame.K_1:
                    n_uno = True
                elif event.key == pygame.K_2:
                    n_dos = True
                if event.key == pygame.K_RETURN:
                    retu = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    derecha = False
                elif event.key == pygame.K_LEFT:
                    izquierda = False
                elif event.key == pygame.K_SPACE:
                    espacio = False
                elif event.key == pygame.K_1:
                    n_uno = False
                elif event.key == pygame.K_2:
                    n_dos = False
                if event.key == pygame.K_RETURN:
                    retu = False

        if derecha:
            algo += 1
        elif izquierda:
            algo -= 1
        if algo < 0:
            algo = 0
        elif algo > 0:
            algo = 0
        if n_uno and election:
            codsx = cordpap1[0]
            codsy = cordpap1[1]
            estoy_en = 1
        elif n_dos and election:
            codsx = cordpap2[0]
            codsy = cordpap2[1]
            estoy_en = 2

        ventana.blit(fondo, (0, 0))

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, BLACK)

        if election:
            hablan = False

            destell = pygame.image.load('img/destello.png')
            destell.set_alpha(0)
            prev = ventana.blit(destell, (codsx, codsy))

            uno = pygame.draw.rect(ventana, BLACK, (100, 200, 439, 150))
            ventana.blit(letre, cordpap1)
            Funciones_Globales.dess2(siu, sid, cordpap1)

            dos = pygame.draw.rect(ventana, BLACK, (800, 200, 439, 150))
            ventana.blit(letre, cordpap2)
            Funciones_Globales.dess2(nou, nod, cordpap2)

            if prev.colliderect(uno):
                cordpap1 = (90, 190)

            else:
                cordpap1 = (100, 200)

            if prev.colliderect(dos):
                cordpap2 = (790, 190)

            else:
                cordpap2 = (800, 200)

        # dialogo master

        if hablan:
            Funciones_Globales.dialog(Master_cuatro.texto(algo), Master_cuatro.stext(algo),
                                      Master_cuatro.sstext(algo))
        if algo == 0:
            Funciones_Globales.acept()

        Funciones_Globales.barra_progreso(score)

        if algo == 0 and espacio:
            algo = 2
            election = True

        if estoy_en == 1:
            mi_resp_es = "si"

        elif estoy_en == 2:
            mi_resp_es = "no"

        if retu:
            if mi_resp_es == "si":
                score += 9
                done = True
            elif mi_resp_es == "no":
                score -= 50
                done = True

        point = score

        pygame.display.update()
        clock.tick(10)


def points():
    return point
