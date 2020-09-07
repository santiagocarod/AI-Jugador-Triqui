def imprimirMatriz(juego):
	print("  A B C")
	for i in range(3):
		print(i+1, end = ' ')
		for j in range(3):
			if juego[i][j] !='N':
				print(f'{juego[i][j]}', end = ' ')
			else:
				print('*', end = ' ')
		print('')

def getColumna(matrix, i):
    return [row[i] for row in matrix]

def getDiagonales(juego):
	return[[ row[i] for i,row in enumerate(juego)],[ row[-i-1] for i,row in enumerate(juego)]]

def filtro(juego,jugada):
    for i in range(3):
        for j in range(3):
            if(juego[i][j] =='N' and jugada[i][j] =='O'):
                jugada[i][j] ='N'
    return jugada

def jugar(juego,jugada):
	if (validarJugada(jugada)):
		columna = ord(jugada[0])-65
		fila = int(jugada[1])-1
		if (juego[fila][columna] =='N'):
			juego[fila][columna] = 'O'
			return juego

def validarJugada(jugada):
	letrasValidas = ['A','B','C']
	numerosValidos = ['1','2','3']
	if (len(jugada) == 2):
		letra = jugada[0]
		numero = jugada[1]
		if(letra in letrasValidas):
			if(numero in numerosValidos):
				return True
	return False

def disponibles(juego):
	cuenta = 0
	for a in juego:
		cuenta += a.count('N')
	return cuenta

def turnoJugador(juego):
	print("En que casilla quieres jugar? (EJ: A1)")
	jugada = input()
	juego = jugar(juego,jugada)
	return juego