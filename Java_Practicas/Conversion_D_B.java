import javax.swing.JOptionPane;

public class Conversion_D_B {

    public static void main(String[] args)
    {

        int i=0;
        byte array_bin[] = new byte[127];
    
        JOptionPane.showMessageDialog(null,"Conversion de Decimal a Binario");

        String decimal = JOptionPane.showInputDialog("introduce el numero: ");

        int num = Integer.parseInt(decimal);
    
        while (i<=127)
        {
            array_bin[i] = (byte)(num%2);
            System.out.println(array_bin[i]);
            num /= 2;

            if ((num==1) || (num==0))
            {
                array_bin[i] = (byte)(num%2);
                break;
            }
            i++;
        }
        for (int n=0;n<=i;n++)
        {
            System.out.print(n);
        }
    }
}