
import java.util.Scanner;

public class decimalAbin {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        StringBuilder binary = new StringBuilder();
        
        System.out.print("Introduce el decimal: ");
        String decimal = input.nextLine();

        int num = Byte.parseByte(decimal);

        for (byte i=0;i<Byte.parseByte(decimal);i++)
        {
            byte residuo = (byte) ((byte) num % 2);
            num /= 2;

            binary.insert(i,String.valueOf(residuo));
            if (num==2)
            {
                break;
            }
        }
        System.out.println(binary);
    }
}
