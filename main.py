from jugadorTriqui import mejorJugada
from heuristica import buscarGanar
from util import imprimirMatriz,turnoJugador,disponibles

triqui= [['N' for i in range(3)]for j in range(3)]

triqui2=[['X','O','O'],
        ['O','X','X'],
        ['X','N','O']]



ganador = False
while(not ganador):
	triqui = mejorJugada(triqui)
	if(buscarGanar(triqui,'X') == 1 or disponibles(triqui)==0):
		ganador = True
		break
	print("El tablero es:")
	imprimirMatriz(triqui)
	triquiAux = None
	while(triquiAux == None):
		triquiAux = turnoJugador(triqui)
		if (triquiAux == None):
			print("Jugada Invalida, por favor ingrese una casilla valida")
			imprimirMatriz(triqui)
	triqui = triquiAux
	imprimirMatriz(triqui)
	if(buscarGanar(triqui,'O') == 1):
		ganador = True
		break

print()
print()
print("JUEGO TERMINADO!!!")
print()
print()
print("TABLERO FINAL:")
imprimirMatriz(triqui)

if(buscarGanar(triqui,'X')==1):
	print("EL GANADOR ES 'X' !! ")
elif(buscarGanar(triqui,'O')==1):
	print("EL GANADOR ES 'O' !! ")
else:
	print("QUE BUENA PARTIDA! ES UN EMPATE!")