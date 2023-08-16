import pygame
import Funciones_Globales
import Master_Desiciones
import Respuestas_Desiciones

letre = pygame.image.load('img/letrero.png')
dark = pygame.image.load('img/papironegro.png')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

point = None
sub = None


def hay_que_desidir(vamos_en):
    global sub
    if vamos_en == "billingue":
        sub = 0
    elif vamos_en == "casamiento":
        sub = 1
    elif vamos_en == "financiar":
        sub = 2
    elif vamos_en == "hijos":
        sub = 3

    return sub


def desicion(ventana, clock, score, subs, base):
    if base == "bonito":
        fondo = pygame.image.load('img/Mapabonito.png')  # fondo
    else:
        fondo = pygame.image.load('img/Mapafeo.png')  # fondo

    global point

    cordpap1 = (200, 300)
    cordpap2 = (900, 300)

    ay = 600
    ax = 1050

    espacio = False
    n_uno = False
    n_dos = False
    retro = False

    mi_resp_es = None
    algo = 0

    estoy_en = None
    election = False
    retu = False
    done = False
    click = False
    unico = True

    codsx = 0
    codsy = - 100
    if sub == 3:
        pass
    else:
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
                if event.key == pygame.K_SPACE:
                    espacio = True
                elif event.key == pygame.K_1:
                    n_uno = True
                elif event.key == pygame.K_2:
                    n_dos = True
                if event.key == pygame.K_RETURN:
                    retu = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    espacio = False
                elif event.key == pygame.K_1:
                    n_uno = False
                elif event.key == pygame.K_2:
                    n_dos = False
                if event.key == pygame.K_RETURN:
                    retu = False

        if n_uno:
            codsx = cordpap1[0]
            codsy = cordpap1[1]
            estoy_en = 1
        elif n_dos:
            codsx = cordpap2[0]
            codsy = cordpap2[1]
            estoy_en = 2

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))
        acept = ventana.blit(letre, (-100, -100))

        ventana.blit(fondo, (0, 0))

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 1100, 40, BLACK)

        if election:
            algo = None

            destell = pygame.image.load('img/destello.png')
            destell.set_alpha(0)
            prev = ventana.blit(destell, (codsx, codsy))

            Funciones_Globales.papoir("", "Open", (0, 0), Respuestas_Desiciones.texto(subs),
                                      Respuestas_Desiciones.stext(
                                          subs),
                                      Respuestas_Desiciones.sstext(subs),
                                      Respuestas_Desiciones.ssstext(subs),
                                      Respuestas_Desiciones.sssstext(subs),
                                      Respuestas_Desiciones.ssssstext(subs))
            # election classic

            uno = pygame.draw.rect(ventana, BLACK, (200, 300, 200, 65))
            ventana.blit(letre, cordpap1)
            Funciones_Globales.dess("Si", cordpap1)

            dos = pygame.draw.rect(ventana, BLACK, (900, 300, 200, 65))
            ventana.blit(letre, cordpap2)
            Funciones_Globales.dess("No", cordpap2)

            if prev.colliderect(uno):
                cordpap1 = (190, 290)

            else:
                cordpap1 = (200, 300)

            if prev.colliderect(dos):
                cordpap2 = (890, 290)

            else:
                cordpap2 = (900, 300)

        # dialogo master

        if algo == 0:
            Funciones_Globales.acept()
            Funciones_Globales.dialog(Master_Desiciones.texto(algo), Master_Desiciones.stext(algo),
                                      Master_Desiciones.sstext(algo))

            Funciones_Globales.acept()

        Funciones_Globales.barra_progreso(score)

        if algo == 0 and espacio:
            election = True

        if estoy_en == 1:
            mi_resp_es = "si"

        elif estoy_en == 2:
            mi_resp_es = "no"

        if retu and unico:
            retro = True
            unico = False
            if mi_resp_es == "si":
                score += 7

            elif mi_resp_es == "no":
                score -= 50

        if retro:
            election = False
            estoy_en = None
            if mi_resp_es == "si":
                if subs == 0:
                    Funciones_Globales.dialog("Ahora es mas facil comunicarte con tus adversarios", "",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 1:
                    Funciones_Globales.dialog("Ahora la tribu a la que pertenece tu esposa",
                                              "esta dispuesta a ser Romanizada",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 2:
                    Funciones_Globales.dialog("Has perdido el poco dinero que conseguiste tras tu libertad",
                                              "",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 3:
                    Funciones_Globales.dialog("Tus hijos acaban de partir al campo de batalla",
                                              "deseales suerte",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)

            elif mi_resp_es == "no":
                if subs == 0:
                    Funciones_Globales.dialog("La guerra es cada dia mas intensa",
                                              "y no hay forma de entender al enemigo",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 1:
                    Funciones_Globales.dialog("Al rechazar la propuesta de matrimonio la tribu se ha ofendido",
                                              "ahora son mas agresivos",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 2:
                    Funciones_Globales.dialog("Los impuestos son una obligacion del Romano",
                                              "has perdido una enorme cantidad de respeto y apoyo",
                                              "")
                    pygame.draw.rect(ventana, BLACK, (1050, 600, 200, 64))

                    acept = ventana.blit(letre, (ax, ay))
                    Funciones_Globales.draw_text(ventana, "Continuar", 40, ax + 30, ay + 20, WHITE)
                elif sub == 3:
                    Funciones_Globales.dialog(
                        "El servicio militar es obligatorio, el pueblo te ve como un cobarde y una deshonra",
                        "tus hijos son obligados a ir, ahora en peores condiciones",
                        "")
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
