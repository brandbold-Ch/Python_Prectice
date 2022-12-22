import java.util.Scanner;

public class AhogadoArray
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        char palabra[] = {'a','l','g','o','r','i','t','m','o','s'};
        palabra[0] = 'a';
        palabra[3] = 'o';
        palabra[8] = 'o';
        
        char adivina[] = new char[palabra.length];
        
        byte limite = 1;
        
        do 
        {
            for(byte i=0;i<adivina.length;i++)
            {
                String convercion = palabra.toString();
                System.out.println(convercion);
                System.out.print("Adivina la palabra: ");
                char index = input.next().charAt(0);
                
                if (palabra[i]==adivina[i])
                {
                    adivina[i] = index;
                    System.out.print(convercion);
                }
                if (limite==6)
                {
                    System.out.println("Se terminaron los intentos");
                    break;
                }
            }
            limite++;
        }while(limite==6);
    }
}