import pygame
import Funciones_Globales
import Master_tres
import List_respon_tres


fondo = pygame.image.load('img/mapa.png')  # fondo
dark = pygame.image.load('img/papironegro.png')

codsx = 0
codsy = -300
mi_resp_es = None
algo = 0
resp_de_un = None
resp_de_dos = None
BLACK = (0, 0, 0)

point = None


def nivel(ventana, clock, score):
    global codsx, codsy, mi_resp_es, algo, resp_de_un, point

    cordpap1 = (250, 100)

    cordpap2 = (750, 100)

    cordpap3 = (250, 300)

    cordpap4 = (750, 300)

    election = False
    derecha = False
    izquierda = False
    espacio = False
    n_uno = False
    n_dos = False
    n_tres = False
    n_cuatro = False
    estoy_en = None
    retu = False
    done = False

    respuest = Funciones_Globales.lista_nivel_dos()

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
                elif event.key == pygame.K_3:
                    n_tres = True
                elif event.key == pygame.K_4:
                    n_cuatro = True
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
                elif event.key == pygame.K_3:
                    n_tres = False
                elif event.key == pygame.K_4:
                    n_cuatro = False
                if event.key == pygame.K_RETURN:
                    retu = False

        if derecha:
            algo += 1
        elif izquierda:
            algo -= 1
        if algo < 0:
            algo = 0
        elif algo > 2:
            algo = 2
        if n_uno and election:
            codsx = cordpap1[0]
            codsy = cordpap1[1]
            estoy_en = 1
        elif n_dos and election:
            codsx = cordpap2[0]
            codsy = cordpap2[1]
            estoy_en = 2
        elif n_tres and election:
            codsx = cordpap3[0]
            codsy = cordpap3[1]
            estoy_en = 3
        elif n_cuatro and election:
            codsx = cordpap4[0]
            codsy = cordpap4[1]
            estoy_en = 4

        ventana.blit(fondo, (0, 0))

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, BLACK)

        if algo == 2 and espacio:
            election = True
            algo = 0

        if election:
            destell = pygame.image.load('img/destello.png')
            destell.set_alpha(0)
            prev = ventana.blit(destell, (codsx, codsy))

            uno = ventana.blit(dark, (250, 100))
            Funciones_Globales.papoir("1", "Close", cordpap1, "", "", "", "", "", "")
            dos = ventana.blit(dark, (750, 100))
            Funciones_Globales.papoir("2", "Close", cordpap2, "", "", "", "", "", "")
            tres = ventana.blit(dark, (250, 300))
            Funciones_Globales.papoir("3", "Close", cordpap3, "", "", "", "", "", "")
            cuatro = ventana.blit(dark, (750, 300))
            Funciones_Globales.papoir("4", "Close", cordpap4, "", "", "", "", "", "")

            if prev.colliderect(uno):
                cordpap1 = (240, 90)

            else:
                cordpap1 = (250, 100)

            if prev.colliderect(dos):
                cordpap2 = (760, 90)

            else:
                cordpap2 = (750, 100)

            if prev.colliderect(tres):
                cordpap3 = (240, 310)

            else:
                cordpap3 = (250, 300)

            if prev.colliderect(cuatro):
                cordpap4 = (760, 310)

            else:
                cordpap4 = (750, 300)

        # dialogo master
        Funciones_Globales.dialog(Master_tres.texto(algo), Master_tres.stext(algo), Master_tres.sstext(algo))

        if algo == 2:
            Funciones_Globales.acept()

        Funciones_Globales.barra_progreso(score)

        if estoy_en == 1 and espacio:
            Funciones_Globales.papoir("1", "Open", (0, 0), List_respon_tres.texto(respuest[0]), List_respon_tres.stext(
                respuest[0]),
                                      List_respon_tres.sstext(respuest[0]),
                                      List_respon_tres.ssstext(respuest[0]),
                                      List_respon_tres.sssstext(respuest[0]),
                                      List_respon_tres.ssssstext(respuest[0]))
            mi_resp_es = List_respon_tres.stext(respuest[0])
        elif estoy_en == 2 and espacio:
            Funciones_Globales.papoir("2", "Open", (0, 0), List_respon_tres.texto(respuest[1]), List_respon_tres.stext(
                respuest[1]),
                                      List_respon_tres.sstext(respuest[1]),
                                      List_respon_tres.ssstext(respuest[1]),
                                      List_respon_tres.sssstext(respuest[1]),
                                      List_respon_tres.ssssstext(respuest[1]))
            mi_resp_es = List_respon_tres.stext(respuest[1])
        elif estoy_en == 3 and espacio:
            Funciones_Globales.papoir("3", "Open", (0, 0), List_respon_tres.texto(respuest[2]), List_respon_tres.stext(
                respuest[2]),
                                      List_respon_tres.sstext(respuest[2]),
                                      List_respon_tres.ssstext(respuest[2]),
                                      List_respon_tres.sssstext(respuest[2]),
                                      List_respon_tres.ssssstext(respuest[2]))
            mi_resp_es = List_respon_tres.stext(respuest[2])
        elif estoy_en == 4 and espacio:
            Funciones_Globales.papoir("4", "Open", (0, 0), List_respon_tres.texto(respuest[3]), List_respon_tres.stext(
                respuest[3]),
                                      List_respon_tres.sstext(respuest[3]),
                                      List_respon_tres.ssstext(respuest[3]),
                                      List_respon_tres.sssstext(respuest[3]),
                                      List_respon_tres.ssssstext(respuest[3]))
            mi_resp_es = List_respon_tres.stext(respuest[3])

        if espacio and retu:
            if mi_resp_es == List_respon_tres.stext(3):
                score += 25
                done = True
            elif mi_resp_es == List_respon_tres.stext(0):
                score -= 25
                done = True
            elif mi_resp_es == List_respon_tres.stext(1) or mi_resp_es == List_respon_tres.stext(2):
                score += 10
                done = True

        point = score

        pygame.display.update()
        clock.tick(10)


def points():
    return point
