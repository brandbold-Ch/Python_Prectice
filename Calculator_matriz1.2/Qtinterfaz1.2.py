import sys
from PyQt5.QtWidgets import QWidget, QTabWidget, QSpinBox
from PyQt5 import QtWidgets, uic
import numpy as np

UIsystem, QtBaseClass = uic.loadUiType("UiMatriz.ui")

class Window(QtWidgets.QMainWindow, UIsystem):
    
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Solucionador de matrices")

class Tabs(Window):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.index = [
                    [self.a11, self.a21,
                    self.a12, self.a22],
                    [self.a31, self.a32, 
                    self.a13, self.a23,self.a33],
                    [self.a41, self.a42, self.a43, self.a14, self.a24, self.a34, self.a44]]
        
        self.tabWidget.currentChanged.connect(self.pages)

    def pages(self):
        if self.tabWidget.currentIndex() == 0:
            print("0")
            self.spinBox.valueChanged.connect(self.dimensionM)
            
        elif self.tabWidget.currentIndex() == 1:
            print("1")
            self.spinBox.valueChanged.connect(self.dimensionM)
        
        elif self.tabWidget.currentIndex() == 2:
            print("2")
            self.spinBox.valueChanged.connect(self.dimensionM)
            
        elif self.tabWidget.currentIndex() == 3:
            print("3")
            self.spinBox.valueChanged.connect(self.dimensionM)
    
    def dimensionM(self):
        if self.spinBox.value() == 2:
            global page
            page = self.spinBox.value()
            for i in self.index[1][:] + self.index[2][:]:
                i.hide()

            self.calcular.clicked.connect(self.setValues)
            
        elif self.spinBox.value() == 3:
            for i in self.index[2][:]:
                i.hide()
                
            for j in self.index[1][:]:
                j.show()
                
        elif self.spinBox.value() == 4:
            for i in self.index[0][:] + self.index[1][:] + self.index[2][:]:
                i.show()
                
    def setValues(self):
        if page == 2:
            self.listValue = [float(eval(k.toPlainText())) for k in self.index[0][:]]
            self.listValue = np.reshape(self.listValue, (page,page))
            print(self.listValue)
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Inicia la aplicacion
    window = Tabs()  # Se establece una ventana
    window.show()
    app.exec_()