public class Cuenta { // modificador de acceso
    
    private String nombre; // solo accesible para metodos de clase

    // metodo setter
    public void establecerNombre(String nombre){
        this.nombre = nombre;
    }

    // metodo getter
    public String obtenerNombre(){
        return nombre;
    }
}