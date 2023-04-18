package array;

public class BookArray {

	public static void main(String[] args) {
		Book[] library = new Book[5];
		
		library[0] = new Book("태백산맥", "조정래");
		library[1] = new Book("낙원의 이론", "정선우");
		library[2] = new Book("안나 카레니나", "레프 톨스토이");
		library[3] = new Book("태백산맥4", "조정래");
		library[4] = new Book("태백산맥5", "조정래");
		
		for(int i = 0; i<library.length; i++) {
			System.out.println(library[i]);
		}	
		for(int i = 0; i<library.length; i++) {
			library[i].showBookInfo();	
		}
	}		
}
