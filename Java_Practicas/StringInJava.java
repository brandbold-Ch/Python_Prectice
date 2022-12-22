public class StringInJava 
{   
    public static void main(String[] args)
    {
        // Conversiond de tipos de datos a Strings 
        //String str = "abc";

        char data[] = {'a','b','c'}; //Conversion de un array a String
        String str = new String(data);

        System.out.println(str);
        System.out.println(data.toString());
        

    }
}
