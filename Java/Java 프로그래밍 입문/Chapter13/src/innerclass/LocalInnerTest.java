package innerclass;
// 익명내부 클래스
class Outer{
	
	int outNum = 100;
	static int sNum = 200;
	
	Runnable runnable = new Runnable() {
		
		@Override
		public void run() {
			System.out.println("runnable");
		}
	};
	
	
	
	// 지역 내부 class
	public Runnable getRunnable(int i){
		
		int localNum = 100;
		
		return new Runnable(){

			@Override
			public void run() {
				
//				localNum += 100; 오류!
//				i += 200; 오류!
				
				System.out.println(outNum);
				System.out.println(sNum);
				System.out.println(localNum);
			}
		};
		
	}
	
}

public class LocalInnerTest {

	public static void main(String[] args) {
		
		Outer outer = new Outer();
		Runnable runnable = outer.getRunnable(20);
		runnable.run();
		
		outer.runnable.run();

	}

}
