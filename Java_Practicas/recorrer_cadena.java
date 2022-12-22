public class recorrer_cadena {
    
    public static void main(String[] args)
    {

        String name = "Brandon";

        for (int i=name.length()-1;i>=0;i--)
        {
            System.out.println(name.charAt(i));
        }
    }
}
