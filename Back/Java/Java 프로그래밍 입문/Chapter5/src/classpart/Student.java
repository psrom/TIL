package classpart;

public class Student {

	int studentID;
	String studentName;
	int grade;
	String address;
	
	public Student() {}
	
	// public Student() {} 자바 컨파일러가 디폴트 생성자 자동으로 넣어줌
	public Student(int id, String name) {
		studentID = id;
		studentName = name;		
	}
	
	public void showStudentInfor() {
		System.out.println(studentName + ", " + address);
	}
	
	/* public static void main(String[] args) {
		
		Student studentLee = new Student();
		studentLee.studentName = "이순신";
		studentLee.address = "서울시 서초구 서초동";
		
		studentLee.showStudentInfor();
	} */
	
	public	String getStudentName() {
		return studentName;
	}
	
	public void setStudentName(String name) {
		studentName = name;
	}
}
