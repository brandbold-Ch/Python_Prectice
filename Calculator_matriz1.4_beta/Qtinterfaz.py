import sys
from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5 import QtWidgets, uic
from fractions import Fraction
#import time
from Tab_1 import T1

#inicio = time.time()
UIsystem, QtBaseClass = uic.loadUiType("UiMatriz.ui")

class Window(QtWidgets.QMainWindow, UIsystem):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Calculadora Matricial")

class Tabs(Window, T1):
    def __init__(self) -> None:
        super().__init__()
        self.tabWidget.currentChanged.connect(self.pages)
        self.tabWidget.setCurrentIndex(0)

    def pages(self):
        match self.tabWidget.currentIndex():
            case 0:
                print("Estoy en pestaña: 0")
                self.spinBox.valueChanged.connect(self.dimensionDet)

            case 1:
                print("Estoy en la pestaña: 1")
                self.spinBox2.valueChanged.connect(self.dimensionEcu)
        
    def events(self):
        
        #Pestaña 0: Determinantes.
        self.calcular.clicked.connect(self.setValues)
        self.limpiar.clicked.connect(self.clearValues) 
        
        #Pestaña 1: Sistema de ecuaciones.
        self.calcular2.clicked.connect(self.setValuesE)
        self.limpiar2.clicked.connect(self.clearValuesE)

        #Grafica de ecuaciones 2x2 y 3x3.
        self.graficar.clicked.connect(self.graphication2d)    
        self.graficar2.clicked.connect(self.graphication3d)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Inicia la aplicacion
    window = Tabs()
    window.events()# Se establece una ventana
    window.show()
    #print(Window.mro())
    #print(Tabs.mro())
    app.exec_()
    #fin = time.time()
    #print(fin-inicio) # 1.5099220275878906