package POO;

public class coche_uso 
{
    public static void main(String[] args) {
        
        Coche auto = new Coche();
        auto.retorna("Dakota");
        System.out.println(auto.dato());

        Coche auto2 = new Coche();
        System.out.println(auto2.dato());
    }
}