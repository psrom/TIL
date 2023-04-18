package java_practice;
import java.util.Scanner;

public class Multiple {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		
	    System.out.printf("곱하기: %d x %d = %d\n", a, b, a*b );
	    System.out.printf("나누기: %d / %d = %d", a, b, a/b );
	}

}
