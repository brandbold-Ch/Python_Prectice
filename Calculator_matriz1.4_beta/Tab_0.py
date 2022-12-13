from tkinter import messagebox
import numpy as np
from PyQt5.QtWidgets import QSpinBox

"""
Página solucionadora de determinates,
máximo determinante de 4x4.
"""
class T0(QSpinBox):
    def __init__(self) -> None:
        super().__init__(self)

    def dimensionDet(self):
        self.elements = [
                            [self.a11,self.a21,self.a12,self.a22],
                            [self.a31,self.a32,self.a13,self.a23,self.a33],
                            [self.a41,self.a42,self.a43,self.a14,self.a24,self.a34,self.a44]
                        ]  
        match self.spinBox.value():
            case 2:
                for i in self.elements[1][:] + self.elements[2][:]:
                    i.hide()

            case 3:
                for i in self.elements[2][:]:
                    i.hide()

                for j in self.elements[1][:]:
                    j.show()

            case 4:
                for i in self.elements[0][:] + self.elements[1][:] + self.elements[2][:]:
                    i.show()

    def setValues(self):
        match self.spinBox.value():
            case 2:
                try:
                    self.listValue = [
                                        [float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText()))],
                                        [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText()))]
                                    ]
                    self.determinante.setText(str(round(np.linalg.det(self.listValue))))
                except:
                    messagebox.showerror("Alert", "Error encontrado")

            case 3:
                try:
                    self.listValue = [
                                        [float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText()))],
                                        [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText()))],
                                        [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText()))]
                                    ]
                    self.determinante.setText(str(round(np.linalg.det(self.listValue))))
                except:
                    messagebox.showerror("Alert", "Error encontrado")

            case 4:
                try:
                    self.listValue = [
                                        [float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText())), float(eval(self.a41.toPlainText()))],
                                        [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText())), float(eval(self.a42.toPlainText()))],
                                        [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText())), float(eval(self.a43.toPlainText()))],
                                        [float(eval(self.a14.toPlainText())), float(eval(self.a24.toPlainText())), float(eval(self.a34.toPlainText())), float(eval(self.a44.toPlainText()))]
                                    ]
                    self.determinante.setText(str(round(np.linalg.det(self.listValue))))
                except:
                    messagebox.showerror("Alert", "Error encontrado")

    def clearValues(self):
        match self.spinBox.value():
            case 2:
                for i in self.elements[0][:]:
                    i.setText("")
                self.determinante.setText("")

            case 3:
                for i in self.elements[0][:] + self.elements[1][:]:
                    i.setText("")
                self.determinante.setText("")

            case 4:
                for i in self.elements[0][:] + self.elements[1][:] + self.elements[2][:]:
                    i.setText("")
                self.determinante.setText("")