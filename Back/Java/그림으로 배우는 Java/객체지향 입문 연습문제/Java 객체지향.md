# 그림으로 배우는 JAVA(객체지향 입문)

YouTube: https://www.youtube.com/playlist?list=PLyebPLlVYXCiKweTN4a-xePbbY1Ta6Yu9

# 01 OOP

- Object Oriented Programming: 객체를 조합하여 만드는 프로그래밍

## 1. 장점

1. 유지보수 관리 용이
2. 재사용성
3. 확장성

## 2. 클래스와 객체

`인스턴스화` **Class** (설계도) ⇒ **Object** (`인스턴스`)

## 3. 클래스 만들기

- **필드와 메소드**
    - `fields`(상태), `methods`(동작)
- 설계
    - class name(고양이)
    - fields(이름, 나이, 체중)
    - methods(할퀴기(), 야옹(), purring())
- 코드 구현
    1. 클래스를 만든다.
    2.  field를 작성한다.
    3. method를 정의한다.

---

# 02 클래스 구현 및 객체 만들기

## 객체(인스턴스) 생성

```java
Cat c1 = new Cat();
Cat c2 = new Cat();
```

## 필드 값 변경

```java
c.name = "샴";
c.weight = 3.5;
```

## 예제) 고양이 클래스

```java
/* CatTest 클래스 */
public class CatTest {
  public static void main(String[] args) {
    // Cat 객체 생성
    Cat c = new Cat();
    
    c.name = "네로";
    c.breeds = "페르시안";
    c.age = 3;
		
		// 인스턴스 메소드 호출
		c.claw();
		c.meow();
    
    System.out.printf("이름: %s\n", c.name);
    System.out.printf("품종: %s\n", c.breeds);
    System.out.printf("나이: %s\n", c.age);
  }
}

/* Cat 클래스 */
class Cat {
  String name;   // 이름
  String breeds; // 품종
  int age;       // 나이

  void claw() {
    System.out.println("할퀴기!!");
  }
  
  void meow() {
    System.out.println("야옹~");
  }
}

/*===========
할퀴기!!
야옹~
이름: 네로
품종: 페르시안
나이: 3
===========*/
```

## 스코프

- 변수의 활동 영역
    - 변수의 이름이 같은 경우 주의
- `클래스` 스코프: 필드
- `메소드` 스코프: 파라미터, 지역변수

# 03 생성자

```java
Cat cat = new Cat(); // Cat()이 생성자
```

## 생성자의 역할

1. 객체 생성
2. 필드 초기화(초기값 설정)

## 생성자의 호출과 정의

```java
public class CatTest {
  public static void main(String[] args) {
    // Cat 객체 생성
    Cat c = new Cat("네로", 3.5, 5);
		/* new Cat(전달값); ==> 생성자 호출 */
  }
}

class Cat{
	String name;
	double weight;
	int age;
	/* 생성자 정의 */
	Cat (String s, double d, int i) {
		name = s;
		weight = d;
		age = i;
	}
}
```

## String.format() 메소드

- 형식 문자열을 만들어주는 메소드

```java
String name = "네오";
int weight = 4.5;
String str = String.format("고양이 {%s, %dkg}", name, weight);
System.out.println(str)
// >> "고양이 {네오, 4.5kg}"
```

### printf()와의 차이

- String.format()은 출력을 하지 않음. 문자열 생성만 함

## 예제1 ) 생성자 정의

```java
public class HeroTest {
  public static void main(String[] args) {
    // 객체 생성
    Hero ironMan = new Hero("아이언맨", 80);
    Hero thanos = new Hero("타노스", 160);
    Hero thor = new Hero("토르", 150);
    Hero groot = new Hero("그루트", 40);

    // 모든 객체 정보를 출력
    System.out.println(ironMan.toStr());
    System.out.println(thanos.toStr());
    System.out.println(thor.toStr());
    System.out.println(groot.toStr());
  }
}

// Hero 클래스
class Hero {
  String name;
  int hp;
  
  **// 생성자
  Hero(String s, int i) {
    name = s;
    hp = i;**
  }

  String toStr() {
    return String.format("Hero { name: %s, hp: %d }", name, hp);
  }
}
```

