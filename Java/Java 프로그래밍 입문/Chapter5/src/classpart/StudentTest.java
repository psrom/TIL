package classpart;

public class StudentTest {

	public static void main(String[] args) {
		
		Student studentLee = new Student(100, "�̼���");
		/* studentLee.studentName = "�̼���";
		studentLee.studentID = 100; */
		studentLee.address = "����� �������� ���ǵ���";
		
		Student studentKim = new Student();
		studentKim.studentName = "������";
		studentKim.studentID = 101;
		studentKim.address = "�̱� ��ȣ��";
		
		studentLee.showStudentInfor();
		studentKim.showStudentInfor();
		
		System.out.println(studentLee);
		System.out.println(studentKim);
		
	}

}
