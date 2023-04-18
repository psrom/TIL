package classex;

public class ClassTest {

	public static void main(String[] args) throws ClassNotFoundException {

		Person person = new Person();
		
		Class pClass1 = person.getClass();

		// 1. getClass();
		// �̹� �ν��Ͻ��� �����Ǿ� �ִ� ��� Class Ŭ���� �ҷ��� �� ����
		// Object�� method��
		// static �ε�
		
		System.out.println(pClass1.getName());
		
		Class pClass2 = Person.class;
		// 2. .class
		// Class �� Ŭ������ ������
		// ������ �� �����̾�� ��
		// static �ε�
		System.out.println(pClass2.getName());
		
		Class pClass3 = Class.forName("classex.Person");
		System.out.println(pClass3.getName());
		// 3. Class.forName("���ڿ�");
		// ���ڿ� �̸��� ���� Ŭ������ ������ Load �ؿ�
		// ���� �ε�
		
		
	}

}
