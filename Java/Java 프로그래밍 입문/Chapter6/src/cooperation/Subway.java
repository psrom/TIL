package cooperation;

public class Subway {
	
	int SubwayLine;
	int passengerCount;
	int money;
	
	public Subway(int SubwayLine) {
		this.SubwayLine = SubwayLine;
	}
	
	public void take(int money) {
		passengerCount++;
		this.money += money;
	}
	
	public void showInfo() {
		System.out.println("����ö " + SubwayLine + "ȣ���� �°��� " + passengerCount + "���̰�, ������ "
				+ money + "�� �Դϴ�."); 
	}
}
