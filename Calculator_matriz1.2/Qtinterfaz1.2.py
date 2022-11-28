import sys
from PyQt5.QtWidgets import QWidget, QTabWidget, QSpinBox
from PyQt5 import QtWidgets, uic
import numpy as np
from fractions import Fraction
from tkinter import messagebox

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
                    self.a13, self.a23, self.a33],
                    [self.a41, self.a42, self.a43, self.a14, self.a24, self.a34, self.a44]]
        
        self.indexE = [
                    [self.a11__2, self.a21__2,
                    self.a12__2, self.a22__2],
                    [self.a31__2, self.a32__2, 
                    self.a13__2, self.a23__2, self.a33__2],
                    [self.a41__2, self.a42__2, self.a43__2, self.a14__2, self.a24__2, self.a34__2, self.a44__2]]
        
        self.equalsE = [self.equal1, self.equal2, self.equal3, self.equal4]
        
        self.tabWidget.currentChanged.connect(self.pages)

    def pages(self):
        if self.tabWidget.currentIndex() == 0:
            print("0")
            self.spinBox.valueChanged.connect(self.dimensionM)

        elif self.tabWidget.currentIndex() == 1:
            print("1")
            self.spinBox2.valueChanged.connect(self.dimensionE)

        elif self.tabWidget.currentIndex() == 2:
            print("2")
            self.spinBox.valueChanged.connect(self.dimensionM)

        elif self.tabWidget.currentIndex() == 3:
            print("3")
            self.spinBox.valueChanged.connect(self.dimensionM)

    def dimensionM(self):
        global page
        page = self.spinBox.value()
        
        if self.spinBox.value() == 2:
            
            for i in self.index[1][:] + self.index[2][:]:
                i.hide()

            self.calcular.clicked.connect(self.setValues)
            self.limpiar.clicked.connect(self.clearValues)
            
        elif self.spinBox.value() == 3:
            for i in self.index[2][:]:
                i.hide()
                
            for j in self.index[1][:]:
                j.show()
                
            self.calcular.clicked.connect(self.setValues)
            self.limpiar.clicked.connect(self.clearValues)
            
        elif self.spinBox.value() == 4:
            for i in self.index[0][:] + self.index[1][:] + self.index[2][:]:
                i.show()
        
    def dimensionE(self):
        global page2
        page2 = self.spinBox2.value()

        if self.spinBox2.value() == 2:

            for i in self.indexE[1][:] + self.indexE[2][:]:
                i.hide()
                
            for j in self.equalsE[2:]:
                j.hide()

            self.labelig3.hide()
            self.labelig4.hide()

            self.calcular2.clicked.connect(self.setValuesE)
            self.limpiar2.clicked.connect(self.clearValuesE)

        elif self.spinBox2.value() == 3:
            for i in self.indexE[2][:]:
                i.hide()

            for j in self.indexE[1][:]:
                j.show()
                
            for k in self.equalsE[:3]:
                k.show()
                
            self.equalsE[3].hide()
            
            self.labelig1.show()
            self.labelig2.show()
            self.labelig3.show()
            self.labelig4.hide()

            self.calcular2.clicked.connect(self.setValuesE)
            self.limpiar2.clicked.connect(self.clearValuesE)

        elif self.spinBox2.value() == 4:
            for i in self.indexE[0][:] + self.indexE[1][:] + self.indexE[2][:]:
                i.show()
                
            for w in self.equalsE:
                w.show()

            self.labelig1.show()
            self.labelig2.show()
            self.labelig3.show()
            self.labelig4.show()
    
    def setValues(self):
        
        try:
            if page == 2:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText()))],
                                [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText()))]]
                self.determinante.setText(str(round(np.linalg.det(self.listValue))))

            elif page == 3:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText()))],
                                [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText()))],
                                [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText()))]]
                self.determinante.setText(str(round(np.linalg.det(self.listValue))))
            
            elif page == 4:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText())), float(eval(self.a41.toPlainText()))],
                                [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText())), float(eval(self.a42.toPlainText()))],
                                [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText())), float(eval(self.a43.toPlainText()))],
                                [float(eval(self.a14.toPlainText())), float(eval(self.a24.toPlainText())), float(eval(self.a34.toPlainText())), float(eval(self.a44.toPlainText()))]]
                self.determinante.setText(str(round(np.linalg.det(self.listValue))))
        except:
            messagebox.showerror("Alert","Error encontrado")


    def clearValues(self):
        if page == 2:
            for i in self.index[0][:]:
                i.setText("")
            self.determinante.setText("")
        
        if page == 3:
            for i in self.index[0][:] + self.index[1][:]:
                i.setText("")
            self.determinante.setText("")
        
        if page == 4:
            for i in self.index[0][:] + self.index[1][:]+ self.index[2][:]:
                i.setText("")
            self.determinante.setText("")
            
    def setValuesE(self):
        
        try:
            if page2 == 2:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText()))],
                                [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText()))]]
                
                self.eq = [float(eval(self.equal1.toPlainText())),
                        float(eval(self.equal2.toPlainText()))]
                
                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))

            elif page2 == 3:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText()))],
                                [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText()))],
                                [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText()))]]
            
                self.eq = [float(eval(self.equal1.toPlainText())),
                        float(eval(self.equal2.toPlainText())),
                        float(eval(self.equal3.toPlainText()))]

                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))

            elif page2 == 4:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText())), float(eval(self.a41__2.toPlainText()))],
                                [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText())), float(eval(self.a42__2.toPlainText()))],
                                [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText())), float(eval(self.a43__2.toPlainText()))],
                                [float(eval(self.a14__2.toPlainText())), float(eval(self.a24__2.toPlainText())), float(eval(self.a34__2.toPlainText())), float(eval(self.a44__2.toPlainText()))]]
                
                self.eq = [float(eval(self.equal1.toPlainText())),
                        float(eval(self.equal2.toPlainText())),
                        float(eval(self.equal3.toPlainText())),
                        float(eval(self.equal4.toPlainText()))]

                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                self.w.setText(str(Fraction(self.valuesxy[3]).limit_denominator(100)))
        except:
            messagebox.showerror("Alert","Error encontrado")


    def clearValuesE(self):
        if page2 == 2:
            for i in self.indexE[0][:]:
                i.setText("")
            
            self.equal1.setText("")
            self.equal2.setText("")
            self.x.setText("")
            self.y.setText("")


        if page2 == 3:
            for i in self.indexE[0][:] + self.indexE[1][:]:
                i.setText("")
            
            self.equal1.setText("")
            self.equal2.setText("")
            self.equal3.setText("")
            
            self.x.setText("")
            self.y.setText("")
            self.z.setText("")

        if page2 == 4:
            for i in self.indexE[0][:] + self.indexE[1][:] + self.indexE[2][:]:
                i.setText("")
                
            self.equal1.setText("")
            self.equal2.setText("")
            self.equal3.setText("")
            self.equal4.setText("")
            
            self.x.setText("")
            self.y.setText("")
            self.z.setText("")
            self.w.setText("")
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Inicia la aplicacion
    window = Tabs()  # Se establece una ventana
    window.show()
    app.exec_()