package abstractex;

public class ComputerTest {

	public static void main(String[] args) {

//		Computer c1 = new Computer(); abstract라서 instance 생성 안 됨
		Computer c2 = new DeskTop();
//		Computer c3 = new NoteBook(); abstract라서 instance 생성 안 됨
		Computer c4 = new MyNoteBook();
		
//		NoteBook c5 = new MyNoteBook(); 가능함
		c2.display();
		c4.display();

	}
}
