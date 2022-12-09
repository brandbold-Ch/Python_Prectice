from matriz_form import matrix
#rom PyQt5.QtWidgets import QWidget, QSpinBox
from Modules import *
from Qtinterfaz import Window

@Window.setter
def dimensionDet(self):
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


def setValues(self):

        try:
            if page == 2:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText()))],
                                  [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText()))]]
                self.determinante.setText(
                    str(round(np.linalg.det(self.listValue))))

            elif page == 3:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText()))],
                                  [float(eval(self.a12.toPlainText())), float(
                                      eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText()))],
                                  [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText()))]]
                self.determinante.setText(
                    str(round(np.linalg.det(self.listValue))))

            elif page == 4:
                self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText())), float(eval(self.a41.toPlainText()))],
                                  [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(
                                      eval(self.a32.toPlainText())), float(eval(self.a42.toPlainText()))],
                                  [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(
                                      eval(self.a33.toPlainText())), float(eval(self.a43.toPlainText()))],
                                  [float(eval(self.a14.toPlainText())), float(eval(self.a24.toPlainText())), float(eval(self.a34.toPlainText())), float(eval(self.a44.toPlainText()))]]
                self.determinante.setText(
                    str(round(np.linalg.det(self.listValue))))
        except:
            messagebox.showerror("Alert", "Error encontrado")

def clearValues(self):
    if page == 2:
        for i in self.index[0][:]:
            i.setText("")
        self.determinante.setText("")

    elif page == 3:
        for i in self.index[0][:] + self.index[1][:]:
            i.setText("")
        self.determinante.setText("")

    elif page == 4:
        for i in self.index[0][:] + self.index[1][:] + self.index[2][:]:
            i.setText("")
        self.determinante.setText("")