## 예제2 ) 디폴트 생성자

```java
public class DrinkTest {
  public static void main(String[] args) {
    // 디폴트 생성자로 객체 만들기
    Drink d1 = new Drink();
    d1.name = "포카리";
    d1.price = 1000;
    
    // 다른 생성자로 객체 만들기
    Drink d2 = new Drink("박카스", 800);
    
    // 모든 객체 출력
    System.out.println(d1.toStr());
    System.out.println(d2.toStr());
  }
}

// 드링크 객체
class Drink {
  // 필드
  String name;
  int price;
  
  **public Drink() { //디폴트 생성자
    // 작성 안 하면 현재 코드는 작동이 안 됨
  }**
  
  // 생성자
  Drink(String n, int p) {
    name = n;
    price = p;
  }
  
  // 메소드
  String toStr() {
    return String.format("Drink { name: %s, price: %d }", name, price);
  }
}
```

## 객체 배열 만들기

```java
Book b1= new Book("물위의 우리");
Book b2 = new Book("창백한 말");
Book b3 = new Book("트럼프");
Book[] comics = { b1, b2, b3 };
```

# 04 레퍼런스와 static

## 0. 변수의 타입

- 레퍼런스형(references type) ⇒ 객체 연결을 위한 타입
    - 클래스 타입
    - 사용자 정의형 타입
- 기본형

## 1-1 . 레퍼런스 변수

- 객체를 가리키는 변수

## 1-2. 기본 변수

- 값을 직접 저장

```java
/* 레퍼런스 변수 */
// 객체 생성 후, 그 객체의 주소를 marine1 변수에 저장. 그 객체를 Marine 타입 으로 해석.
Marine marine1 = new Marine("레이너", 80);
// marine1 주소의 객체이 접근하여, stimpack() 동작을 실행
marine1.stimpack();

/* 기본형 */
int score = 88;
```

## 2. static

- `공유`의 개념이 담긴 키워드

- **클래스 변수** `static fields`
    - 공유를 위한 객체 외부 변수
    

- **인스턴스 변수** `non-static fields`
    - 객체 내부에 존재하는 변수

- **클래스 메소드** `static methods`
    - “클래스”가 동작시키는 메소드
    - `ex) Math.random();`

- **인스턴스 메소드** `non-static methods`
    - “주 객체”가 동작하는 메소드
    - ex)  `Hero hero1 = new Hero();`
           `hero1.punch();`
    

### 예제 ) 원의 넓이 구하기

```java
public class CircleTest {
  public static void main(String[] args) {
    // 객체 생성
    Circle c1 = new Circle(0, 0, 3); // 중심(0,0) - 반지름3
    Circle c2 = new Circle(2, 3, 4); // 중심(2,3) - 반지름4
    
    /* 1. 클래스 메소드를 호출하여 원의 넓이를 구하세요. */
    double area1 = Circle.area(c1);
    double area2 = Circle.area(c2);
    
    // 결과 출력
    System.out.printf("%s => 넓이: %.2f\n", c1.toStr(), area1);
    System.out.printf("%s => 넓이: %.2f\n", c2.toStr(), area2);
  }
}

class Circle {
  // 필드
  int x; // 원의 중심 - X 좌표
  int y; // 원의 중심 - Y 좌표
  int r; // 반지름

  // 생성자
  Circle(int centerX, int centerY, int radius) {
    x = centerX;
    y = centerY;
    r = radius;
  }

  // 인스턴스 메소드
  String toStr() {
    return String.format("Circle { 중심: (%d, %d), 반지름: %d }", x, y, r);
  }
  
  // 클래스 메소드
  static double area(Circle c) {
    // 원의 넓이 = 원주율 x 반지름 x 반지름
    return Math.PI * c.r * c.r;
  } 
}
```

