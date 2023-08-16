def texto(sub,  vamos_en):
    uno = "Después de realizar 100 días de juegos en el coliseo y espectáculos de circo "

    dos = "Un ingeniero presento el acueducto."

    tres = "Otro presentó los Teatro y espectáculo circense "

    cuatro = "Escoge cual llevaras a Utopía {}. " .format(vamos_en)

    guion = [uno, dos, tres, cuatro]

    salida = guion[sub]
    return salida


def stext(sub):
    suno = "El emperador debe estampar su grandeza y te pide que reúnas los ingenieros "

    sdos = "Otro presentó los arcos, la piedra angular y puentes."

    stres = "Otro presentó los Templos"

    scuatro = " "

    guion = [suno, sdos, stres, scuatro]
    salida = guion[sub]

    return salida


def sstext(sub):
    ssuno = "y seleccionen las obras mas majestuosas y para demostrar lo valioso de roma."

    ssdos = "Otro presentó el Coliseo "

    sstres = "Finalmente, otro presentó las Termas "

    sscuatro = " "

    guion = [ssuno, ssdos, sstres, sscuatro]
    salida = guion[sub]

    return salida
