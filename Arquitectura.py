import pygame
import Funciones_Globales
import Master_Arco
import Respuestas_arco


dark = pygame.image.load('img/papironegro.png')
letre = pygame.image.load('img/letrero.png')

codsx = 0
codsy = -300
mi_resp_es = None
algo = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
contin = True
point = None


def donde_vamos(vamos_en):
    correcta = None
    if vamos_en == "arco":
        correcta = Respuestas_arco.sstext(0)
    elif vamos_en == "acueducto":
        correcta = Respuestas_arco.sstext(1)
    elif vamos_en == "templo":
        correcta = Respuestas_arco.sstext(2)
    elif vamos_en == "termas":
        correcta = Respuestas_arco.sstext(3)
    elif vamos_en == "coliseo":
        correcta = Respuestas_arco.sstext(4)
    elif vamos_en == "teatro":
        correcta = Respuestas_arco.sstext(5)

    return correcta


def arco(ventana, clock, score, correcta, base):
    if base == "bonito":
        fondo = pygame.image.load('img/Mapabonito.png')  # fondo
    else:
        fondo = pygame.image.load('img/Mapafeo.png')  # fondo

    global codsx, codsy, mi_resp_es, algo, point, contin

    contin = True

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
    puesto = None
    retro = False
    unico = True

    ay = 600
    ax = 1050
    click = False

    respuest = None

    if correcta == Respuestas_arco.sstext(0):
        puesto = "primero"
        respuest = Funciones_Globales.lista_arco()

    elif correcta == Respuestas_arco.sstext(1):
        puesto = "de segundas"
        respuest = Funciones_Globales.lista_acueducto()

    elif correcta == Respuestas_arco.sstext(2):
        puesto = "de terceras"
        respuest = Funciones_Globales.lista_templo()

    elif correcta == Respuestas_arco.sstext(3):
        puesto = "de cuartas"
        respuest = Funciones_Globales.lista_termas()

    elif correcta == Respuestas_arco.sstext(4):
        puesto = "de quintas"
        respuest = Funciones_Globales.lista_coliseo()

    elif correcta == Respuestas_arco.sstext(5):
        puesto = "de sextas"
        respuest = Funciones_Globales.lista_teatro()
    if score >= 100:
        score -= 50
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
        elif algo > 3:
            algo = 3
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

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))
        acept = ventana.blit(letre, (-100, -100))

        ventana.blit(fondo, (0, 0))

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, BLACK)

        if algo == 3 and espacio:
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
        Funciones_Globales.dialog(Master_Arco.texto(algo, puesto), Master_Arco.stext(algo), Master_Arco.sstext(algo))

        if algo == 3:
            Funciones_Globales.acept()

        Funciones_Globales.barra_progreso(score)

        if estoy_en == 1 and espacio:
            Funciones_Globales.papoir("1", "Open", (0, 0), Respuestas_arco.texto(respuest[0]), Respuestas_arco.stext(
                respuest[0]),
                                      Respuestas_arco.sstext(respuest[0]),
                                      Respuestas_arco.ssstext(respuest[0]),
                                      Respuestas_arco.sssstext(respuest[0]),
                                      Respuestas_arco.ssssstext(respuest[0]))
            mi_resp_es = Respuestas_arco.sstext(respuest[0])
        elif estoy_en == 2 and espacio:
            Funciones_Globales.papoir("2", "Open", (0, 0), Respuestas_arco.texto(respuest[1]), Respuestas_arco.stext(
                respuest[1]),
                                      Respuestas_arco.sstext(respuest[1]),
                                      Respuestas_arco.ssstext(respuest[1]),
                                      Respuestas_arco.sssstext(respuest[1]),
                                      Respuestas_arco.ssssstext(respuest[1]))
            mi_resp_es = Respuestas_arco.sstext(respuest[1])
        elif estoy_en == 3 and espacio:
            Funciones_Globales.papoir("3", "Open", (0, 0), Respuestas_arco.texto(respuest[2]), Respuestas_arco.stext(
                respuest[2]),
                                      Respuestas_arco.sstext(respuest[2]),
                                      Respuestas_arco.ssstext(respuest[2]),
                                      Respuestas_arco.sssstext(respuest[2]),
                                      Respuestas_arco.ssssstext(respuest[2]))
            mi_resp_es = Respuestas_arco.sstext(respuest[2])
        elif estoy_en == 4 and espacio:
            Funciones_Globales.papoir("4", "Open", (0, 0), Respuestas_arco.texto(respuest[3]), Respuestas_arco.stext(
                respuest[3]),
                                      Respuestas_arco.sstext(respuest[3]),
                                      Respuestas_arco.ssstext(respuest[3]),
                                      Respuestas_arco.sssstext(respuest[3]),
                                      Respuestas_arco.ssssstext(respuest[3]))
            mi_resp_es = Respuestas_arco.sstext(respuest[3])

        if espacio and retu and unico:
            retro = True
            unico = False
            if mi_resp_es == correcta:
                score += 6

            elif mi_resp_es == Respuestas_arco.sstext(8) or mi_resp_es == Respuestas_arco.sstext(
                    7) or mi_resp_es == Respuestas_arco.sstext(6):
                contin = False

            elif mi_resp_es != correcta:
                score -= 10

        if retro:
            election = False
            estoy_en = None
            if mi_resp_es == correcta:
                Funciones_Globales.dialog("Hemos empezado la construcción", "muy pronto veremos como quedaran", "")
                pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                acept = ventana.blit(letre, (ax, ay))
                Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

            elif mi_resp_es == Respuestas_arco.sstext(8) or mi_resp_es == Respuestas_arco.sstext(
                    7) or mi_resp_es == Respuestas_arco.sstext(6):

                Funciones_Globales.dialog("¡No!", "Ordenaste construir algo que no te habian aconsejado los ingenieros",
                                          "El Emperador se ha enfurecido contigo")
                pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                acept = ventana.blit(letre, (ax, ay))
                Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

            elif mi_resp_es != correcta:
                if puesto == "primero":
                    Funciones_Globales.dialog("Sin los arcos y la piedra angular no se desarrolla la arquitectura", "",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif puesto == "de segundas":
                    Funciones_Globales.dialog("Los ciudadanos de Utopía reqieren de agua antes que cualquier cosa", "",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif puesto == "de terceras":
                    Funciones_Globales.dialog("El descontento se extiende, los ciudadanos quieren un Templo", "", "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif puesto == "de cuartas":
                    Funciones_Globales.dialog("Una ciudad sin Termas es una ciudad para cerdos...",
                                              "eso cualquier Romano lo sabe", "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif puesto == "de quintas":
                    Funciones_Globales.dialog("¿Acaso esperas que los espectaculos se hagan en la calle?", "", "")
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

        point = score

        pygame.display.update()
        clock.tick(10)


def points():
    return point


def continuar():
    return contin
