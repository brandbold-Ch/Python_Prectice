public class array_each {
    
    public static void main(String[] args)
    {
        String matriz[] = new String[8];

        matriz[0] = "Jared";
        matriz[1] = "Jocker";
        matriz[2] = "Woshingo";
        matriz[3] = "Sergio AD";
        matriz[4] = "Peper sheed";
        matriz[5] = "Breakman";
        matriz[6] = "Loco";
        matriz[7] = "Staryukiii";

        /*for (int i=0; i<=matriz.length-1; i++)
        {
            System.out.println("Cosa " + (i+1) + " " + matriz[i]);
        }
        */

        byte i = 1;
        for (String elemento:matriz)
        {
            System.out.println("Cosa " + (i) + " " + elemento);
            i++;
        }
    }
}
