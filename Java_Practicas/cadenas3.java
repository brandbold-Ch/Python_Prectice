public class cadenas3 {

    public static void main(String[] args) {

        String name = "brandon jared molina vazquez";
        String name2 = "Android";

        System.out.println(name.charAt(6));
        System.out.println(name.codePointAt(6));
        System.out.println(name.codePointBefore(6));
        System.out.println(name.compareTo(name2));
        System.out.println(name.compareToIgnoreCase(name2));
        System.out.println(name.concat(name2));
        System.out.println(name.contains("w"));

    }

}
