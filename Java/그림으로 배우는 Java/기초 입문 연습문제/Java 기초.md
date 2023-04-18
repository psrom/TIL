# 그림으로 배우는 JAVA(기초 입문)

YouTube: https://www.youtube.com/playlist?list=PLyebPLlVYXCgb5B-toSOvivS1RChZLnNu

# 01 자바의 특징

- 객체 지향 프로그래밍(object-oriented programming): 유지, 보수에 용이

# 02 Type

```java
double a = 5.0 / 2.0; // 2.5
int b = 4 / 2; // 2
int c = 5 / 2; // 2

String seven = 7; // ERROR
String seven = "7";

// 자동 변환
double p = 2; // 2.0
int n = 5/2; // 2
double q = n; // q = 2.0

int r = 10.4; // ERROR
int r = (int) 10.4; // 강제 캐스팅: 10
double c = (int) (5.0 / 2.0); // 2.0
```

- 대입값과 변수 타입이 일치해야 함
- `byte/ short/ int/ long/ float/ double` : 캐스팅 가능

---

# 03 자바의 구성

## 1. class

```java
public class Main {
} 
```

- 객체를 만들기 위한 틀
- 유사한 특징을 지닌 객체들의 속성과 동작을 묶은 집합체

## 2. main

```java
public class Main{
	public static void main(String[] args){
	}
}
```

- 자바 프로그램의 시작점

---

## 3. Method

- Java API에 있는 프로그래밍 도구를 호출
- 일련의 코드를 단순화

### 1. println()

```java
public class Main{
	public static void main(String[] args) {
	
	System.out.println("Hello world!");

	}
}
```

- input: `System.out.println("문자열")` ⇒ output: `문자열`

### 2. printf()

```java
public class Main {
	public static void main(String[] args) {
	
	int age = 1;
	System.out.printf("신생아의 나이는 %d세 입니다.", age);

	}
}
```

- `%d` : 정수 type
- `%f` : 실수 type
    - `%.2f`: 소수점 두 자리 수까지 출력
- `%s` : 문자열
- `\n` : 줄바꿈이 필요할 때 (ex. `%s\n`)

<aside>
💡 **질문: 왜 실수를 float로 안 쓰고 double이라고 쓰는지?**
float는 4byte, double은 8byte이다.
double의 *정밀도*가 더 높다!

[https://devlog-wjdrbs96.tistory.com/254](https://devlog-wjdrbs96.tistory.com/254)

</aside>

### 3. parseInt(), parseDouble()

```java
// String to Int
String one = "1";
String two = "2";

int a = Integer.parseInt(one); // "1" => 1
int b = Integer.parseInt(two); // "2" => 2

// String to Double
String pi = "3.14";

double c = Double.parseDouble(pi); // "3.14 => 3.14"
```

- 입력값을 받을 때는 `int a = Integer.parseInt(args[0]);` 으로 작성

### Math 클래스

```java
//원주율
double pi = Math.PI; // 3.141592...

// 절대값
double x = Math.abs(-1.2); // 1.2

// 반올림
long n = Math.round(1.6); // 2
```

## 메소드 만들기

```java
// public static #type #name(input type + var)
public static int square(int n) {
	int result;
	result = n * n;
	return result;
}
```

## 단일 파라미터 메소드

- 입력 변수(parameter)가 하나만 있는 메소드

## 다중 파라미터 메소드

- 입력 변수가 2개 이상인 경우

---

# 04 조건문

- 조건에 따라 실행 흐름을 결정

## 1. if

```java
if (조건식) {
// (조건이 참이면 실행할 내용)
}
```

## 2. if-else

```java
if (조건식) {
  // 참인 경우
} else {
  // 거짓인 경우
}
```

## 3. else-if

- 파이썬 `elif` 와 같은 기능

```java
if (조건식) {

} else if (조건식) {

} else {

}
```

## 비교/논리 연산자

### 비교 연산자

`==, !=, >, >=, <, <=`

### 논리 연산자

- AND(`&&`)
- OR(`||`)

# 05 반복문

## 1. for 문

```java
for (int i = 1; i <= 10; i++) {
	System.out.printf("# %d", i);
}
```

## 2. while문

```java
int n = 1;
while (n <= 10) {
	System.out.println(n);
	n++;
}
```

## 3. break

```java
if (조건식) {
	break; //조건식이 참이면 탈출
}
```

## 4. continue

```java
public class Continue {
  public static void main(String[] args) {
    printSum(1, 10);
  }
  
  public static void printSum(int start, int end) {
    int sum = 0;

    for (int i = start; i <= end; i++) {
      if (i % 3 == 0) {
        continue;
      }
      
      System.out.printf("%d", i);
      sum += i;
      
      if (i==end) {
        break;
      }
      System.out.printf(" + ");
    }
    
    System.out.printf("\n=> %d", sum);
  }
}

/* =======================
output:
1 + 2 + 4 + 5 + 7 + 8 + 10
=> 37
======================= */
```

# 06 배열

- 배열 안의 type이 동일해야 한다.
- 순서有

```java
int[] score = {100, 98, 50};
double[] num = {36.5, 37.5};

// 출력
for (int i = 0; int<10; i++) {
	System.out.printf("학생 %d: %d점\n", i, score[i]);
}
```

## 1. 생성

```java
// 1. 생성과 동시에 초기화
String[] names = {"Alice", "Barbie"};

// 2. 공간 할당 후 값 대입
int[] ids = new int[3];
ids[0] = 100;
ids[1] = 200;
ids[2] = 300;
```

## 2. 읽기/ 변경

```java
// 1. 배열 값 읽기
int[] scores = {100, 99, 98};
System.out.println(score[1]); // 99

// 2. 배열 값 변경
System.out.println(scores[2]); // 98
scores[2] = 200;
System.out.println(scores[0]); // 200
```

### length keyword

```java
String[] names = {"Alice", "James"};
int[] scores = {99, 87};

for (int i = 0; i < names.length; i++) {
	System.out.printf("%s : %d\n", names[i], scores[i]);
}
```
