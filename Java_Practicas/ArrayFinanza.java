public class ArrayFinanza {
    
    public static void main(String[] args) {

        double array[][] = new double[6][5];
        double tarifa = 0.10;
        
        System.out.println(array.length);

        double euro = 10000;

        for (int i=0; i<6; i++) 
        {
            array[i][0]= euro;

            for (int j=1; j<5; j++) 
            {
                double acumulador = euro+(euro*tarifa);
                array[i][j] = acumulador;
            }
            tarifa += 0.01;
        }
        for (int x=0; x<6; x++)
        {
            System.out.println();

            for (int y=0; y<5; y++)
            {
                System.out.print(array[x][y] + ", ");
            }
        }
    }
}