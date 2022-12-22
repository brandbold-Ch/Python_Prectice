public class Teorema_de_Pitagoras {
    public static void main(String[] args) {

        final Double pi = Math.PI;

        Double a, b, c, res;
        Double area, perimetro, s;

        /*
         * Encontrar lados
         * 
         * a = hipotenusa
         * b = cateto 1
         * c = cateto 2
         */

        a = 131.0;
        b = 63.0;
        c = 0.0;

        if (a != 0) {
            System.out.println("Nada que hacer");
        } else {
            res = Math.sqrt(Math.pow(b, 2) + Math.pow(c, 2));
            System.out.println("A mide: " + res);
        }

        if (b != 0) {
            System.out.println("Nada que hacer");
        } else {
            res = Math.sqrt(Math.pow(a, 2) - Math.pow(c, 2));
            System.out.println("B mide: " + res);
        }

        if (c != 0) {
            System.out.println("Nada que hacer");
            // Area y perimetro de triangulos rectangulos
            s = (a + b + c) / 2;
            area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            perimetro = a + b + c;
            System.out.println("Area: " + area + " Perimetro: " + perimetro);
        } else {
            res = Math.sqrt(Math.pow(a, 2) - Math.pow(b, 2));
            System.out.println("C mide: " + res);
        }

    }
}