# 05 접근 제한자와 게터 세터

## 1. private

- 비공개

## 2. default

- 패키지 내부 공개

## 3. protected

- 상속 공개

```java
class A {
	protected String name;	
}

class B extends A {
	public void printName() { // 부모 클래스 A의 필드 name을 출력
		System.out.println(name);
	}
}
```

## 4. public

- 완전 공개

## 5. getter methods

- private 필드를 반환(get): 비공개 필드를 우회해서 가져옴
- public이다.
- `get` + `필드명`

```java
class SmartPhone {
	private int number;

	public int getNumber() {
		return number;
	}
}
```

## 6. setter methods

- private 필드를 변경(set): 비공개 필드를 우회해서 변경
- public이다.
- `set` + `필드명`

```java
class SmartPhone {
	private int number;

	public void setNumber(int n) {
		number = n;	
	}
}
```

## 7. 스코프와 this

```java
public class CoffeeTest{
	public static void main(String[] args) {

	Coffee americano = new Coffee("아메리카노", 1500);
	System.out.printf("커피값 인상 전 => %s\n", americano.toString());

	// 커피값 인상: 1500 -> 1800
	americano.setPrice(1800);
	System.out.printf("커피값 인상 후 => %s\n", americano.toString());
	}
}

class Coffee {
	// 필드(인스턴스 변수)
	private String name;
	private int price;

	// 생성자
	public Coffee(String name, int price) {
		this.name = name;
		this.price = price;
	}

	// setter
	public void setPrice(int price) {
		this.price = price;
	}

	public String toString() {
		return String.format("Coffee { name: %s, price: %d }", name, price);	
	}
}

/*======================================================
커피값 인상 전 => Coffee { name: 아메리카노, price: 1500 }
커피값 인상 후 => Coffee { name: 아메리카노, price: 1800 }
======================================================*/
```

- `this.변수` : 주체 객체를 가리키게 해줌

# 06  JAVA API

## API

- 도구들의 모음

## 패키지

- 관련 API 묶음

## Math

- 수학 관련 API 묶음

```java
import java.lang.Math;

double r = Math.random();
double a = Math.abs(-8.2019); // 8.2019
double greater = Math.max(1, 2); // 2
double smaller = Math.min(1, 2); // 1
```

## Random

- 난수 생성 관련 API 묶음

```java
import java.util.Random;

Random rand = new Random();
int a = rand.nextInt(10); // 0 <= a < 10
double b = rand.nextDouble(); // 0.0 <= b < 1.0
boolean c = rand.nextBoolean(); // T or F
```

## ArrayList

```java
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<String>();
names.add("Kim");
names.add("Lee");
names.add("Park");

System.out.println(names.get(2)); // Park

names.remove(1); // Lee가 지워지고 Park가 index 1로 옮겨짐
System.out.println(names.size()); // 2

// set(int index, E element) => index 위치 요소를 element로 변경
names.set(0, "Choi"); // names -> {"Choi", "Park"}
```

- 중간값이 지워지면 그 뒤에 있는 값들이 앞으로 당겨짐

## Collections, Arrays

```java
import java.util.Collections;
import java.util.Arrays;

Collections.shuffle(numbers); // 배열 섞기
Arrays.toString(picked); // 값 출력

/*=========================================
numbers.toString();으로 출력하면 주소값이 나옴
=========================================*/
```

# 07 상속(Inheritance)

- 기존 코드를 확장(`extends`)
- 코드 중복 줄이기

- 부모 클래스
- 자식 클래스

```java
class B extends A {...} 
// B는 A를 토대로 확장 됨
// A: 부모 클래스, B: 자식 클래스
```

## 업 캐스팅

- 자식 객체를 부모의 타입으로 해석
- 객체를 `그룹화` 하여 관리하기 위해 사용

