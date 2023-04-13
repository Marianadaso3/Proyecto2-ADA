#Importaciones
import os
from dinamica import *
from Dac import *

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Utilizando algoritmo Dac")
	print ("\t2 - Utilizando algoritmo Dinamico")
	print ("\t3 - tercera opción")
	print ("\t4 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		print ("La distancia más corta entre dos puntos es (Dac): " + str(closest_pair_Dac(points)))
	elif opcionMenu=="2":
		print ("")
		print ("La distancia más corta entre dos puntos es (DINAMICA): " + str(closest_pair_din(puntos)))
	elif opcionMenu=="4":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")