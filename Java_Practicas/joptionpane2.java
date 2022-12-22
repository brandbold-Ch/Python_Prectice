import javax.swing.JOptionPane;

public class joptionpane2 {
    public static void main(String[] args) {
        
        JOptionPane.showMessageDialog(null, "Hola Cachorro" );

        String num1 = JOptionPane.showInputDialog("Introduce un numero: ");

        Double num1_m = Double.parseDouble(num1);

        int raiz = (int) Math.sqrt(num1_m);

        JOptionPane.showMessageDialog(null,"La raiz de " + num1 + " es " + raiz);

    }
}
