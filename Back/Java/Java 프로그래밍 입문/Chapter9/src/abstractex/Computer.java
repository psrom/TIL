package abstractex;

public abstract class Computer {
	
	public abstract void display(); //메서드를 선언만 함(구현 X)
	public abstract void typing(); //{}가 있으면 구현O
	
	// public abstract int add(int x, int y);
	// public int add(int x, int y) {return x+y};
	
	public void turnOn() {
		System.out.println("전원을 켭니다.");
	}
	
	public void turnOff() {
		System.out.println("전원을 끕니다.");
	}
}

// 추상 클래스는 상속을 하기 위해 만든다.
// new(instance 할 수 없음)