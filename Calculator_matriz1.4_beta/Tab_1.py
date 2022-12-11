from Tab_0 import T0
from tkinter import messagebox
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 
#from equation_graph import graphication

"""
Página solucionadora de sistema de ecuaciones,
máximo sistema de ecuaciones de 4x4.
"""
class T1(T0):
    def __init__(self) -> None:
        super().__init__()

    def dimensionEcu(self):
        self.indexE = [[self.a11__2,self.a21__2,self.a12__2,self.a22__2],[self.a31__2,self.a32__2,self.a13__2,self.a23__2,self.a33__2],[self.a41__2,self.a42__2,self.a43__2,self.a14__2,self.a24__2,self.a34__2,self.a44__2]]
        self.equalsE = [self.equal1, self.equal2, self.equal3, self.equal4]

        match self.spinBox2.value():
            case 2:
                for i in self.indexE[1][:] + self.indexE[2][:]:
                    i.hide()

                for j in self.equalsE[2:]:
                    j.hide()

                self.labelig3.hide()
                self.labelig4.hide()

                self.calcular2.clicked.connect(self.setValuesE)
                self.limpiar2.clicked.connect(self.clearValuesE)

            case 3:
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

            case 4:
                for i in self.indexE[0][:] + self.indexE[1][:] + self.indexE[2][:]:
                    i.show()

                for w in self.equalsE:
                    w.show()

                self.labelig1.show()
                self.labelig2.show()
                self.labelig3.show()
                self.labelig4.show()

    def setValuesE(self):
        try:
            match self.spinBox2.value():
                case 2:
                    self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText()))],[float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText()))]]

                    self.eq = [float(eval(self.equal1.toPlainText())),float(eval(self.equal2.toPlainText()))]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                    
                    print("Estoy en la ecuación 2x2")

                case 3:
                    self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText()))],
                                    [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText()))],
                                    [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText()))]]
                    self.eq = [float(eval(self.equal1.toPlainText())),float(eval(self.equal2.toPlainText())),float(eval(self.equal3.toPlainText()))]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                    self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                    
                    self.graficar.clicked.connect(self.graphication)
                    print("Estoy en la ecuación 3x3")
                    
                case 4:
                    self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText())), float(eval(self.a41__2.toPlainText()))],
                                    [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText())), float(eval(self.a42__2.toPlainText()))],
                                    [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText())), float(eval(self.a43__2.toPlainText()))],
                                    [float(eval(self.a14__2.toPlainText())), float(eval(self.a24__2.toPlainText())), float(eval(self.a34__2.toPlainText())), float(eval(self.a44__2.toPlainText()))]]
                    self.eq = [float(eval(self.equal1.toPlainText())),float(eval(self.equal2.toPlainText())),float(eval(self.equal3.toPlainText())),float(eval(self.equal4.toPlainText()))]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                    self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                    self.w.setText(str(Fraction(self.valuesxy[3]).limit_denominator(100)))
                    
                    print("Estoy en la ecuación 3x3")

        except:
            messagebox.showerror("Alert", "Error encontrado")
        finally:
            print("Entre en una excepción")

    def clearValuesE(self):
        match self.spinBox2.value():
            case 2:
                for i in self.indexE[0][:]:
                    i.setText("")

                self.equal1.setText("")
                self.equal2.setText("")
                self.x.setText("")
                self.y.setText("")

            case 3:
                for i in self.indexE[0][:] + self.indexE[1][:]:
                    i.setText("")

                self.equal1.setText("")
                self.equal2.setText("")
                self.equal3.setText("")

                self.x.setText("")
                self.y.setText("")
                self.z.setText("")

            case 4:
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
                
    def graphication(self):
        
        equation_system = self.listValue
        solution = self.valuesxy
        
        x, y = np.linspace(0,10,10), np.linspace(0,10,10)
        X, Y = np.meshgrid(x, y)
        
        for i in range(len(equation_system)-1):
            if equation_system[0][i]>0 or equation_system[0][i]<0:
                equation_system[0][i] = equation_system[0][i]*-1
        
        z1 = (solution[0] + equation_system[0][0]*X + equation_system[0][1]*Y)/equation_system[0][2]
        
        for j in range(len(equation_system)-1):
            if equation_system[1][j]>0 or equation_system[1][j]<0:
                equation_system[1][j] = equation_system[1][j]*-1
        
        z2 = (solution[1] + equation_system[1][0]*X + equation_system[1][1]*Y) / equation_system[1][2]
        
        for k in range(len(equation_system)-1):
            if equation_system[2][k]>0 or equation_system[2][k]<0:
                equation_system[2][k] = equation_system[2][k]*-1
        
        z3 = (solution[2] + equation_system[2][0]*X +equation_system[2][1]*Y)/equation_system[2][2]
                
        for a in range(len(equation_system)):
            for b in range(len(equation_system)):
                
                print(equation_system[a][b],", ")
                  
        fig = plt.figure()
        
        ax = fig.add_subplot(111,projection="3d")
        
        ax.plot_surface(X,Y,z1, alpha=0.5, cmap=cm.Accent, rstride=100, cstride=100)
        ax.plot_surface(X,Y,z2, alpha=0.5, cmap=cm.Paired, rstride=100, cstride=100)
        ax.plot_surface(X,Y,z3, alpha=0.5, cmap=cm.Pastel1, rstride=100, cstride=100)
        
        ax.plot((solution[0],), (solution[1],), (solution[2],), lw=2, c="k", marker="o",markersize=7, markeredgecolor="g", markerfacecolor="white")

        ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
        plt.show()