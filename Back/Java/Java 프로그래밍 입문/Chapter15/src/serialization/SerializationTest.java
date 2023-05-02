package serialization;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Person implements Serializable{

	private static final long serialVersionUID = -1522576323440032360L;
	String name;
	String title;
	
	public Person() {}
	public Person(String name, String title) {
		this.name = name;
		this.title = title;
	}
	
	public String toString() {
		return name + "," + title;
	}
}


public class SerializationTest {

	public static void main(String[] args) throws ClassNotFoundException {

		Person personLee = new Person("Lee", "Manager");
		try( FileInputStream fis = new FileInputStream("serial.dat");
				ObjectInputStream ois = new ObjectInputStream(fis)){
			
			Object obj = ois.readObject();
			if( obj instanceof Person) {
				Person p = (Person)obj;
			}
		}catch(IOException e) {
			System.out.println(e);
		}
	}

}

// Externalizable