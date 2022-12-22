package multiplicacion_matriz;

public class salida {
    public static void mensaje(){

        int array_datos[] = entrada.input();

        int n1 = array_datos[0];
        int n2 = array_datos[1];
        int n3 = array_datos[2];
        int n4 = array_datos[3];

        int lista[][][] = proceso.process();

        int m1[][][] = lista[][][];
        int m2[0][1][1] = lista;

        for (byte i=0;i<n1;i++)
        {
            System.out.println();
            for (byte j=0; j<n2;j++)
            {
                System.out.print(lista1[i][j]);
            }
        }
        System.out.println();
        for (byte a=0;a<n3;a++)
        {
            System.out.println();
            for (byte b=0; b<n4;b++)
            {
                System.out.print(lista2[a][b]);
            }
        }
    }
}