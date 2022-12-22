import javax.swing.JOptionPane;

public class joptionpane {

    public static void main(String[] args) {

        String nombre = JOptionPane.showInputDialog("Introduce tu nombre: ");
        String edad = JOptionPane.showInputDialog("Introduce tu edad: ");

        int edad2 = Integer.parseInt(edad);
        edad2++;
        System.out.println(nombre + " tendra " + edad2 + " anos el siguiente ano");

    }
}
