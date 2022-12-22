import java.util.Scanner;

public class mayor_menor {
    
    public static void main(String[] args)
    {
        float num1, num2;
        Scanner input = new Scanner(System.in);

        System.out.print("Introduce el primer numero: ");
        num1 = input.nextFloat();
        System.out.print("Introduce el segundo numero: ");
        num2 = input.nextFloat();

        if (num1 > num2)
        {
            System.out.print(num1 + " Es mayor a " + num2);
        }
        else if (num2 > num1)
        {
            System.out.print(num2 + " Es mayor a " + num1);
        }
        else if (num1 == num2)
        {
            System.out.print(num1 + " Es igual a " + num2);
        }else{
            System.out.print("Error");

        }
    }
}
