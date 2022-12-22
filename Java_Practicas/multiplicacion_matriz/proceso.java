package multiplicacion_matriz;
import java.util.Scanner;   

public class proceso {

    public static int[][][] process(){

        int array_datos[] = entrada.input();

        int n1 = array_datos[0];
        int n2 = array_datos[1];
        int n3 = array_datos[2];
        int n4 = array_datos[3];

        Scanner input_my_array2 = new Scanner(System.in);
        int array1[][] = new int[n1][n2];
        int array2[][] = new int[n3][n4];

        for (byte i=0;i<n1;i++)
        {
            System.out.println();
            for (byte j=0; j<n2;j++)
            {
                System.out.print(array1[i][j]);
                array1[i][j] = input_my_array2.nextInt();
            }
        }
        System.out.println();
        for (byte a=0;a<n3;a++)
        {
            System.out.println();
            for (byte b=0; b<n4;b++)
            {
                System.out.print(array2[a][b]);
                array2[a][b] = input_my_array2.nextInt();
            }
        }
        
        int[][][] data = {array1,array2};
        return data;
    }
}

