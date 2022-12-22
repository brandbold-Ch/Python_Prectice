import java.util.Scanner;
public class array_suma 
{
    public static void main(String[] args)
    {
        byte i;
        i = 0;

        Scanner input = new Scanner(System.in);

        byte array[] = new byte[9];
        byte array2[] = new byte[9];

        while (i<=array.length-1)
        {
            System.out.print("Introduce el valor del inidce " + i + ": ");
            array[i] = input.nextByte();
            i++;
        }
        
        for (byte lista:array)
        {
            System.out.println(lista);
        }
    }    
}