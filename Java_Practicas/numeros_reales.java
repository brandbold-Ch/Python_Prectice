import java.util.Scanner;
public class numeros_reales {
    
    public static void main(String[] args)
    {
        /* 
        *   Realizar un programa donde se solicite 2 números reales y se determine lo siguiente:
        *    Los dos son negativos
        *    Los dos son positivos
        *    Uno de los dos es positivo
        *    Ambos números son igual a cero.
        */
        Scanner input = new Scanner(System.in);
        
        float num1, num2;

        do{
            System.out.print("Introduce el primer numero: ");
            num1 = input.nextFloat();

            System.out.print("Introduce el segundo numero: ");
            num2 = input.nextFloat();

            if (num1>0 && num2>0)
            {
                System.out.println(num1 +  " y " + num2 + " Son positivos");
            }
            else if(num1<0 && num2<0)
            {
                System.out.println(num1 +  " y " + num2 + " Son negativos");
            }
            else if(num1<0 && num2>0)
            {
                System.out.println(num1 +  " Es negativo y " + num2 + " Es positivo");
            }
            else if(num1>0 && num2<0)
            {
                System.out.println(num1 +  " Es positivo y " + num2 + " Es negativo");
            }
        } while((num1>0||num2>0) || (num1<0||num2<0));
        
        System.out.println("Ambos numero son ceros: " + num1 + " y " + num2);
    }
}