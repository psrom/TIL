// RunTimeException은 컴파일러가 못잡는 경우가 다수여서 직접 걸어줘야 함

package exception;

public class ArrayExceptionTest {

	public static void main(String[] args) {
		
		int[] arr = {1,2,3,4,5};
		try {
		for(int i=0; i<=5; i++) {
			System.out.println(arr[i]);
			}
		}catch(ArrayIndexOutOfBoundsException e) {
			System.out.println(e);
			return;
		}finally { // try가 수행되면 finally는 무조건 수행 됨
			System.out.println("finally");
		}
		System.out.println("end");
	}
}
