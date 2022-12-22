import javax.swing.JOptionPane;

public class acceso {
    
    public static void main(String[] args){

        String pass= "", clave = "2n3055psk";

        while (clave.equals(pass)==false){

            pass = JOptionPane.showInputDialog("Introduce el password:");

            if (clave.equals(pass)==false){

                JOptionPane.showMessageDialog(null, "Password incorrecto");
            }
        }

        JOptionPane.showMessageDialog(null, "Password Correcto. Acceso Permitido");
    }
}
