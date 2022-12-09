from matriz_form import values
from Qtinterfaz import *

def dimensionT0(self):
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


def setValuesT0(self):

        try:
            if page2 == 2:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText()))],
                                  [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText()))]]

                self.eq = [float(eval(self.equal1.toPlainText())),
                           float(eval(self.equal2.toPlainText()))]

                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(
                    str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(
                    str(Fraction(self.valuesxy[1]).limit_denominator(100)))

            elif page2 == 3:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText()))],
                                  [float(eval(self.a12__2.toPlainText())), float(
                                      eval(self.a22__2.toPlainText())), float(eval(self.a32__2.toPlainText()))],
                                  [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(eval(self.a33__2.toPlainText()))]]

                self.eq = [float(eval(self.equal1.toPlainText())),
                           float(eval(self.equal2.toPlainText())),
                           float(eval(self.equal3.toPlainText()))]

                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(
                    str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(
                    str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                self.z.setText(
                    str(Fraction(self.valuesxy[2]).limit_denominator(100)))

            elif page2 == 4:
                self.listValue = [[float(eval(self.a11__2.toPlainText())), float(eval(self.a21__2.toPlainText())), float(eval(self.a31__2.toPlainText())), float(eval(self.a41__2.toPlainText()))],
                                  [float(eval(self.a12__2.toPlainText())), float(eval(self.a22__2.toPlainText())), float(
                                      eval(self.a32__2.toPlainText())), float(eval(self.a42__2.toPlainText()))],
                                  [float(eval(self.a13__2.toPlainText())), float(eval(self.a23__2.toPlainText())), float(
                                      eval(self.a33__2.toPlainText())), float(eval(self.a43__2.toPlainText()))],
                                  [float(eval(self.a14__2.toPlainText())), float(eval(self.a24__2.toPlainText())), float(eval(self.a34__2.toPlainText())), float(eval(self.a44__2.toPlainText()))]]

                self.eq = [float(eval(self.equal1.toPlainText())),
                           float(eval(self.equal2.toPlainText())),
                           float(eval(self.equal3.toPlainText())),
                           float(eval(self.equal4.toPlainText()))]

                self.valuesxy = np.linalg.inv(self.listValue).dot(self.eq)
                self.x.setText(
                    str(Fraction(self.valuesxy[0]).limit_denominator(100)))
                self.y.setText(
                    str(Fraction(self.valuesxy[1]).limit_denominator(100)))
                self.z.setText(
                    str(Fraction(self.valuesxy[2]).limit_denominator(100)))
                self.w.setText(
                    str(Fraction(self.valuesxy[3]).limit_denominator(100)))
        except:
            messagebox.showerror("Alert", "Error encontrado")

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