import java.util.Scanner;

public class scanner2 {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		// Ecuación de la Recta

		float x1, x2, y1, y2, m, p, ángulo, d, option, Y, Y2;

		System.out.print("\tEcuaciones\n" +
				"\n1._ Punto Pendiente.\n" +
				"2._ Punto Medio.\n" +
				"2._ Distancia entre dos puntos.\n" +
				"3._ Ángulo de inclinacion.\n" +
				"\nElige una opción: ");

		option = input.nextInt();

		if (option == 1) {

			System.out.print("\nX1: ");
			x1 = input.nextFloat();
			System.out.print("Y1: ");
			y1 = input.nextFloat();
			System.out.print("X2: ");
			x2 = input.nextFloat();
			System.out.print("Y2: ");
			y2 = input.nextFloat();

			m = (y2 - y1) / (x2 - x1);
			Y = (-1 * y1);
			Y2 = m * (-1 * x1);

			if (Y < 0) {

				Y = Math.abs(Y) + Y2;
				System.out.println("y = " + m + "x " + Y);

			} else {

				Y = (-1 * Y) + Y2;
				System.out.println("y = " + m + "x " + Y);

			}
		}

		if (option == 2) {

			System.out.print("\nX1: ");
			x1 = input.nextInt();
			System.out.print("Y1: ");
			y1 = input.nextInt();
			System.out.print("X2: ");
			x2 = input.nextInt();
			System.out.print("Y1: ");
			y2 = input.nextInt();

			x1 = (x1 + x2) / 2;
			y1 = (y1 + y2) / 2;

			System.out.println("Pendiente = " + "(" + x1 + "," + y1 + ")");
		}

		/*
		 * if (option == 3) {
		 * 
		 * System.out.print("\nX1: ");
		 * x1 = input.nextDouble();
		 * System.out.print("Y1: ");
		 * y1 = input.nextDouble();
		 * System.out.print("X2: ");
		 * x2 = input.nextInt();
		 * System.out.print("Y1: ");
		 * y2 = input.nextInt();
		 * 
		 * d = Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
		 * 
		 * }
		 */

	}
}