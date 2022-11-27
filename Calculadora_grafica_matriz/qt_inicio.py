from PyQt5 import uic, QtWidgets
import sys
from tkinter import messagebox 
from fractions import Fraction
import numpy as np

qtCreatorFile = "matriz.ui"
solucionador, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QtWidgets.QMainWindow, solucionador):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        solucionador.__init__(self)
        self.setupUi(self)
        self.setFixedSize(757,658)
        self.setWindowTitle('Solucionador de matrices') 
            
        # Operaciones con matrices    
        self.boton1.clicked.connect(self.det3x3)
        self.boton2.clicked.connect(self.det4x4)
        self.boton3.clicked.connect(self.ecu1)
        self.boton4.clicked.connect(self.ecu2)
        
        # ELiminacion de valores 
        self.boton_borrar1.clicked.connect(self.delete3x3)
        self.boton_borrar2.clicked.connect(self.delete4x4)
        self.boton_borrar3.clicked.connect(self.deleteEcu1)
        self.boton_borrar4.clicked.connect(self.deleteEcu2)


    def delete3x3(self):
        valores1 = [self.a11,self.a12,self.a13,
                    self.a21,self.a22,self.a23,
                    self.a31,self.a32,self.a33,
                    self.determinante]
        for i in range(len(valores1)):
            valores1[i].setText("")
        
        self.determinante.setText("")
            
    def delete4x4(self):
        valores2 = [self.a11_2,self.a12_2,self.a13_2,self.a14_2,
                    self.a21_2,self.a22_2,self.a23_2,self.a24_2,
                    self.a31_2,self.a32_2,self.a33_2,self.a34_2,
                    self.a41_2,self.a42_2,self.a43_2,self.a44_2,
                    self.determinante_2]
        for i in range(len(valores2)):
            valores2[i].setText("")

    def deleteEcu1(self):
        valores3 = [self.a11_4,self.a12_4,
                    self.a21_4,self.a22_4,
                    self.igual_5,self.igual_4,
                    self.solucion1]
        for i in range(len(valores3)):
            valores3[i].setText("")

    def deleteEcu2(self):
        valores4 = [self.a11_3,self.a12_3,self.a13_3,
                    self.a21_3,self.a22_3,self.a23_3,
                    self.a31_3,self.a32_3,self.a33_3,
                    self.igual_1,self.igual_2,
                    self.igual_3,self.solucion2]
        for i in range(len(valores4)):
            valores4[i].setText("")
            
    def det3x3(self):
        try:
            self.A = np.array(
            [
            [float(eval(self.a11.toPlainText())),float(eval(self.a12.toPlainText())),float(eval(self.a13.toPlainText()))],
            [float(eval(self.a21.toPlainText())),float(eval(self.a22.toPlainText())),float(eval(self.a23.toPlainText()))],
            [float(eval(self.a31.toPlainText())),float(eval(self.a32.toPlainText())),float(eval(self.a33.toPlainText()))]
            ])
            self.det = round(np.linalg.det(self.A))
            self.determinante.setText(str(self.det))
        except:
            messagebox.showerror("Alert","Error encontrado")
            
    def det4x4(self):
        try:
            self.B = np.array(
            [
            [float(eval(self.a11_2.toPlainText())),float(eval(self.a12_2.toPlainText())),float(eval(self.a13_2.toPlainText())),float(eval(self.a14_2.toPlainText()))],
            [float(eval(self.a21_2.toPlainText())),float(eval(self.a22_2.toPlainText())),float(eval(self.a23_2.toPlainText())),float(eval(self.a24_2.toPlainText()))],
            [float(eval(self.a31_2.toPlainText())),float(eval(self.a32_2.toPlainText())),float(eval(self.a33_2.toPlainText())),float(eval(self.a34_2.toPlainText()))],
            [float(eval(self.a41_2.toPlainText())),float(eval(self.a42_2.toPlainText())),float(eval(self.a43_2.toPlainText())),float(eval(self.a44_2.toPlainText()))]
            ])
            self.det = round(np.linalg.det(self.B))
            self.determinante_2.setText(str(self.det))
        except:
            messagebox.showerror("Alert","Error encontrado")

    def ecu1(self):
        try:
            self.D = np.array(
            [
            [float(eval(self.a11_4.toPlainText())),float(eval(self.a12_4.toPlainText()))],
            [float(eval(self.a21_4.toPlainText())),float(eval(self.a22_4.toPlainText()))]
            ])
            self.igualdad = np.array([float(eval(self.igual_5.toPlainText())),float(eval(self.igual_4.toPlainText()))])
            self.sol = np.linalg.inv(self.D).dot(self.igualdad)
            self.p = f"x = {Fraction(self.sol[0]).limit_denominator(100)}\ny = {Fraction(self.sol[1]).limit_denominator(100)}"
            self.solucion1.setText(str(self.p))
        except:
            messagebox.showerror("Alert","Error encontrado")

    def ecu2(self):
        try:
            self.C = np.array(
            [
            [float(eval(self.a11_3.toPlainText())),float(eval(self.a12_3.toPlainText())),float(eval(self.a13_3.toPlainText()))],
            [float(eval(self.a21_3.toPlainText())),float(eval(self.a22_3.toPlainText())),float(eval(self.a23_3.toPlainText()))],
            [float(eval(self.a31_3.toPlainText())),float(eval(self.a32_3.toPlainText())),float(eval(self.a33_3.toPlainText()))]
            ])
            self.igualdad = np.array([float(eval(self.igual_1.toPlainText())),float(eval(self.igual_2.toPlainText())),float(eval(self.igual_3.toPlainText()))])
            self.sol = np.linalg.inv(self.C).dot(self.igualdad)
            self.p = f"x = {Fraction(self.sol[0]).limit_denominator(100)}\ny = {Fraction(self.sol[1]).limit_denominator(100)}\nz = {Fraction(self.sol[2]).limit_denominator(100)}"
            self.solucion2.setText(str(self.p))
        except:
            messagebox.showerror("Alert","Error encontrado")
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Inicia la aplicacion
    window = Main() # Se establece una ventana
    window.show()
    app.exec_()