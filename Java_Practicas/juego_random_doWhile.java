import java.util.Scanner;

public class juego_random_doWhile {
    
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int numero=0, intentos=0, aleatorio = (int)(Math.random()*100);

    do {
            System.out.print("Introdue el numero: ");
            numero = input.nextInt();

            if (numero < aleatorio)
            {
                System.out.println("Te falto, te quedan: " + intentos + " Intentos.");
            }
            else if (numero > aleatorio)
            {
                System.out.println("Te pasaste, te quedan: " + intentos + " Intentos.");
                
            }
            intentos++;

        } while (numero != aleatorio );


        System.out.println("Le atinanste " + numero + " == " + aleatorio + " En el intento " + intentos);
    }   
}
