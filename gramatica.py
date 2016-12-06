import sys
import re

###########################################################################################e
class LindenmayerSystem:

	def __init__(self, start, alfabetoNoTerminales, produccionesIniciales = []):
		self.producciones = produccionesIniciales
		self.start = start
		self.producciones.append(start)
		self.noTerminales = alfabetoNoTerminales

	def agregarProduccion(self,noTerminal, producciones, probabilidades):
		p = Produccion(noTerminal,producciones, probabilidades)
		self.producciones.append(p)

	def mostrarGramatica(self):
		print "{"
		for i in self.producciones:
			i.mostrarProduccion()
		print "}"

##############################################################################################

class Produccion:
	def __init__(self, noTerminal, producciones):
		self.noTerminal = noTerminal
		self.producciones = producciones
	
	def mostrarProduccion(self):
		print self.noTerminal + " -> ",
		if len(self.producciones) > 1:

			lista = self.producciones[:len(self.producciones)-1]
			for i in lista:
				print i + " |",
		print self.producciones[len(self.producciones)-1]

##############################################################################################

class Derivador:

	def derivar(self,gramatica, palabra, PD, LA, RA, LB, RB): ##ARREGLAR DERIVAR
		nuevaPalabra = ""
		regexGramatica = re.compile("([SABG]\(.{1,5}\))")
		listaCaracteres = regexGramatica.split(palabra)
		for elemento in listaCaracteres:
			if elemento == 'S':
				for produccion in gramatica.producciones:
					if produccion.noTerminal == "S":
						nuevaPalabra = produccion.producciones
			
			elif re.match("A(.*)", elemento) != None :
				cadenaParametro = re.split("A\(|\)", elemento)
				parametro = eval(cadenaParametro[1])
				for produccion in gramatica.producciones:
					if produccion.noTerminal == "A(t)":
						nuevaPalabra = nuevaPalabra + re.sub("t", str(parametro), produccion.producciones)
			
			elif re.match("B(.*)", elemento) != None :
				cadenaParametro = re.split("B\(|\)", elemento)
				parametro = eval(cadenaParametro[1])
				if parametro > 0:
					for produccion in gramatica.producciones:
						if produccion.noTerminal == "B(t)":
							nuevaPalabra = nuevaPalabra + re.sub("t", str(parametro), produccion.producciones)
			
			elif re.match("G(.*)", elemento) != None :
				cadenaParametro = re.split("G\(|,|\)", elemento)
				nuevaS = int(cadenaParametro[1])*int(cadenaParametro[2])
	
				for produccion in gramatica.producciones:
					if produccion.noTerminal == "G(s,r)":
						print "entro"
						palabraAuxiliar = re.sub("s", str(nuevaS) , produccion.noTerminal)
						nuevaPalabra = nuevaPalabra + re.sub("r",cadenaParametro[2], palabraAuxiliar)
			else:
				nuevaPalabra = nuevaPalabra + elemento
			nuevaPalabra = re.sub("LA", str(LA), nuevaPalabra)
			nuevaPalabra = re.sub("RA", str(RA), nuevaPalabra)
			nuevaPalabra = re.sub("LB", str(LB), nuevaPalabra)
			nuevaPalabra = re.sub("RB", str(RB), nuevaPalabra)	
		print nuevaPalabra
		return nuevaPalabra