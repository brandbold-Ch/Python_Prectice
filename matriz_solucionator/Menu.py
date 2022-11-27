def message():
    
    data = """
   *****************************************************************
   *                            ATENCION                           *
   *                                                               *
   * Para introducir tus matrices no va a ser de la forma normal:  *
   *                         [a11 a12 a13                          *
   *                         a21 a22 a23                           *
   *                         a31 a32 a33]                          *
   * va a ser de esta forma: [a11 a12 a13 a21 a22 a23 a31 a32 a33],*
   * separa tus número con comas ',' porfavor o no funcionará.     *
   *---------------------------------------------------------------*
   *                     OPERACIONES CON MATRICES                  *
   *                                                               *
   *                 1._ Suma de Matrices                          *
   *                 2._ Resta de Matrices                         *
   *                 3._ Multiplicacion de matrices                *
   *                 4._ Determinante de una matriz                *
   *                 5._ Solucionador de sistema de ecuaciones     *
   *                 6._ About                                     *
   *                 7._ Salir                                     *
   *****************************************************************
    """
    return data

def config():
    
    alert = """
                                    ALERT
                                    
    Para resolver tu sistema de ecuaciones introduce los coeficientes 
    de las incognitas de la siguiete manera separando las igualdades.
    __ 
   | x + y - z = 12            |1  1 -1|        |12|
   < 2x -y + 3z + = 0  ------> |2 -1  3|------> |0 |
   |-x +4y -2z = 8             |-1 4 -2|        |8 |
   |__
   """
    return alert

def about():
    
    mi = """
    
    Soy alumno de la Uiversidad Politecnica de Tapachula en desarrollo de software,
    este es un trabajo con la finalidad de obtener un punto extra en la asignatura 
    de algebra lineal con el profesor David Enrique Vazquez Ramos, las faltas de
    ortografia se debe a que mi teclado esta en ingles y ademas podria dar un error
    en los mensajes por la codificacion. Hice este programa con pasion por la programacion.
    
                    ________00000000000___________000000000000_________
                    ______00000000_____00000___000000_____0000000______
                    ____0000000_____________000______________00000_____
                    ___0000000_______________0_________________0000____
                    __000000____________________________________0000___
                    __00000_____________________________________ 0000__
                    _00000______________________________________00000__
                    _00000_____________________________________000000__
                    __000000_________________________________0000000___
                    ___0000000______________________________0000000____
                    _____000000____________________________000000______
                    _______000000________________________000000________
                    __________00000_____________________0000___________
                    _____________0000_________________0000_____________
                    _______________0000_____________000________________
                    _________________000_________000___________________
                    _________________ __000_____00_____________________
                    ______________________00__00_______________________
                    ________________________00_________________________
"""
    return mi
      
message()
config()
about()