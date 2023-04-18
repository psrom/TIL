package inheritance;

public class OverridingTest {

	public static void main(String[] args) {

		/* Customer customerLee = new Customer(10010, "Lee");
		int price = customerLee.calcPrice(10000);
		System.out.println("지불 금액은 " + price + "원 이고, " + customerLee.showCustomerInfo());

		VIPCustomer customerKim = new VIPCustomer(10011, "Kim", 100);
//		customerKim.calcPrice(10000);
		price = customerKim.calcPrice(10000);
		System.out.println("지불 금액은 " + price + "원 이고, " + customerKim.showCustomerInfo());	}

} */
		
		Customer customerWho = new VIPCustomer(101010, "Who", 101);
		int price = customerWho.calcPrice(10000);
		System.out.println("지불 금액은 " + price + "원 이고, " + customerWho.showCustomerInfo());
		
		Customer customerGold = new GoldCustomer();
		customerGold.
	}
}