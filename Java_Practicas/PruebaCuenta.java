public class PruebaCuenta {
    public static void main(String[] args){

        Cuenta miCuenta = new Cuenta(); //Instanciar clase
        miCuenta.establecerNombre("Brandon");
        System.out.print(miCuenta.obtenerNombre());
    }
}