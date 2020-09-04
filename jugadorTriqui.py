from heuristica import heuristica
from util import imprimirMatriz,filtro
from copy import deepcopy
import random

def obtenerJuegosPosibles(juego,jugador):
    juegos = []
    for i in range(3):
        for j in range(3):
            if (juego[i][j]=='N'):
                juego[i][j]= jugador
                aux = deepcopy(juego)
                juegos.append(aux)
                juego[i][j]='N'
    return juegos

def obtenerHijoMinimo(juego):
    juegosPosibles = obtenerJuegosPosibles(juego,'O')
    valores = list(map(heuristica,juegosPosibles))
    resultado = [juegosPosibles[i] for (i,v) in enumerate(valores) if v == min(valores)]
    return random.choice(resultado)

def obtenerHijoMaximo(juego):
    juegosPosibles = obtenerJuegosPosibles(juego,'X')
    valores = list(map(heuristica,juegosPosibles))
    resultado = [juegosPosibles[i] for (i,v) in enumerate(valores) if v == max(valores)]
    return random.choice(resultado)	

def obtenerMaximo(juegos):
    valores = list(map(heuristica,juegos))
    resultado = [juegos[i] for (i,v) in enumerate(valores) if v == max(valores)]
    return random.choice(resultado)

def verificarDisponibilidad(juego):
    disponibles = 0
    for i in juego:
        disponibles += i.count('N')
    if (disponibles>1):
        return True
    else:
        for i in range(3):
            for j in range(3):
                if(juego[i][j]=='N'):
                    juego[i][j] = 'X'
        return False

def mejorJugada(juego):
    ##Si solo queda una posicion no indagar
    if(verificarDisponibilidad(juego)):
        juegosPosibles = obtenerJuegosPosibles(juego,'X')
        juegosMinimos = []

        for i in juegosPosibles:
            juegosMinimos.append(obtenerHijoMinimo(i))

        jugada = obtenerMaximo(juegosMinimos) 
        return filtro(juego,jugada)
    else:
        return juego