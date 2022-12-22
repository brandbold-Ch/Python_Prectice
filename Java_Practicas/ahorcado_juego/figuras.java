package ahorcado_juego;

public class figuras {
    public static void base() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void cabeza() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void tronco() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("  |   |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void brazoIzquierdo() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("/ |   |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void brazoDerecho() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("/ | \\ |");
        System.out.println("      |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void piernaIzquierda() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("/ | \\ |");
        System.out.println(" /    |");
        System.out.println("      |");
        System.out.println("=======");
    }
    public static void piernaDerecha() {
        System.out.println("  +---+");
        System.out.println("  |   |");
        System.out.println("  O   |");
        System.out.println("/ | \\ |");
        System.out.println(" / \\  |");
        System.out.println("      |");
        System.out.println("=======");
    }
}