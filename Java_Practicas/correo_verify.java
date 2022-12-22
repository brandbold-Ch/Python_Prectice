import javax.swing.JOptionPane;

public class correo_verify {

    public static void main(String[] args) {

        /*          Partes de un correo electronico
         *
         *  jaredbrandon970@gmail.com
         *  nombre de usuario: organizacion: tipo.
         *                           Dominio
         */

        boolean arroba=false, punto=false;

        JOptionPane.showMessageDialog(null, "Programa para evaluar tu correo");

        String email = JOptionPane.showInputDialog("Correo:");
        
        if (email.length()==0)
        {
            System.out.println("No escribiste nada");
            System.exit(0);
        }
        byte arroba_enum=0;

        for (int i=0;i<=email.length()-1;i++)
        {
            if (email.charAt(i)== ' ')
            {
                System.out.println("No pueden tener espacios en tu correo");
                System.exit(0);
            }
            else if ((i>0)&&(email.charAt(i)=='@'))
            {   
                arroba_enum += 1;
                arroba = true;

                if (arroba_enum>1)
                {
                    arroba = false;
                }
            }
            else if ((i>email.indexOf('@'))&&(email.charAt(i)=='.'))
            {
                punto = true;
            }
        }
        if (arroba && punto)
        {
            System.out.println("Correo Correcto para: " + email);
        }else{
            System.out.println("Correo Incorrecto para: " + email);
        }
        System.out.println(arroba_enum);
    }
}