import random

def ha_comido_serpiente(serpiente: list[tuple[int, int]], posicion_comida: tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    posicion_comida: Tupla representando la posición de la comida (columna, fila).

    Devuelve:
    True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.
    '''
    # TODO: Ejercicio 1
    if posicion_comida in serpiente:
        return True
    else:
        return False

def comprueba_choque(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma o con las paredes. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de cada segmento de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.

    Devuelve:
    True si la serpiente se ha chocado consigo misma o con las paredes, False en caso contrario.
    '''
    # TODO: Ejercicio 2
    choque = False
    cabeza = serpiente[0]
    for pared in paredes:
        if cabeza in pared:
            choque = True
   
    if cabeza in serpiente[1:]:
        choque = True
    return choque

def crece_serpiente(serpiente: list[tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    '''
    # TODO: Ejercicio 3
    serpiente.append(serpiente[-1])

def genera_comida_aleatoria(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], filas: int, columnas: int) -> tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que la serpiente o las paredes.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.

    Devuelve:
    Posición aleatoria para la comida (columna, fila).
    '''
    # TODO: Ejercicio 4
    comida = (random.randint(0, columnas-1), random.randint(0, filas-1))
    todas_paredes = []
    for columna in paredes:
        for posicion in columna:
            todas_paredes.append(posicion)
    while comida in todas_paredes or comida in serpiente:
            comida = (random.randint(0, columnas-1), random.randint(0, filas-1))
    return comida

def mueve_serpiente(serpiente: list[tuple[int, int]], direccion: str, filas: int, columnas: int) -> None:
    '''
    Mueve la serpiente en el tablero según la dirección dada. El tablero es circular, lo que significa
    que si la serpiente se sale por la derecha, debe aparecer por la izquierda, y viceversa (y lo 
    mismo si se sale por arriba o por abajo).

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    direccion: Dirección en la que se debe mover la serpiente ('Left', 'Right', 'Down', 'Up').
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.
    '''
    # TODO: Ejercicio 5
    posicion_cabeza = serpiente[0]
    if direccion == 'Left':
        x, y = posicion_cabeza
        posicion_nueva = ((x-1) % columnas, y)
        serpiente.insert(0, posicion_nueva)
        serpiente.pop()
    if direccion == 'Right':
        x, y = posicion_cabeza
        posicion_nueva = ((x+1) % columnas, y)
        serpiente.insert(0, posicion_nueva)
        serpiente.pop()
    if direccion == 'Down':
        x, y = posicion_cabeza
        posicion_nueva = (x, (y+1) % filas)
        serpiente.insert(0, posicion_nueva)
        serpiente.pop()
    if direccion == 'Up':
        x, y = posicion_cabeza
        posicion_nueva = (x, (y-1) % filas)
        serpiente.insert(0, posicion_nueva)
        serpiente.pop()    
    return None