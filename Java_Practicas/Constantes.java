public class Constantes {
    public static void main(String[] args) {

        final float gravedad = 9.81f;
        final Double ln = 2.718281828459;
        final Double pi = 3.141592653589793238462643383;

        float num1, num2, div;

        num1 = 20;
        num2 = 42;

        div = num1 / num2;

        boolean question = gravedad != ln;
        boolean what = num1 == num2;

        // volumen de una esferajl
        Double ecuacion, r;
        r = 5.0;
        ecuacion = 4 / 3 * pi * Math.pow(r, 3);

        System.out.println("El volumen de la esfera es: " + Math.round(ecuacion) + " u^3");
        System.out.println(Math.PI);

        Double num3;
        num3 = 10.85;

        // raiz = Math.sqrt(num3);
        int raiz = (int) Math.round(num3);
        System.out.println(raiz);

    }
}
