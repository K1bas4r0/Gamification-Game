import pygame
# import time
import Nivel_Tres
import animaciones
import Niveles
import Nivel_Dos
import Menus
# import threading
import Arquitectura
import Desisiones
import nivel_cuatro


"""def temporizador():
    i = 60
    while i > 0:
        print(i)
        i -= 1
        time.sleep(1)
    print("time off")"""


def main():
    done = False
    score = None
    bases = None

    pygame.init()
    pygame.mixer.init()

    ANCHO = 1300
    ALTO = 700
    clock = pygame.time.Clock()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # ventana

    pygame.display.set_caption('Legends Don\'t Crumble ')  # titulo
    pygame.display.set_icon(pygame.image.load('img/escudosin.png'))

    pygame.mixer.music.load('music/Passengers.mp3')
    pygame.mixer.music.set_volume(0.2)

    menu_ini = True
    cinematic_ini = False

    Nivel_uno = False
    arco = False

    Nivel_dos = False
    acueducto = False
    billingue = False
    templo = False

    Nivel_tres = False
    las_termas = False
    casamiento = False
    coliseo = False

    Nivel_cuatro = False
    teatro = False
    financiar = False
    hijos = False

    ganar = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()

        if menu_ini:
            Menus.inicial(ventana, clock)
            cinematic_ini = True

        # animaciones.movimientos_germanos(ventana, clock)
        # animaciones.filosofo(ventana, clock)
        # animaciones.win(ventana, clock)
        # animaciones.unlock_all_croma(ventana, clock, "bonito")
        # animaciones.lose(ventana, clock, 50, "bonito")
        # animaciones.estado_final(ventana, clock, 50, "bonito")

        if cinematic_ini:
            animaciones.inicial(ventana, clock)
            cinematic_ini = False
            Nivel_uno = True

        if Nivel_uno:
            animaciones.movimientos_hunos(ventana, clock)
            pygame.mixer.music.play(-1)
            Niveles.nivel_uno(ventana, clock)
            Niveles.segunda_tirada(ventana, clock)
            score = Niveles.points()
            cont = Niveles.conti()

            if cont:
                if score > 0:
                    arco = True
                    animaciones.croma_init(ventana, clock, score)
                else:
                    animaciones.lose(ventana, clock, score, bases)

            Nivel_uno = False
            bases = animaciones.base()

        if arco:
            correcta = Arquitectura.donde_vamos("arco")
            Arquitectura.arco(ventana, clock, 50, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()
            if cont:
                if score > 0:
                    Nivel_dos = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)

                arco = False
            else:
                animaciones.lose(ventana, clock, score, bases)

        if Nivel_dos:
            animaciones.movimientos_vandalos(ventana, clock)
            Nivel_Dos.nivel(ventana, clock, score)
            score = Nivel_Dos.points()

            if score > 0:
                acueducto = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            Nivel_dos = False
            # animaciones.croma_level2()

        if acueducto:
            correcta = Arquitectura.donde_vamos("acueducto")
            Arquitectura.arco(ventana, clock, score, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()

            if cont:

                if score > 0:
                    billingue = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            acueducto = False

        if billingue:
            sub = Desisiones.hay_que_desidir("billingue")
            Desisiones.desicion(ventana, clock, score, sub, bases)
            score = Desisiones.points()

            if score > 0:
                templo = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)
            billingue = False

        if templo:
            correcta = Arquitectura.donde_vamos("templo")
            Arquitectura.arco(ventana, clock, score, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()

            if cont:

                if score > 0:
                    Nivel_tres = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            templo = False

        if Nivel_tres:
            animaciones.movimientos_germanos(ventana, clock)
            Nivel_Tres.nivel(ventana, clock, score)
            score = Nivel_Tres.points()

            if score > 0:
                las_termas = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            Nivel_tres = False

        if las_termas:
            correcta = Arquitectura.donde_vamos("termas")
            Arquitectura.arco(ventana, clock, score, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()

            if cont:

                if score > 0:
                    casamiento = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            las_termas = False

        if casamiento:
            sub = Desisiones.hay_que_desidir("casamiento")
            Desisiones.desicion(ventana, clock, score, sub, bases)
            score = Desisiones.points()

            if score > 0:
                coliseo = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)
            casamiento = False

        if coliseo:
            correcta = Arquitectura.donde_vamos("coliseo")
            Arquitectura.arco(ventana, clock, score, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()

            if cont:

                if score > 0:
                    Nivel_cuatro = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            coliseo = False

        if Nivel_cuatro:
            animaciones.filosofo(ventana, clock)
            nivel_cuatro.hay_que_desidir("1")
            nivel_cuatro.desicion(ventana, clock, score)
            score = nivel_cuatro.points()

            if score > 0:

                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            nivel_cuatro.hay_que_desidir("2")
            nivel_cuatro.desicion(ventana, clock, score)
            score = nivel_cuatro.points()

            if score > 0:

                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            nivel_cuatro.hay_que_desidir("3")
            nivel_cuatro.desicion(ventana, clock, score)
            score = nivel_cuatro.points()

            if score > 0:

                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            nivel_cuatro.hay_que_desidir("4")
            nivel_cuatro.desicion(ventana, clock, score)
            score = nivel_cuatro.points()

            if score > 0:

                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            nivel_cuatro.hay_que_desidir("5")
            nivel_cuatro.desicion(ventana, clock, score)
            score = nivel_cuatro.points()

            if score > 0:
                teatro = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            Nivel_cuatro = False
            if score >= 100:
                animaciones.selec_croma(ventana, clock, bases)

        if teatro:
            correcta = Arquitectura.donde_vamos("teatro")
            Arquitectura.arco(ventana, clock, score, correcta, bases)
            score = Arquitectura.points()
            cont = Arquitectura.continuar()

            if cont:

                if score > 0:
                    financiar = True
                    if score >= 100:
                        animaciones.selec_croma(ventana, clock, bases)
                else:
                    animaciones.lose(ventana, clock, score, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)

            teatro = False

        if financiar:
            sub = Desisiones.hay_que_desidir("financiar")
            Desisiones.desicion(ventana, clock, score, sub, bases)
            score = Desisiones.points()

            if score > 0:
                hijos = True
                if score >= 100:
                    animaciones.selec_croma(ventana, clock, bases)
            else:
                animaciones.lose(ventana, clock, score, bases)
            financiar = False

        if hijos:
            sub = Desisiones.hay_que_desidir("hijos")
            Desisiones.desicion(ventana, clock, score, sub, bases)
            score = Desisiones.points()

            if score > 0:
                ganar = True
                if score >= 100:
                    animaciones.croma_level3(ventana, clock, bases, score)
            else:
                animaciones.lose(ventana, clock, score, bases)

        if ganar:
            animaciones.win(ventana, clock)
            animaciones.estado_final(ventana, clock, score, bases)
            animaciones.descargo(ventana, clock)


if __name__ == '__main__':
    # principal_hilo = threading.Thread(target=main, name="main")
    # hilo_daemon = threading.Thread(target=temporizador, name="temporizador", daemon=True)
    # principal_hilo.start()
    main()
