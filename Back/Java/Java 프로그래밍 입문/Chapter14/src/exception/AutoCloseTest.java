package exception;

public class AutoCloseTest {

	public static void main(String[] args) {

		//AutoCloseObj obj = new AutoCloseObj();
		//try(obj) {} �̰͵� �ֱٿ��� ���� ��
		try (AutoCloseObj obj = new AutoCloseObj()){
			throw new Exception();
		}catch(Exception e) {
			System.out.println("exception");
		}
	}

}
