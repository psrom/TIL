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
		System.out.println("지하철 " + SubwayLine + "호선의 승객은 " + passengerCount + "명이고, 수입은 "
				+ money + "원 입니다."); 
	}
}
