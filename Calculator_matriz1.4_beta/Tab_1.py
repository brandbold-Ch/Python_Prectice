from Tab_0 import T0
from tkinter import messagebox
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 

"""
Página solucionadora de sistema de ecuaciones,
máximo sistema de ecuaciones de 4x4.
"""
class T1(T0):
    def __init__(self) -> None:
        super().__init__()

    def dimensionEcu(self):
        self.indexE = [
                        [self.a11__2,self.a21__2,self.a12__2,self.a22__2],
                        [self.a31__2,self.a32__2,self.a13__2,self.a23__2,self.a33__2],
                        [self.a41__2,self.a42__2,self.a43__2,self.a14__2,self.a24__2,self.a34__2,self.a44__2]
                    ]
        self.equalsE = [self.equal1, self.equal2, self.equal3, self.equal4]

        match self.spinBox2.value():
            case 2:
                for i in self.indexE[1][:] + self.indexE[2][:]:
                    i.hide()

                for j in self.equalsE[2:]:
                    j.hide()

                self.labelig3.hide()
                self.labelig4.hide()
                self.graficar.show()
                self.graficar2.hide()

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
                self.graficar2.show()
                self.graficar.hide()

            case 4:
                for i in self.indexE[0][:] + self.indexE[1][:] + self.indexE[2][:]:
                    i.show()

                for w in self.equalsE:
                    w.show()

                self.labelig1.show()
                self.labelig2.show()
                self.labelig3.show()
                self.labelig4.show()
                self.graficar2.hide()
                self.graficar.hide()

    def setValuesE(self):
        match self.spinBox2.value():
            case 2:
                try:
                    self.listValue = [
                                        [float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText()))],
                                        [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText()))]
                                    ]

                    self.eq = [float(eval(self.equal1.toPlainText())),float(eval(self.equal2.toPlainText()))]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                        
                    print("Estoy en la ecuación 2x2")
                except:
                    messagebox.showerror("Alert", "Error encontrado")

            case 3:
                try:
                    self.listValue = [
                                        [float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText()))],
                                        [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText()))],
                                        [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText()))]
                                    ]
                    self.eq = [
                                float(eval(self.equal1.toPlainText())),
                                float(eval(self.equal2.toPlainText())),
                                float(eval(self.equal3.toPlainText()))
                            ]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                    self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                        
                    print("Estoy en la ecuación 3x3")
                except:
                    messagebox.showerror("Alert", "Error encontrado")

            case 4:
                try:
                    self.listValue = [
                                        [float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText())), float(eval(self.a41__2.toPlainText()))],
                                        [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText())), float(eval(self.a42__2.toPlainText()))],
                                        [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText())), float(eval(self.a43__2.toPlainText()))],
                                        [float(eval(self.a14__2.toPlainText())), float(eval(self.a24__2.toPlainText())), float(eval(self.a34__2.toPlainText())), float(eval(self.a44__2.toPlainText()))]
                                    ]
                    self.eq = [
                                    float(eval(self.equal1.toPlainText())),float(eval(self.equal2.toPlainText())),
                                    float(eval(self.equal3.toPlainText())),float(eval(self.equal4.toPlainText()))
                                ]

                    self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                    self.x.setText(str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                    self.y.setText(str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                    self.z.setText(str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                    self.w.setText(str(Fraction(self.valuesxy[3]).limit_denominator(100)))
                        
                    print("Estoy en la ecuación 4x4")
                except:
                    messagebox.showerror("Alert", "Error encontrado")
            
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
                
    def graphication2d(self):
        try:
            x = np.linspace(-5,5,100)
            a = self.listValue
            b = self.eq

            #Despeje de ecuciones para Y
            for i in range(len(a)):
                print("")
                for j in range(len(a)-1):
                    a[i][j] *= -1

            for q in range(len(a)):
                print("")
                for w in range(len(a)):
                    print(a[q][w])

            y1 = (b[0] + a[0][0]*x) / a[0][1]
            y2 = (b[1] + a[1][0]*x) / a[1][1]

            f1 = f"y1 = ({b[0]} {a[0][0]}*x) / {a[0][1]}"
            f2 = f"y2 = ({b[1]} {a[1][0]}*x) / {a[1][1]}"

            plt.plot(x, y1, c="r", label=f1)
            plt.plot(x, y2, c="b", label=f2)

            plt.title('Gráfica de sistema de ecuaciones')

            plt.xlabel('x', color='#1C2833'); plt.ylabel('y', color='#1C2833'); plt.legend(loc='upper left')

            plt.grid()
            plt.show()
        except:
            messagebox.showerror("Alert", "Error encontrado")

                
    def graphication3d(self):
        try:
            equation_system = self.listValue
            solution = self.valuesxy
            equals = self.eq
            
            print(equation_system)
            print(equals)
            print(solution)
            
            x, y = np.linspace(0,50,50), np.linspace(0,50,50)
            X, Y = np.meshgrid(x, y)
            
            #Despeje de ecuaiciones para Z
            for i in range(len(equation_system)):
                for j in range(len(equation_system)-1):
                    if equation_system[i][j] > 0 or equation_system[i][j] < 0:
                        equation_system[i][j] *= -1
                        
            z1 = (equals[0] + equation_system[0][0]*X + equation_system[0][1]*Y)/equation_system[0][2]
            z2 = (equals[1] + equation_system[1][0]*X + equation_system[1][1]*Y) /equation_system[1][2]
            z3 = (equals[2] + equation_system[2][0]*X +equation_system[2][1]*Y)/equation_system[2][2]
            
            for a in range(len(equation_system)):
                print("")
                for b in range(len(equation_system)):    
                    print(equation_system[a][b], end=", ")
                    
            fig = plt.figure()
            
            ax = fig.add_subplot(111,projection="3d")

            ax.plot_surface(X,Y,z1, alpha=0.5, cmap=cm.Accent, rstride=100, cstride=100)
            ax.plot_surface(X,Y,z2, alpha=0.5, cmap=cm.Paired, rstride=100, cstride=100)
            ax.plot_surface(X,Y,z3, alpha=0.5, cmap=cm.Pastel1, rstride=100, cstride=100)
            
            ax.plot((solution[0],), (solution[1],), (solution[2],), lw=2, c="k", marker="o",markersize=7, markeredgecolor="g", markerfacecolor="white")

            ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
            plt.show()
        except:
            messagebox.showerror("Alert", "Error encontrado")