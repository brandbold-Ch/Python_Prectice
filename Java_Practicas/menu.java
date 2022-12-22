import java.util.Scanner;

public class menu {
    
    public static void main(String[] args)
    {
        /*
         * 
         *  Escribir un programa que mediante un menú, permita: 
	     *      1. Imprimir intervalo.
	     *      2. Salir. 
         *  Si el usuario selecciona opción 1, el programa tendrá que solicitar dos números enteros, 
         *  correspondientes a un intervalo.
         *     * Si el valor de inicio es mayor al valor final, imprimir todos los números pares que estén
         *       desde el valor de inicio al valor final. 
         *     * En caso contrario, si el valor de inicio es menor al valor final, desplegar los números consecutivos 
         *       desde el valor de inicio al valor final. 
         *     * Si los números son iguales imprimir un mensaje indicándolo. 
         *  Si el usuario selecciona la opción 2, el programa termina la ejecución. 
         *  Si el usuario selecciona un número diferente de 1 o 2 el programa desplegará un mensaje de error.
         * 
         */
        String option;
        int num1, num2, i;

        Scanner input = new Scanner(System.in);
        
        System.out.print("\tMenu de opciones \n1._ Imprimir Intervalo \n2._ Salir \n\nOpcion > ");
        option = input.nextLine();

        switch (option)
        {
            case ("1"):
                System.out.print("Introduce el primer numero: ");
                num1 = input.nextInt();

                System.out.print("Introduce el segundo numero: ");
                num2 = input.nextInt();

                if (num1 > num2)
                {
                    if (num1 % 2 != 0)
                    {
                        num1 -= 1;
                    }
                    for (i=num1;i>=num2;i-=2)
                    {
                        System.out.println(i);
                    }
                }
                else if (num1 < num2)
                {
                    for (i=num1;i<=num2;i++)
                    {
                        System.out.println(i);
                    }
                }
                else if (num1 == num2)
                {
                    System.out.println(num1 + " es igual a " + num2);
                }
                System.exit(0);
            case ("2"):
                System.out.println("Programa Finalizado");
                System.exit(0);
            case (""):
                System.exit(0);
        } 
        System.out.println("Opcion no encontrada");
    }
}