package java_practice;
import java.io.InputStream;
import java.util.Scanner;

public class Exchange {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		
		int euro = scanner.nextInt();
		int dollar = scanner.nextInt();
		
	    double euroToKwnRate = 1281.62664;
	    double dollarToKwnRate = 1091.70306;
	    
	    double kwn = euro*euroToKwnRate + dollar*dollarToKwnRate;
	    
	    System.out.printf("환전 결과: %.0f원", kwn);
	}

}
