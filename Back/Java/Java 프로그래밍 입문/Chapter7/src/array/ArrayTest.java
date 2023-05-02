package array;

public class ArrayTest {

	public static void main(String[] args) {

		int[] numbers = new int[3];
		
		numbers[0] = 1;
		numbers[1] = 2;
		numbers[2] = 3;
		
		for(int i = 0; i<numbers.length; i++) {
			System.out.println(numbers[i]);
		}
		

//		int[] numbers = new int[] {1, 2, 3};	
//		int[] numbers = {1, 2, 3}; 위와 같은 의미
		
		int[] studentsIDs = new int[5];
		
		for(int i = 0; i<studentsIDs.length;i++) {
			System.out.println(studentsIDs[i]);
		}//값 지정 안 해주면 0으로 초기화 됨
	
	}

}
