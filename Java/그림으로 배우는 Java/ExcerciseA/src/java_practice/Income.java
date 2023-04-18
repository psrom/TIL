package java_practice;

public class Income {

	public static void main(String[] args) {
		double[] money = { 8.62, 10.23, 12.48, 7.82, 9.54 };
	
		double sum = 0;
	    for (int i=0; i<money.length; i++) {
	      sum += money[i];
	    }
	    System.out.printf("$ %.2f", sum);
	}

}
