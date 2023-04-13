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
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		print ("La distancia más corta entre dos puntos es: " + str(closest_pair_Dac(points)))
	elif opcionMenu=="2":
		print ("")
		print ("La distancia más corta entre dos puntos es: " + str(closest_pair_din(points)))
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")