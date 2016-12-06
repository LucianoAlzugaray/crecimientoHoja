import numpy as np
import pyqtgraph as pg
import math
from time import sleep

class Graficador:
	def __init__(self, ventana):
		self.ventana = ventana

		self.view = ventana.addViewBox()
		self.view.setAspectLocked()

		self.graph = pg.GraphItem()
		self.view.addItem(self.graph)

	def graficar(self, palabra, anguloDeGiro):
		angulo = math.radians(90)
		nodos = []
		nodos_borde = []
		lineas = []
		nodo_actual = [0,0]
		pila_ramas = []
		posicion = 0
		posicion_actual = 0
		posicion_nuevo = 1
		posicion_inicial_borde = 0
		posicion_final_borde = 0
		inicioRama = [0,0]
		anguloDeGiro = math.radians(anguloDeGiro)
		anguloDeRama = 0

		nodos.append([nodo_actual[0], nodo_actual[1]])
		
		for caracter in palabra:
			if caracter == '-':
				angulo = angulo + anguloDeGiro
			elif caracter == '+':
				angulo = angulo - anguloDeGiro
			elif caracter == '[':
				inicioRama[0] = nodo_actual[0]
				inicioRama[1] = nodo_actual[1]
				anguloPrincipal = angulo
				pila_ramas.append([[inicioRama[0], inicioRama[1]],anguloPrincipal, posicion_actual])
			elif caracter == '{':
				posicion_inicial_borde = posicion_actual
				posicion_final_borde = posicion_actual
			elif caracter == ']':
				elemento = pila_ramas.pop()
				nodo_actual[0] = elemento[0][0]
				nodo_actual[1] = elemento[0][1]
				angulo = elemento[1]
				posicion_actual = elemento[2]
			elif caracter == '}':
				primer_nodo = posicion_inicial_borde
				for nodo in nodos_borde:
					lineas.append([primer_nodo, nodo])
					primer_nodo = nodo
				lineas.append([posicion_final_borde, posicion_inicial_borde])
			elif caracter == '.':
				if nodo_actual[1] == 15:
					print "posicion_actual: ",
					print posicion_actual
				nodos_borde.append(posicion_actual)
				posicion_final_borde = posicion_actual			
			elif caracter == 'G':
				nodo_actual[0] = nodo_actual[0] + math.cos(angulo) * 5
				nodo_actual[1] = nodo_actual[1] + math.sin(angulo) * 5				
				nodos.append([nodo_actual[0], nodo_actual[1]])
				lineas.append([posicion_actual, posicion_nuevo])
				posicion = posicion + 1
				posicion_actual = posicion
				posicion_nuevo = posicion_nuevo + 1
		## Update the graph		
		pos = np.array(nodos)
		adj = np.array(lineas)	
		print "lineas: ",
		print lineas
		print "nodos:",
		print nodos
		
		if lineas:
			self.graph.setData(pos=pos, adj=adj, size=0.1, pxMode=False)