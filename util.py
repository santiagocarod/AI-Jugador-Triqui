def imprimirMatriz(juego):
	for i in range(3):
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