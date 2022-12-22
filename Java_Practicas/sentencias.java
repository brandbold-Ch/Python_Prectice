import java.util.Scanner;

public class sentencias {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print(">>> ");

        String word = input.next();

        if (word.equals("a") || word.equals("A")) {

            System.out.println("Enhorabuena");

        }

    }
}
