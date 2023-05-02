package exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class ExceptionTest2 {

	public static void main(String[] args) throws IOException {

		
		try (FileInputStream fis = new FileInputStream("a.txt")){
		
		}catch (IOException e) {
			System.out.println(e);
		}
		System.out.println("end");
		
	}
}


