package abstractex;

public class ComputerTest {

	public static void main(String[] args) {

//		Computer c1 = new Computer(); abstract�� instance ���� �� ��
		Computer c2 = new DeskTop();
//		Computer c3 = new NoteBook(); abstract�� instance ���� �� ��
		Computer c4 = new MyNoteBook();
		
//		NoteBook c5 = new MyNoteBook(); ������
		c2.display();
		c4.display();

	}
}
