import java.util.Scanner;

public class IVA {
    
    public static void main(String[] args)
    {
        final float iva = 0.21f;

        float productos, precio_final=0, precios=0; 
        byte i=1;

        Scanner input = new Scanner(System.in);

        System.out.print("Cuantos productos comprastes: ");
        productos = input.nextFloat();

        while (i <= productos)
        {
            System.out.print("Precio del producto " + i + " $");
            precios = input.nextFloat();

            precio_final += precios;

            System.out.println("Total " + precio_final);

            i++;
        }
        precio_final += precio_final*iva;
        System.out.println("Vas a pagar en total: $" + precio_final + " pesos");
    }
}