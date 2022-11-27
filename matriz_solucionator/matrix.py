#!/usr/bin/env python
import Menu
import os
from fractions import Fraction
import numpy as np
import msvcrt

while True:
    class Matriz(): 
        def __init__(self, args, args2):
            self.matriz_1, self.matriz_2 = args, args2            
        
        def trasformacion(self):
            try:
                self.a = self.matriz_1.split(",")
                self.b = self.matriz_2.split(",")
                self.__A = [float(eval(self.a[i])) for i in range(len(self.a))]
                self.__B = [float(eval(self.b[i])) for i in range(len(self.b))]
            except:
                os.system("cls")
                print("Error inesperado\nPresiona cualquier tecla para salir")                
            
        def suma_matriz(self):
            for x in range(1,11):
                if ((len(self.__A)==x**2) and (len(self.__B)==x**2)):
                    self.__suma = [self.__A[j]+self.__B[j] for j in range(len(self.__A))]
                    if (len(self.__suma) <= 3):
                        os.system("cls")
                        print("Matriz incompleta")
                    else:
                        print(f"A + B = \n{tuple(self.__suma)}")
                        print("Presiona cualquier tecla para continuar")
                    break
            else:
                os.system("cls")
                print("No son matrices cuadradas")
                
        def resta_matriz(self):
            for x in range(1,11):
                if ((len(self.__A)==x**2) and (len(self.__B)==x**2)):
                    self.__resta = [self.__A[j]-self.__B[j] for j in range(len(self.__A))]
                    if (len(self.__resta) <= 3):
                        os.system("cls")
                        print("Matriz incompleta")
                    else:
                        print(f"A - B = \n{tuple(self.__resta)}")
                        print("Presiona cualquier tecla para continuar")
                    break
            else:
                os.system("cls")
                print("No son matrices cuadradas")
    
        def multiplicacion_matriz(self,filaA, columnaA, filaB, columnaB):
            self.filaA = filaA
            self.columnaA = columnaA
            self.filaB = filaB
            self.columnaB = columnaB
            self.__A = np.array(self.__A).reshape(filaA, columnaA)
            self.__B = np.array(self.__B).reshape(filaB, columnaB)
            print(f"A x B = \n{np.dot(self.__A,self.__B)}")
            print("Presiona cualquier tecla para continuar")
            
        def determinante(self, filaA, columnaA):
            self.filaA = filaA
            self.columnaA = columnaA
            self.a = self.matriz_1.split(",")
            self.__A = [float(eval(self.a[i])) for i in range(len(self.a))]
            if (len(self.__A) == (self.filaA*self.columnaA)):
                self.__A = np.array(self.__A).reshape(filaA, columnaA)
                self.det = f"{np.linalg.det(self.__A):.3f}"
                print(f"det(A) = {Fraction(str(self.det))} ---> {self.det}")
                print("Presiona cualquier tecla para continuar")
            else:
                os.system("cls")
                print("No es matriz cuadrada")

    class ecuation_solve():
        def __init__(self,filaA, columnaA, matriz, igualdad):
            self.filaA,self.columnaA,self.__A,self.igualdad = filaA,columnaA,matriz,igualdad
            self.a = self.__A.split(",")
            self.b = self.igualdad.split(",")
            
        def operating(self):
            try:
                self.__A = [float(eval(self.a[i])) for i in range(len(self.a))]
                self.igualdad = np.array([float(eval(self.b[i])) for i in range(len(self.b))])
                if (len(self.__A) == (self.filaA*self.columnaA)):
                    self.__A = np.array(self.__A).reshape(self.filaA, self.columnaA)
                    self.solutions = np.linalg.inv(self.__A).dot(self.igualdad)
                    if (len(self.solutions)==2):
                        print(f"x = {self.solutions[0]}\ny = {self.solutions[1]}")
                    elif (len(self.solutions)==3):
                        print(f"x = {self.solutions[0]}\ny = {self.solutions[1]}\nz = {self.solutions[2]}")
                        print("Presiona cualquier tecla para continuar")
                    else:
                        print(self.solutions)
                    print("Presiona cualquier tecla para continuar")
                else:
                    os.system("cls")
                    print("No es matriz cuadrada")
            except:
                os.system("cls")
                print("Error inesperado\nPresiona cualquier tecla para salir")
                    
    class Option():
        print(Menu.message())
        def __init__(self, option):
            self.option = option
                
        def selection(self):  
            if (self.option=='1'):
                try:
                    A = Matriz(input("A = "),input("B = "))
                    A.trasformacion()
                    A.suma_matriz()
                except:
                    print("Valores erroneos")
                    
            elif (self.option=='2'):
                try:
                    B = Matriz(input("A = "),input("B = "))
                    B.trasformacion()
                    B.resta_matriz()
                except:
                    print("Valores erroneos")
                    
            elif (self.option=='3'):
                try:
                    a = int(input("Filas A >> "))
                    b = int(input("Columnas A >> "))
                    c = int(input("Filas B >> "))
                    d = int(input("Columnas B >> "))
                    if (b!=c):
                        print("No son operables")
                    else:   
                        C = Matriz(input("A = "),input("B = "))
                        C.trasformacion()
                        C.multiplicacion_matriz(a,b,c,d)
                except:
                    print("Valores erroneos")      
            
            elif (self.option=='4'):
                try:
                    a = int(input("Filas A >> "))
                    b = int(input("Columnas A >> "))
                    if (a != b):
                        os.system("cls")
                        print("No es matriz cuadrada")
                    else:
                        D = Matriz(input("A = "),None)
                        D.determinante(a,b)
                except:
                    print("Valores erroneos")
              
            elif (self.option=='5'):
                try:
                    print(Menu.config())
                    a = int(input("Filas A >> "))
                    b = int(input("Columnas A >> "))
                    if (a != b):
                        os.system("cls")
                        print("No es matriz cuadrada")
                    else:
                        E = ecuation_solve(a,b,input("A = "),input("Igualdades >> "))
                        E.operating()
                except:
                    print("Valores erroneos")
                    
            elif (self.option=='6'):
                print(Menu.about())
                print("Presiona cualquier tecla para salir")
            elif (self.option=='7'):
                exit()
            else:
                os.system("cls")
                print("No disponible\nPresiona cualquier tecla para salir")
    
    f = Option(input("Selecciona >> "))
    f.selection()
    msvcrt.getch()