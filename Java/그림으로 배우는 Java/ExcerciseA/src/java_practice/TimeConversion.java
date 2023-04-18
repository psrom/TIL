package java_practice;

public class TimeConversion {

	public static void main(String[] args) {

		int totalSec = 7582;
	    
	    int hour = totalSec / (60 * 60);
	    int min = totalSec / 60 % 60;
	    int sec = totalSec % 60;
	    
	    System.out.printf("%d시간 %d분 %d초", hour, min, sec);

	}

}
