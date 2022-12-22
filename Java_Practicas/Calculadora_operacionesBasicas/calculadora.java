package Calculadora_operacionesBasicas;
import java.util.InputMismatchException;
import java.util.Scanner;

public class calculadora {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.println("\tCalculadora Basica\n1._Suma\n2._Resta\n3._Multiplicacion\n4._Division\n5._Exponenciacion");
        System.out.print("\nElige una opcion: ");
        try {
            byte opcion = input.nextByte();

            if (opcion>5){
                System.exit(0);
            }
            
            System.out.print("\nvalor1: ");
            float num1 = input.nextFloat();
            System.out.print("\nvalor2: ");
            float num2 = input.nextFloat();
    
            operaciones obj = new operaciones();
            obj.obtener(num1, num2);
            
            if(opcion == 1)
            {
                System.out.println(">> " + obj.suma());
    
            }else if (opcion == 2) {
    
                System.out.println(">> " + obj.resta());
    
            }else if (opcion == 3){
    
                System.out.println(">> " + obj.multiplicacion());
    
            }else if(opcion == 4){
    
                System.out.println(">> " + obj.division());
    
            }else if (opcion == 5){
    
                System.out.println(">> " + obj.exponenciacion());
    
            }else{
                System.exit(0);
            }
        } catch (InputMismatchException e) {
            System.out.println("Not found");
        }
    }
}