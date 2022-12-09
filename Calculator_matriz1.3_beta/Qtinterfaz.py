from Modules import *

UIsystem, QtBaseClass = uic.loadUiType("UiMatriz.ui")

class Window(QtWidgets.QMainWindow, UIsystem):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Solucionador de matrices")

class Tabs(Window):
    def __init__(self) -> None:
        super().__init__()
        self.tabWidget.currentChanged.connect(self.pages)
        global index
        #index = matrix(self)
        #index.elements()

    def pages(self):
        if self.tabWidget.currentIndex() == 0:
            print("0")
            self.spinBox.valueChanged.connect(self.dimensionT0)

        elif self.tabWidget.currentIndex() == 1:
            print("1")
            #self.spinBox2.valueChanged.connect(dimensionE)
            
    def dimensionT0(self):
        global page
        page = self.spinBox.value()
        if self.spinBox.value() == 2:

            for i in self.elements[1][:] + self.elements[2][:]:
                i.hide()

            self.calcular.clicked.connect(self.setValues)
            self.limpiar.clicked.connect(self.clearValues)

        elif self.spinBox.value() == 3:
            for i in self.elements[2][:]:
                i.hide()

            for j in self.elements[1][:]:
                j.show()

            self.calcular.clicked.connect(self.setValues)
            self.limpiar.clicked.connect(self.clearValues)

        elif self.spinBox.value() == 4:
            for i in self.elements[0][:] + self.elements[1][:] + self.elements[2][:]:
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
                                [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText()))],
                            [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText()))]]
            self.determinante.setText(
            str(round(np.linalg.det(self.listValue))))

        elif page == 4:
            self.listValue = [[float(eval(self.a11.toPlainText())), float(eval(self.a21.toPlainText())), float(eval(self.a31.toPlainText())), float(eval(self.a41.toPlainText()))],
                            [float(eval(self.a12.toPlainText())), float(eval(self.a22.toPlainText())), float(eval(self.a32.toPlainText())), float(eval(self.a42.toPlainText()))],
                            [float(eval(self.a13.toPlainText())), float(eval(self.a23.toPlainText())), float(eval(self.a33.toPlainText())), float(eval(self.a43.toPlainText()))],
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Inicia la aplicacion
    window = Tabs()  # Se establece una ventana
    window.show()
    app.exec_()