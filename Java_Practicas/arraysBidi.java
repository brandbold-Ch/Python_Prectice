class arraysBidi
{
    public static void main(String[]  args)
    {
        byte array[][] = new byte[3][2];

        array[0][0] = 1; 
        array[1][0] = 2;
        array[2][0] = 3;

        array[0][1] = 4;
        array[1][1] = 5;
        array[2][1] = 6;

        // array[0][2] = 1;
        // array[1][2] = 7;
        // array[2][2] = 3;

        for (byte i=0;i<array.length;i++)
        {
            System.out.println();
            for (byte j=0;j<array.length;j++)
            {
                System.out.println(array[j][i]);
            }   
        }
    }
}