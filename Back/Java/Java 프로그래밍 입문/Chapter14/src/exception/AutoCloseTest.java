package exception;

public class AutoCloseTest {

	public static void main(String[] args) {

		//AutoCloseObj obj = new AutoCloseObj();
		//try(obj) {} 이것도 최근에는 지원 됨
		try (AutoCloseObj obj = new AutoCloseObj()){
			throw new Exception();
		}catch(Exception e) {
			System.out.println("exception");
		}
	}

}
