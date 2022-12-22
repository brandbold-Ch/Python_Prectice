public class cadenas_2 {

    public static void main(String args[]) {

        // String str = "abc";

        char data[] = { 'a', 'b', 'c' };
        String str = new String(data);

        String word = "Hola soy brandon y estoy estudiando Java";

        System.out.println(word.substring(5, 16) + " huele a mierda");
        System.out.println(word.codePointAt(3));

        System.out.println(str);

        String name = "Jared";
        String name2 = "jared";

        System.out.println(name.equals(name2));
        System.out.println(name.equalsIgnoreCase(name2));

    }
}
