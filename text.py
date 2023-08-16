

def texto(sub):
    uno = "Este es un cuadro de dialogo, en este punto se presentará la información"

    dos = "Aquí se planteará un conflicto, se dan 4 posibles  soluciones."

    tres = "Use los  números 1, 2, 3, 4 para seleccionar la opción que considere acertada."

    cuatro = "Use espacio para abrirla, precione Enter al mismo tiempo para seleccionar"

    guion = [uno, dos, tres, cuatro]

    salida = guion[sub]
    return salida


def stext(sub):
    suno = "relevante al usuario, interactúe mediante Flecha_Derecha para avanzar"
    sdos = ""
    stres = ""
    scuatro = "o cerrar."

    guion = [suno, sdos, stres, scuatro]
    salida = guion[sub]
    return salida


def sstext(sub):
    ssuno = "y con Flecha_Izquierda para retroceder."
    ssdos = ""
    sstres = ""
    sscuatro = ""

    guion = [ssuno, ssdos, sstres, sscuatro]
    salida = guion[sub]
    return salida
