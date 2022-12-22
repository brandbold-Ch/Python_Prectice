import java.util.Scanner;

public class calculadora {
    
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        float num1, num2;
        String option;

        System.out.print("\n\tOperaciones \n1._ Suma \n2._ Resta \n3._ Multiplicacion \n4._ Division \n5._ Modulo \nOpcion>> ");
        option = input.next();

        switch (option)
        {
            case ("1"):
                System.out.print("Introduce el primer numero: ");
                num1 = input.nextFloat();
                System.out.print("Introduce el segundo numero: ");
                num2 = input.nextFloat();

                System.out.println("Tu suma es: " + (num1+num2));
                break;
            case ("2"):
            
                System.out.print("Introduce el primer numero: ");
                num1 = input.nextFloat();
                System.out.print("Introduce el segundo numero: ");
                num2 = input.nextFloat();

                System.out.println("Tu resta es: " + (num1-num2));
                break;      
            case ("3"):
                
                System.out.print("Introduce el primer numero: ");
                num1 = input.nextFloat();
                System.out.print("Introduce el segundo numero: ");
                num2 = input.nextFloat();

                System.out.println("Tu multiplicacion es: " + (num1*num2));
                break;
            case ("4"):
                System.out.print("Introduce el primer numero: ");
                num1 = input.nextFloat();
                System.out.print("Introduce el segundo numero: ");
                num2 = input.nextFloat();

                while (num2 == 0)
                {
                    System.out.print("Introduce el segundo numero: ");
                    num2 = input.nextFloat();
                }

                System.out.println("Tu division es: " + (num1/num2)); 
                break;
            case ("5"):
                System.out.print("Introduce el numero: ");
                num1 = input.nextFloat();
                System.out.print("Introduce el divisor: ");
                num2 = input.nextFloat();

                System.out.println("Tu residuo es: " + (num1%num2));
                break;
            case(""):
                System.exit(0);
        }  
    }
}
