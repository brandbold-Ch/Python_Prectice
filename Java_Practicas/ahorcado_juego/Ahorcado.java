package ahorcado_juego;
import java.util.Scanner;

public class Ahorcado
{
	public static void main(String[] args)
	{
		char lista[] = { 'a', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o', 's' };
		char adivina[] = new char[lista.length];
		adivina[0] = '_';
		adivina[1] = '_';
		adivina[2] = 'g';
		adivina[3] = '_';
		adivina[4] = 'r';
		adivina[5] = '_';
		adivina[6] = 't';
		adivina[7] = '_';
		adivina[8] = '_';
		adivina[9] = 's';
		proceso(lista, adivina);
	}
	public static void proceso(char lista[], char adivina[])
	{
		byte fallos = 0;
		boolean ciclo = true;
		Scanner input = new Scanner(System.in);

		while (ciclo) 
		{
			String newlist = new String(lista);
			String newadivina = new String(adivina);
			System.out.println(newadivina + "\n");

			if (newlist.equals(newadivina)) 
			{
				System.out.print("Felicidades haz ganado");
				ciclo = false;
				break;
			} 
			System.out.print("Adivina la letra: ");
			String word = input.nextLine().toLowerCase();
			
			if ((newlist.contains(word)) && (newadivina.contains(word) == false)) 
			{
				for (byte j = 0; j < lista.length; j++) 
				{
					if (newlist.charAt(j) == word.charAt(0)) 
					{
						adivina[j] = word.charAt(0);
					}
				}
			} else {
				fallos += 1;
				muertes(fallos);
			}
		}
	}
	public static void muertes(int fallos)
	{
		if (fallos == 1) {
			figuras.base();
		} else if (fallos == 2) {
			figuras.cabeza();
		} else if (fallos == 3) {
			figuras.tronco();
		} else if (fallos == 4) {
			figuras.brazoIzquierdo();
		} else if (fallos == 5) {
			figuras.brazoDerecho();
		} else if (fallos == 6) {
			figuras.piernaIzquierda();
		} else if (fallos == 7) {
			figuras.piernaDerecha();
			System.out.println("AHORCADO");
			System.exit(0);
		}
	}
}