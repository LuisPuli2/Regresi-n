from urllib.request import urlopen

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import pylab as pl
import sys

"""Calcula el indice de masa corporal apartir de las lineas dadas de la url"""
def imc (linea): 
	peso = float(linea[22]) 
	talla = float(linea[23])/100
	imc =  peso/(talla*talla)
	return imc

"""La función regresión, recibe un arreglo de valoresX (la edad), y valoresY (el imc) mediante las fórmulas dadas
   calcula la pendiente, intersección y correlación para hacer la aproximación. Regresa la pendiente y la interseccion
   para graficar la línea."""
def regresion(valoresX,valoresY):
	N = len(valoresY)
	sumaX = sumaY = sumaXY = sumXSquared = sumYSquared = 0
	for i in range(0,len(valoresX)):
		sumaXY = sumaXY + (valoresX[i]* valoresY[i])
		sumaX = sumaX + valoresX[i]
		sumaY = sumaY + valoresY[i]
		sumXSquared = sumXSquared + valoresX[i]**(2)
		sumYSquared = sumYSquared + valoresY[i]**(2)

	pendiente = ((N * sumaXY) - (sumaX * sumaY)) / ((N* sumXSquared) - (sumaX)**2)
	interseccion = (sumaY - (pendiente * sumaX)) / N
	corr = ((N*sumaXY) - (sumaX * sumaY))/(((N * sumXSquared - (sumaX)**(2)) * (N * sumYSquared - (sumaY)**2 ))**(.5))
	print ("La correlacion es " + str(corr))
	x = np.arange(15, 70, 0.1)
	y = x*pendiente + interseccion  
	width = 1
	return (interseccion,pendiente)

""" La función GraficaRegresion recibe cuatro atributos, los datos de hombres y los datos de mujeres respectivamente.
    manda a llamar a la función regresión para cada género y los grafica """
def GraficaRegresion (edadH,imcH,edadM,imcM):
	print ("Los datos generados de calcular la regresion lineal para hombres: ")
	(interseccionH,pendienteH) = regresion(edadH,imcH) # Se calculan los datos para hombres
	print ("Los datos generados de calcular la regresion lineal para mujeres: ")
	(interseccionM,pendienteM) = regresion(edadM,imcM) # Se calculan los datos para mujeres
	x = np.arange(15, 70, 0.1)
	y1 = x*pendienteH + interseccionH # Recta para hombres
	y2 = x*pendienteM + interseccionM # Recta para mujeres
	f, (ax2,ax1) = plt.subplots( 1,2,sharey=True)
	""" Caracteristicas y especificaciones de las graficas"""
	ax1.scatter(edadM, imcM)
	ax1.plot(x, y2,color="red")
	ax1.set_title('IMC Mujeres')
	ax2.scatter(edadH, imcH)
	ax2.plot(x, y1,color="red")
	ax2.set_title('IMC Hombres')
	ax1.set_ylabel('Imc')
	ax1.set_xlabel('Edad')
	ax2.set_ylabel('Imc')
	ax2.set_xlabel('Edad')

"""Función que utiliza la biblioteca urlib, para tomar los datos de las personas."""
def llenaValores():
	indicemc={} #Almacena indice de mas corporal
	edadH = {} #Almacena los valores
	contH = {} #Diccionario para hacer la division 
	edadM = {}
	contM = {}
	contador = {}
	imcH = []
	imcM = []
	edadHombre = []
	edadMujer = []
	for line in urlopen('http://ww2.amstat.org/publications/jse/datasets/body.dat.txt'):
		line = line.decode("utf-8") 
		listaValores = line.split()
		llave = int(float(listaValores[21])) #La llave del diccionario
		""" Se llenan los datos de los hombres """
		if listaValores[24] == '1': 
			imcH.append(imc(listaValores)) 
			edadHombre.append(float(listaValores[21]))
			"""Si tiene llave, se le agrega el valor, si no se crea el valor."""
			if llave in edadH:
				edadH[llave] = edadH[llave] + int(float(listaValores[22]))
				contH[llave] = contH[llave] + 1
			else:
				edadH[llave] = int(float(listaValores[22]))
				contH[llave] = 1
		"""Se llenan datos de las mujeres"""
		if listaValores[24] == '0':
			imcM.append(imc(listaValores)) 
			edadMujer.append(float(listaValores[21]))
			"""Si tiene llave, se le agrega el valor, si no se crea el valor."""
			if llave in edadM:
				edadM[llave] = edadM[llave] + int(float(listaValores[22]))
				contM[llave] = contM[llave] + 1
			else:
				edadM[llave] = int(float(listaValores[22]))
				contM[llave] = 1
	PesoHombre = []
	EdadHombre = []
	PesoMujer = []
	EdadMujer = []
	indice = []
	edad = []
	""" En los tres 'for' se les saca el promedio por edad, y se agregan a sus listas"""
	for llave in edadH:
		EdadHombre.append(llave)
		PesoHombre.append(edadH[llave]/contH[llave])
	for llave in edadM:
		EdadMujer.append(llave)
		PesoMujer.append(edadM[llave]/contM[llave])
	for llave in indicemc:
		indice.append(indicemc[llave]/contador[llave])
		edad.append(llave)
	width = 1
	""" Se manda a llamar la función GraficaRegresion para grŕaficar la regresión (valga la redundancia)"""
	GraficaRegresion(edadHombre,imcH,edadMujer,imcM) 
	f, (ax1,ax2) = plt.subplots(1, 2,sharey=True)
	"""Caracteristicas de las gráficas, estas solo graficarán los pesos y edades"""
	ax1.bar(EdadHombre, PesoHombre, width, color="blue")
	ax1.set_title('Hombres')
	ax2.bar(EdadMujer, PesoMujer, width, color="red")
	ax2.set_title('Mujeres')
	ax1.set_ylabel('Peso')
	ax1.set_xlabel('Edad')
	ax2.set_ylabel('Peso')
	ax2.set_xlabel('Edad')
	plt.show()

if __name__ == '__main__':
	llenaValores()