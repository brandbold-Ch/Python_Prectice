package Calculadora_operacionesBasicas;

public class operaciones 
{
    private float num1;
    private float num2;

    public void obtener(float num1, float num2)
    {
        this.num1 = num1;
        this.num2 = num2;
    }
    public float suma()
    {   
        return num1 + num2;
    }
    public float resta()
    {
        return num1 - num2;
    }
    public float multiplicacion()
    { 
        return num1 * num2;
    }
    public float division()
    {
        return num1 / num2;
    }
    public float exponenciacion()
    {
        return (float) Math.pow(num1, num2);
    } 
}