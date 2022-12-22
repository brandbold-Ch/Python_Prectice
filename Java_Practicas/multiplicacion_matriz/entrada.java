package multiplicacion_matriz;

import java.util.Scanner;   

public class entrada{

    public static int[] input(){

        Scanner input_my_array = new Scanner(System.in);

        System.out.print("Filas 1: ");
        int filas1 = input_my_array.nextInt();

        System.out.print("Columnas 1: ");
        int columnas1 = input_my_array.nextInt();

        System.out.print("Filas 2: ");
        int filas2 = input_my_array.nextInt();

        System.out.print("Columnas 2: ");
        int columnas2 = input_my_array.nextInt();

        int datos[] = {filas1, columnas1, filas2, columnas2};
            
        return datos;
    }
}