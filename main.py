# Reto 4 - Isla del Tesoro
print('¡Bienvenido a la Isla!\nTu misión será encontrar el tesoro.\n')

while True:
    mision_principal = int(input('Ingresa 1 para aceptar la misión o 0 para rechazar la misión '))

    if mision_principal == 1:
        print('Bajar del barco')

        ingreso_isla = int(input('Ingresa 1 para ir al interior de la isla o 0 para rodear la isla '))

        if ingreso_isla == 1:
            print('Caminar hasta el centro de la isla\nDetenerse frente a un sendero lleno de maleza')

            cruzar = int(input('Ingresa 1 para cruzar corriendo o 0 para cruzar caminando '))

            if cruzar == 1:
                print('Correr hasta encontrar una catacumba')

                ingreso_catacumba = int(input('Ingresa 1 para nadar al interior de la catacumba o 0 para esperar '))

                if ingreso_catacumba == 1:
                    print('Nadar hasta el fondo de la catacumba\nAcercarse al portal para ingresar a la catacumba')

                    mision_busqueda = int(input('Ingresa 1 para aceptar misión de busqueda del Mercader Mammon o 0 para recharzar la misión '))

                    if mision_busqueda == 1:
                        print('Caminar por la catacumba')

                        sala = int(input('Ingresa 1 para elegir la sala de la izquierda, 2 para la sala del centro o 0 para la sala de la derecha '))

                        if sala == 1:
                            print('Encontraste al Mercader Mammon\nReclamar el tesoro\nGanaste el Juego')
                            break

                        elif sala == 2:
                            print('Atacado por grupo de Lilim Salayer\nFin del Juego')

                        elif sala == 0:
                            print('Atacado por Raid Boss Anakazel\nFin del Juego')

                    elif mision_busqueda == 0:
                        print('Expulsado de la catacumba\nFin del Juego')

                elif ingreso_catacumba == 0:
                    print('Atacado por una tribu de Orcos\nFin del Juego')

            elif cruzar == 0:
                print('Caíste en el agujero\nFin del Juego')

        elif ingreso_isla == 0:
            print('Raptado por una Harpía\nFin del Juego')

    elif mision_principal == 0:
        print('Atacado por un Gremlin\nFin del Juego')
        
    else:
        print('Elije una opción válida.')
