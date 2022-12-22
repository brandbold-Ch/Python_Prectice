import java.util.Scanner;

public class binario_decimal 
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);

		System.out.print("introduce tus bits>> ");
		String binary = input.nextLine();

		int p=0, dec=0;
		for (int i=(binary.length()-1);i>=0;i--)
		{
			System.out.println(binary.charAt(i) + ", " + ((int)Math.pow(2,p)));

			if (binary.charAt(i)== '1')
			{
				dec += ((int)Math.pow(2,p));
			}
			p++;
		}
		System.out.println(dec);
	}
}