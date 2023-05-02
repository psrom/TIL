package exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class ExceptionTest {

	public static void main(String[] args) throws IOException {

		FileInputStream fis = null;
		
		try {
			fis = new FileInputStream("a.txt");
		}catch (FileNotFoundException e) {
			
			e.printStackTrace();
		} finally {
			try{fis.close();
			} catch (IOException e) {
			e.printStackTrace();
			}
			System.out.println("finally");
		}
		System.out.println("end");
	}
}
