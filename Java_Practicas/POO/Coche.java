package POO;

public class Coche 
{
    private int ruedas, puertas, cilindros;
    private String color, marca, modelo;

    public Coche()
    {
        ruedas = 4; 
        puertas = 4;
        cilindros = 6;
        color = "Gris";
        marca = "Honda";
        modelo = "Odyzzey";
    }
    
    public void retorna(String modelo) 
    {
        this.modelo = modelo;
    }

    public String dato()
    {
        return modelo;
    }
}