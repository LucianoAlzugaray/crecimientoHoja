	# -*- coding: utf-8 -*-
import pyqtgraph as pg
from graficador import Graficador
from gramatica import *
from pyqtgraph.Qt import QtCore, QtGui

# Configuraciones iniciales a la hoja
iteraciones = 20
grados = 60
tamanioInicialPrincipal = 5
razonCrecimientoPrincipal = 1
tamanioInicialLateral = 5
razonCrecimientoLateral = 1
decrecimientoPotencial = 1

#Crea la ventana y genera el graficador
pg.setConfigOptions(antialias=True)
w = pg.GraphicsWindow()
w.setWindowTitle('Sistemas L: Crecimiento de Hoja')
g = Graficador(w)

# Se genera la gramatica del L-Sistema
start = Produccion("S", "{.A(0)}")		
noTerminales = ["S","A(t)", "B", "G(s,r)", "C" ]
produccionesIniciales =[Produccion("A(t)", "G(LA,RA)[-B(t).][A(t+1)][+B(t).]"),
						Produccion("B(t)", "G(LB,RB)B(t-PD)"), 
						Produccion("G(s,r)", "G(s*r,r)")]
gramaticaL = LindenmayerSystem(start, noTerminales, produccionesIniciales)

#Se crea el derivador para cada retraso
d = Derivador()
palabra = d.derivar(gramaticaL, 
	start.noTerminal, 
	decrecimientoPotencial,
	tamanioInicialPrincipal,
	razonCrecimientoPrincipal,
	tamanioInicialLateral,
	razonCrecimientoLateral,
	)
for i in range(0,iteraciones):
	palabra = d.derivar(gramaticaL, 
		palabra, 
		decrecimientoPotencial,
		tamanioInicialPrincipal,
		razonCrecimientoPrincipal,
		tamanioInicialLateral,
		razonCrecimientoLateral,
		)
	g.graficar(palabra, grados)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
