import pygame
import text
import Funciones_Globales
import list_tuto

BLACK = (0, 0, 0)


def tutor(ventana, clock):
    fon = pygame.image.load('img/mapanuevo.png')

    election = False
    hablan = True
    derecha = False
    izquierda = False
    espacio = False
    NOuno = False
    NOdos = False
    NOtres = False
    NOcuatro = False
    estoy_en = None
    retu = False
    rands = [0, 1, 2, 3]
    cordpap1 = (250, 100)
    cordpap2 = (750, 100)
    cordpap3 = (250, 300)
    cordpap4 = (750, 300)
    codsx = 0
    codsy = -300
    score = 50
    algo = 0
    ####
    done = False

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
                    NOuno = True
                elif event.key == pygame.K_2:
                    NOdos = True
                elif event.key == pygame.K_3:
                    NOtres = True
                elif event.key == pygame.K_4:
                    NOcuatro = True
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
                    NOuno = False
                elif event.key == pygame.K_2:
                    NOdos = False
                elif event.key == pygame.K_3:
                    NOtres = False
                elif event.key == pygame.K_4:
                    NOcuatro = False
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
        if NOuno and election:
            codsx = cordpap1[0]
            codsy = cordpap1[1]
            estoy_en = 1
        elif NOdos and election:
            codsx = cordpap2[0]
            codsy = cordpap2[1]
            estoy_en = 2
        elif NOtres and election:
            codsx = cordpap3[0]
            codsy = cordpap3[1]
            estoy_en = 3
        elif NOcuatro and election:
            codsx = cordpap4[0]
            codsy = cordpap4[1]
            estoy_en = 4

        if algo == 3 and espacio:
            hablan = False
            election = True
            algo = 0

        ventana.blit(fon, (0, 0))

        # #---- zona de dibujo ---##

        Funciones_Globales.draw_text(ventana, "Puntaje: {}".format(score), 50, 900, 40, BLACK)

        if hablan:
            Funciones_Globales.dialog(text.texto(algo), text.stext(algo), text.sstext(algo))
        if algo == 3 and hablan:
            Funciones_Globales.acept()
        if election:
            destell = pygame.image.load('img/destello.png')
            ventana.blit(destell, (codsx, codsy))
            Funciones_Globales.papoir("1", "Close", cordpap1, "", "", "", "", "", "")
            Funciones_Globales.papoir("2", "Close", cordpap2, "", "", "", "", "", "")
            Funciones_Globales.papoir("3", "Close", cordpap3, "", "", "", "", "", "")
            Funciones_Globales.papoir("4", "Close", cordpap4, "", "", "", "", "", "")

        if estoy_en == 1 and espacio:
            Funciones_Globales.papoir("1", "Open", (0, 0), list_tuto.texto(rands[0]), list_tuto.stext(rands[0]),
                                      list_tuto.sstext(rands[0]),
                                      list_tuto.ssstext(rands[0]),
                                      list_tuto.sssstext(rands[0]), list_tuto.ssssstext(rands[0]))
        elif estoy_en == 2 and espacio:
            Funciones_Globales.papoir("2", "Open", (0, 0), list_tuto.texto(rands[1]), list_tuto.stext(rands[1]),
                                      list_tuto.sstext(rands[1]),
                                      list_tuto.ssstext(rands[1]),
                                      list_tuto.sssstext(rands[1]), list_tuto.ssssstext(rands[1]))
        elif estoy_en == 3 and espacio:
            Funciones_Globales.papoir("3", "Open", (0, 0), list_tuto.texto(rands[2]), list_tuto.stext(rands[2]),
                                      list_tuto.sstext(rands[2]),
                                      list_tuto.ssstext(rands[2]),
                                      list_tuto.sssstext(rands[2]), list_tuto.ssssstext(rands[2]))
        elif estoy_en == 4 and espacio:
            Funciones_Globales.papoir("4", "Open", (0, 0), list_tuto.texto(rands[3]), list_tuto.stext(rands[3]),
                                      list_tuto.sstext(rands[3]),
                                      list_tuto.ssstext(rands[3]),
                                      list_tuto.sssstext(rands[3]), list_tuto.ssssstext(rands[3]))

        if espacio and retu:
            done = True

        pygame.display.update()
        clock.tick(10)
    return
