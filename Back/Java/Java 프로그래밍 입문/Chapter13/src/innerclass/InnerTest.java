package innerclass;

// instance 내부 클래스 & 정적 내부 클래스

class OutClass{
	
	private int num = 10;
	private static int sNum = 20;
	private InClass inClass;
	
	public OutClass(){
		inClass = new InClass();
	}
	
	private class InClass{
		int inNum = 200;
		// static int sInNum = 100; 
		// static 변수/메소드는 instance의 생성과 상관 없이 사용 가능=> 여기서는 사용 불가
		
		void inTest() {
			System.out.println(num);
			System.out.println(sNum);
		}
		
	}
	
	public void usingInTest() {
		inClass.inTest();
	}
	
	static class InStaticClass{
		int iNum = 100;
		static int sInNum = 200;
		
		void inTest() {
//			num += 10; 사용 불가
			sNum += 10; // 정적변수 + 정적 내부 클래스라 사용 가능
			System.out.println(sNum);
			System.out.println(iNum);
			System.out.println(sInNum);
		}
		
		static void sTest() {
			System.out.println(sNum);
//			System.out.println(iNum); 사용 불가
			System.out.println(sInNum);
		}
	}
	
}

public class InnerTest {

	public static void main(String[] args) {

		/* OutClass outClass = new OutClass();
		outClass.usingInTest(); */
		
		OutClass.InStaticClass sInClass = new OutClass.InStaticClass();
		sInClass.inTest();
		
		OutClass.InStaticClass.sTest(); // 바로 호출 가능. 모두 정적 변수

	}

}
