from jugadorTriqui import mejorJugada
from util import imprimirMatriz

triqui= [['N' for i in range(3)]for j in range(3)]

triqui2=[['X','O','O'],
        ['O','X','X'],
        ['X','N','O']]

triqui3=[['N','N','N'],
        ['N','N','N'],
        ['N','N','N']]




print("MEJOR JUGADA")
imprimirMatriz(mejorJugada(triqui2))
