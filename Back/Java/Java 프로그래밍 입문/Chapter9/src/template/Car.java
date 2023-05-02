package template;

public abstract class Car {
	
	public abstract void drive();
	public abstract void stop();
	
	public abstract void wiper();
	public void washCar() {}
	
	public void startCar() {
		System.out.println("시동을 켭니다.");
	}
	
	public void turnOff() {
		System.out.println("시동을 끕니다.");
	}
	public final void run() {
		startCar();
		drive();
		wiper();
		stop();
		washCar();
		turnOff();
	} //Template Method: 차가 달리는 시나리오(이것은 변함이 없음)
}
