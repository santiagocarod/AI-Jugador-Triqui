import numpy as np
from util import getColumna,getDiagonales

def heuristica(juego):
	resultado = 0
	resultado += buscarGanar(juego,'X')
	resultado -= buscarGanar(juego,'O')
	if (resultado == 0):
		resultado += buscarCasiTriqui(juego,'X')
		resultado -= buscarCasiTriqui(juego,'O')
		if (resultado == 0):
			resultado += buscarLineaLibre(juego,'X')
			resultado -= buscarLineaLibre(juego,'O')
	return resultado


def buscarGanar(juego,jugador):
	
	for i in range(3):
		fila = np.array(juego[i])
		columna = np.array(getColumna(juego,i))

		if (len(np.unique(fila)) == 1 and fila[0]==jugador):
			return 1
		elif (len(np.unique(columna)) == 1 and columna[0]==jugador):
			return 1
	diagonales = getDiagonales(juego)
	diagonal= np.array(diagonales[0])
	diagonalRev= np.array(diagonales[1])
	
	if (len(np.unique(diagonal)) == 1 and diagonal[0]==jugador):
		return 1
	elif (len(np.unique(diagonalRev)) == 1 and diagonalRev[0]==jugador):
		return 1
	
	return 0

def buscarCasiTriqui(juego, jugador):
	acumulado = 0
	for i in range(3):
		fila = juego[i]
		columna = getColumna(juego,i)

		if (fila.count('N') == 1 and fila.count(jugador) == 2):
			acumulado += 0.5
		if(columna.count('N') == 1 and columna.count(jugador) == 2):
			acumulado += 0.5
	
	diagonales = getDiagonales(juego)
	diagonal= diagonales[0]
	diagonalRev= diagonales[1]

	if(diagonal.count('N') == 1 and diagonal.count(jugador) == 2):
		acumulado += 0.5
	if(diagonalRev.count('N') == 1 and diagonalRev.count(jugador) == 2):
		acumulado += 0.5

	return acumulado


def buscarLineaLibre(juego,jugador):
	acumulado = 0
	for i in range(3):
		fila = juego[i]
		columna = getColumna(juego,i)

		if (fila.count('N') == 2 and fila.count(jugador) == 1):
			acumulado += 1/3
		if(columna.count('N') == 2 and columna.count(jugador) == 1):
			acumulado += 1/3
	
	diagonales = getDiagonales(juego)
	diagonal= diagonales[0]
	diagonalRev= diagonales[1]

	if(diagonal.count('N') == 2 and diagonal.count(jugador) == 1):
		acumulado += 1/3
	if(diagonalRev.count('N') == 2 and diagonalRev.count(jugador) == 1):
		acumulado += 1/3

	return acumulado