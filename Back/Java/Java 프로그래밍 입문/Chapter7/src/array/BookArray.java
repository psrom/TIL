package array;

public class BookArray {

	public static void main(String[] args) {
		Book[] library = new Book[5];
		
		library[0] = new Book("�¹���", "������");
		library[1] = new Book("������ �̷�", "������");
		library[2] = new Book("�ȳ� ī���ϳ�", "���� �罺����");
		library[3] = new Book("�¹���4", "������");
		library[4] = new Book("�¹���5", "������");
		
		for(int i = 0; i<library.length; i++) {
			System.out.println(library[i]);
		}	
		for(int i = 0; i<library.length; i++) {
			library[i].showBookInfo();	
		}
	}		
}