```java
class Animal {...}
class Cat extends Animal {...}
class Dog extends Animal {...}
class Horse extends Animal {...}

// 고양이는 동물이다(O)
Cat c = new Cat();
Animal a = c; // 고양이 객체를 동물로 해석

// 동물은 고양이다(X)
Animal aaa = new Animal();
Cat ccc = aaa; // Error!

/* 그룹화 */
Animal c = new Cat();
Animal d = new Dog();
Animal h = new Horse();

Animal[] animals = { c, d, h };
```

## 메소드 오버라이딩(Method Overriding)

- 부모의 메소드를 자식 클래스에서 재정의

```java
public class Overriding {
	public static void main(String[] args) {
		Square s = new Square();
		s.name = "정사각형";
		s.length = 5;

		Triangle t = new Triangle();
		t.name = "삼각형";
		t.base = 4;
		t.height = 3;

		Circle c = new Circle();
		c.name = "원";
		c.radius = 4;

		Shape[] shapes = { s, t, c };

		//모든 도형의 넓이 계산 및 출력
		for (int i = 0; i < shapes.length; i++) {
			Shape tmp = shapes[i];
			System.out.printf("%s의 넓이 -> %.2f\n", tmp.name, tmp.area());
		}
	}
}
// 도형
class Shape {
  String name;

  // 도형의 넓이를 반환
  public double area() {
    return 0;
  }
}

// 정사각형
class Square extends Shape {
  int length; // 한 변의 길이
  
  public double area() {
    return length * length;
  }
}

// 삼각형
class Triangle extends Shape {
  int base;   // 밑변
  int height; // 높이

  public double area() {
    return base * height / 2.0;
  }
}

// 원
class Circle extends Shape {
  int radius; // 반지름

  public double area() {
    return radius*radius*Math.PI;
  }
}

/*======================
정사각형의 넓이 -> 25.00
삼각형의 넓이 -> 6.00
원의 넓이 -> 50.27
======================*/
```

## Super

- 자식 객체를 생성과 동시에 초기화 하려면 부모의 생성자 호출 필요
- `super(object, object, ...);` 키워드 이용

```java
public class SuperTest {
  public static void main(String[] args) {
    Orc orc = new Orc("오크", 80);
    System.out.println(orc.toString());

    OrcWarrior war = new OrcWarrior("오크전사", 120, 3);
    System.out.println(war.toString());
  }
}

class Orc {
  protected String name;
  protected int hp;
  
  public Orc(String name, int hp) {
    this.name = name;
    this.hp = hp;
  }
  
  public String toString() {
    return String.format("Orc { name: %s, hp: %d }", this.name, this.hp);
  }
}

class OrcWarrior extends Orc {
  protected int amor;
  
  public OrcWarrior(String name, int hp, int amor) {
    super(name, hp);
    this.amor = amor;
  }
  
  // 메소드 오버라이딩!
  public String toString() {
    return String.format("OrcWarrior { name: %s, hp: %d, amor: %d }", super.name, super.hp, this.amor);
  }
}

/* ===========================================
Orc { name: 오크, hp: 80 }
OrcWarrior { name: 오크전사, hp: 120, amor: 3 }
=========================================== */
```

## 예시 ) 엘프의 연속 확장

