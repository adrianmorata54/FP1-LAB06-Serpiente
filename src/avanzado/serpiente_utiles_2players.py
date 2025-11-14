import random

def comprueba_choque(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], otra_serpiente: list[tuple[int, int]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma, con las paredes o con la otra serpiente. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de cada segmento de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    otra_serpiente: Lista de tuplas representando las posiciones (columna, fila) de la otra serpiente.

    Devuelve:
    True si la serpiente se ha chocado consigo misma, con las paredes o con la otra serpiente, False en caso contrario.
    '''    
    # TODO: Copia tu solución anterior y añádele la comprobación de choque con la otra serpiente
    choque = False
    cabeza = serpiente[0]
    for pared in paredes:
        if cabeza in pared:
            choque = True
   
    if cabeza in serpiente[1:]:
        choque = True
    elif cabeza in otra_serpiente:
        choque = True
    return choque
    

def ha_comido_serpiente(serpiente: list[tuple[int, int]], posicion_comida: tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    posicion_comida: Tupla representando la posición de la comida (columna, fila).

    Devuelve:
    True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.
    '''
    # TODO: Copia tu solución anterior
    if posicion_comida in serpiente:
            return True
    else:
            return False

def crece_serpiente(serpiente: list[tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    '''
    # TODO: Copia tu solución anterior
    serpiente.append(serpiente[-1])

def genera_comida_aleatoria(serpiente_jugador: list[tuple[int, int]], serpiente_ia: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], filas: int, columnas: int) -> tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que las serpientes o las paredes.

    Parámetros:
    serpiente_jugador: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    serpiente_ia: Lista de tuplas representando las posiciones (columna, fila) de la otra serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.

    Devuelve:
    Posición aleatoria para la comida (columna, fila).
    '''
    # TODO: Copia tu solución anterior y añádele la comprobación de que la comida no se genere sobre la serpiente_ia
    comida = (random.randint(0, columnas-1), random.randint(0, filas-1))
    todas_paredes = []
    for columna in paredes:
        for posicion in columna:
            todas_paredes.append(posicion)
    while comida in todas_paredes or comida in serpiente_jugador or comida in serpiente_ia:
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
    # TODO: Copia tu solución anterior
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

def decide_movimiento_ia(serpiente_rival: list[tuple[int, int]], serpiente_jugador: list[tuple[int, int]],
    paredes: list[list[tuple[int, int]]], posicion_comida: tuple[int, int],
    filas: int, columnas: int) -> str:
    '''
    Decide la dirección de movimiento de la serpiente rival, intentando elegir la que más 
    le acerque a la comida sin chocar.

    Parámetros:
    serpiente_rival: lista de posiciones (columna, fila) de la serpiente rival.
    serpiente_jugador: lista de posiciones de la serpiente del jugador.
    paredes: lista de listas de posiciones de las paredes.
    posicion_comida: posición actual de la comida.
    filas, columnas: tamaño del tablero.

    Devuelve:
    Dirección elegida: 'Left', 'Right', 'Up' o 'Down'.    
    '''
    # Construiremos una lista de (distancia_a_la_comida, direccion)
    opciones = []
    for d in ("Up", "Down", "Left", "Right"):
        # TODO: Haz una copia de la serpiente rival y muévela en la dirección d
        serpiente_copia = serpiente_rival.copy()
        mueve_serpiente(serpiente_copia, d, filas, columnas)

        # TODO: Si la copia no se ha chocado
        if not comprueba_choque(serpiente_copia, paredes, serpiente_jugador):    
            # TODO: Calcula la distancia de la cabeza a la comida
            # Usa la distancia Manhattan: valor absoluto de la diferencia en x + valor absoluto de la diferencia de y
            comida = genera_comida_aleatoria(serpiente_jugador, serpiente_copia, paredes, filas, columnas)
            x1, y1 = serpiente_copia[0]
            x2, y2 = posicion_comida
            distancia = (abs(x2-x1), abs(y2-y1))
            # TODO: Añade a la lista opciones una tuplºa con la distancia y la dirección
            opcion = [distancia, d]
            opciones.append(opcion)
    # TODO: Si no hay opciones válidas, devolvemos "Up" por defecto
    if opciones == []:
         return 'Up'
    # TODO: Devolvemos la dirección que minimiza la distancia a la comida
    distancia_minima = None
    for opcion in opciones:
        if distancia_minima == None:
            distancia_minima = opcion
        elif opcion[0] < distancia_minima[0]:
            distancia_minima = opcion
    mejor_opcion = distancia_minima.pop()
    return mejor_opcion 
             

