package classex;

public class ClassTest {

	public static void main(String[] args) throws ClassNotFoundException {

		Person person = new Person();
		
		Class pClass1 = person.getClass();

		// 1. getClass();
		// 이미 인스턴스가 생성되어 있는 경우 Class 클래스 불러올 수 있음
		// Object의 method임
		// static 로딩
		
		System.out.println(pClass1.getName());
		
		Class pClass2 = Person.class;
		// 2. .class
		// Class 의 클래스를 가져옴
		// 컴파일 된 상태이어야 함
		// static 로딩
		System.out.println(pClass2.getName());
		
		Class pClass3 = Class.forName("classex.Person");
		System.out.println(pClass3.getName());
		// 3. Class.forName("문자열");
		// 문자열 이름을 가진 클래스가 있으면 Load 해옴
		// 동적 로딩
		
		
	}

}
