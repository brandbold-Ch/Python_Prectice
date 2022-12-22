public class practicas_scape
{
	public static void main(String args[])
	{
		/*
			Tabla de conversiones
			
			%b = booleano
			%h = hashcode
			%s = string
			%c = caracter unicode
			%d = entero decimal
			%o = entero octal
			%x = entero hexadecimal
			%f = real decimal
			%e = real notacion cientifica o decimal
			%g = real notacion cientifica o decimal
			%a = real hexadecimal con mantisa y exponente 
			%t = fecha u hora	
		*/
		byte hour=2, edad=18, minuts=10;
		String name ="Brandon", patron="%s va a la universidad a las %d:%d h";
		String resultado=String.format(patron,name,hour,minuts), matricula="223031";

		System.out.printf("Hola jared");
	}
}