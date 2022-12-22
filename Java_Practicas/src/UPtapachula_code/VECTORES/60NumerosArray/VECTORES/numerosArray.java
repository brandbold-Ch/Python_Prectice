package UPtapachula_code.VECTORES;

public class numerosArray 
{
    public static void main(String[] args)
    {
        byte array[] = new byte[60];
        recorre(array);
        
    }
    public static void recorre(byte array[])
    {
        byte contposit, contneg, contcero;
        contposit = 0;
        contneg = 0;
        contcero = 0;

        for (byte i = 0; i < array.length; i++) 
        {
            array[i] = (byte) Math.round(Math.random()*101-50-124);

            System.out.println(array[i]);
            if(array[i]<0)
            {
                contneg++;
            }
            else if (array[i]==0)
            {
                contcero++;
            }
            else{
                contposit++;
            }
        }
        System.out.println("Hay "+contposit+" positivos, "+contneg+" negativos y "+contcero+" ceros.");
    }
}