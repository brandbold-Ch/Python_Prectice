public class array_random {
    
    public static void main(String[] args)
    {
        int numbers[] = new int[130];

        for (int i=0;i<=numbers.length-1;i++)
        {
            numbers[i] = (byte)Math.round(Math.random()*100);
        }
        for (int numeros:numbers)
        {
            System.out.println(numeros);
        }
    }
}
