package abstractex;

public abstract class Computer {
	
	public abstract void display(); //�޼��带 ���� ��(���� X)
	public abstract void typing(); //{}�� ������ ����O
	
	// public abstract int add(int x, int y);
	// public int add(int x, int y) {return x+y};
	
	public void turnOn() {
		System.out.println("������ �մϴ�.");
	}
	
	public void turnOff() {
		System.out.println("������ ���ϴ�.");
	}
}

// �߻� Ŭ������ ����� �ϱ� ���� �����.
// new(instance �� �� ����)