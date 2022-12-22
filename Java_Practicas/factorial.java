import javax.swing.JOptionPane;

public class factorial {

    public static void main(String[] args) {

        JOptionPane.showMessageDialog(null, "Deseas saber un factorial");

        int num,i;
        Long factorial = 1L;

        num = Integer.parseInt(JOptionPane.showInputDialog("Introduce un numero: ")); 

        for (i = num;i>0;i--)
        {
            factorial *= i;
        }
        JOptionPane.showInternalMessageDialog(null, "El resultado es:\n" + factorial);
    }
}