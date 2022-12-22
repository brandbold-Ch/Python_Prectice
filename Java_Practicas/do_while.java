import java.util.Scanner;

public class do_while {
    
    public static void main(String[] args){;

        Scanner input = new Scanner(System.in);

        Double num; 

        do{

            // Calculador de Raiz Cuadrada
            
            System.out.print("Introduce un numero: ");
            
            num = input.nextDouble();

            float num2 = (float) Math.sqrt(num) ;

            System.out.print("Raiz = ");
            System.out.printf("%1.2f", + num2);
            System.out.println(" ");

        }   while (num > 0);            
    }
}