```java
import java.util.ArrayList
public class ElvesTest {
  public static void main(String[] args) {
    // 객체 생성
    Elf elf = new Elf("티란데", 100);
    Elf high = new HighElf("말퓨리온", 160, 100);
    Elf lord = new ElfLord("마이에브", 230, 140, 100);
    
    // 객체 배열 생성
    // Elf[] elves = { elf, high, lord };
    ArrayList<Elf> = new ArrayList<Elf>();
    list.add(elf);
    list.add(high);
    list.add(lord);
    
    모든 객체 정보 출력
    for (int i = 0; i < list.size; i++) {
      // for (int i = 0; i < elves.length; i++)
      // System.out.println(elves[i].toString());
      System.out.println(list.get(i).toString());
    }
  }
}

class Elf {
  protected String name;
  protected int hp;
  
  public Elf(String name, int hp) {
    this.name = name;
    this.hp = hp;
  }
  
  public String toString() {
    return String.format("[엘프] Name: %s, HP: %d", name, hp);
  }
}

class HighElf extends Elf {
  protected int mp;
  
  public HighElf(String name, int hp, int mp) {
    super(name, hp);
    this.mp = mp;
  }

  public String toString() {
    return String.format("[하이엘프] Name: %s, HP: %d, MP: %d", super.name, super.hp, this.mp);
  }
}

class ElfLord extends HighElf {
  protected int shield;
  
  public ElfLord(String name, int hp, int mp, int shield) {
    super(name, hp, mp);
    this.shield = shield;
  }

  public String toString() {
    return String.format("[엘프로드] Name: %s, HP: %d, MP: %d, SH: %d", super.name, super.hp, super.mp, this.shield);
    }
}
```

# 08 인터페이스

## 1. 인터페이스

- 메소드 묶음의 역할 정의 방법

### 장점

- 인터페이스를 통한 `업캐스팅` 가능
    - 관계성 부여 가능
- 프로그램 설계의 명확성 증가

```java
interface Alarm {
	public void beep();
	public void playMusic();
}
```

- **프로토타입(추상) 메소드:** 내용이 없는 껍데기 메소드
    - 중괄호가 없다!
- `implements` : 클래스에게 역할을 부여하는 것

```java
// 구현체 클래스
class SmartPhone implements Alarm {
	// 프로토타입 메소드 오버라이딩
	public void beep() {
		System.out.println("삐비비빅");
	}
	public void playMusic() {
		System.out.println("뉴진스의 하입뽀이");
	}
}
```

### 다형성(Polymorphism)

### 업캐스팅(up-casting)

하나의 객체가 다양한 타입으로 해석되는 것

- 자식 객체를 부모의 타입으로 해석
    - 고양이는 동물이다.
- `인터페이스를 구현하는 객체`도 인터페이스 타입으로 업캐스팅 가능
    - 업캐스팅을 통해 그룹화 가능

### 예제 ) 인터페이스

```java
import java.util.ArrayList;
public class InterfaceReview {
  public static void main(String[] args) {
    // 객체 생성
    Sounding dog = new Dog();
    Sounding baby = new Baby();
    Sounding tiger = new Tiger();
    Sounding robot = new Robot();
    
    // ArrayList를 통한 객체 저장
    ArrayList<Sounding> list = new ArrayList<Sounding>();
    list.add(dog);
    list.add(baby);
    list.add(tiger);
    list.add(robot);
    
    for (int i=0; i < list.size(); i++) {
      list.get(i).sound();
    }
    // 인터페이스 배열 생성
    // Sounding[] arr = { dog, baby, tiger, robot };
    // 소리내기
    // for (int i=0; i<arr.length; i++) {
    //   arr[i].sound();
    // }
  }
}

/* 인터페이스 및 클래스를 작성하시오. */
interface Sounding {
  public void sound();
}

class Dog implements Sounding {
    public void sound() {
      System.out.println("Dog: 멍멍!");
    }
}

class Baby implements Sounding {
  public void sound() {
      System.out.println("Baby: 응애!");
    }
}

class Tiger implements Sounding {
  public void sound() {
      System.out.println("Tiger: 어흥!");
    }
}

class Robot implements Sounding {
  public void sound() {
      System.out.println("Robot: 삐빕!");
    }
}

/*==========
Dog: 멍멍!
Baby: 응애!
Tiger: 어흥!
Robot: 삐빕!
==========*/
```

<aside>
💡 강의 주소: [https://www.youtube.com/playlist?list=PLyebPLlVYXCiKweTN4a-xePbbY1Ta6Yu9](https://www.youtube.com/playlist?list=PLyebPLlVYXCiKweTN4a-xePbbY1Ta6Yu9)

</aside>
