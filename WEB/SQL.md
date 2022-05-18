# SQL

: Structured Query Language



## RDBMS

- 전통적인 DB
- 상호 관련성이 있는 테이블의 집합
- 범용성/고성능/일관성/정규화
- 대량의 데이터

- 종류: Oracle, MS-SQL Server, MySQL(Oracle), DB2, MariaDB, SQLite



## NoSQL

- Not only SQL
- SQL을 보완할 때 사용



## SQL 문장 종류

__데이터 조작어(DML: Data Manipulation Language)__

- SELECT
- INSERT, UPDATE, DELETE

__데이터 정의어(DDL: Data Definition Language)__

- CREATE, ALTER, DROP, RENAME

__데이터 제어어(DCL: Data Control Language)__

__트랜잭션 제어어(TCL: Transaction Control Language)__



## SQL 실습

https://www.w3schools.com/sql/trysql.asp?filename=trysql_asc

```sql
--고객(Customer)의 이름과 국가를 조회
SELECT CustomerName, Country 
FROM Customers;

--고객(Customer) 정보 전체 조회
SELECT * FROM Customers;

--고객의 국가 목록 중복 없이 조회
SELECT DISTINCT Country 
FROM Customers;

--국가가 France인 고객 조회
SELECT *
FROM Customers
WHERE Country="France";
```

```sql
--이름이 'Bl'로 시작하는 고객 조회
SELECT *
FROM Customers
Where CustomerName LIKE 'Bl%'

--이름이 'et'로 끝나는 고객 조회
SELECT *
FROM Customers
Where CustomerName Like '%et'

--이름에 'et'가 들어가는 고객 조회
SELECT *
FROM Customers
Where CustomerName Like '%et%'
```

```sql
--국가가 France이고 ContactName이 'Mar'로 시작하는 고객(Customers) 조회
SELECT *
FROM Customers
WHERE Country='France' AND ContactName LIKE 'Mar%';

--국가가 France이거나 ContactName이 'Mar'로 시작하는 고객(Customers) 조회
SELECT *
FROM Customers
WHERE Country='France' OR ContactName LIKE 'Mar%';

--국가가 France이 아니고 ContactName이 'Mar'로 시작하지 않는 고객(Customers) 조회
SELECT *
FROM Customers
(WHERE NOT Country='France') AND (ContactName NOT LIKE 'Mar%');
```

```sql
--국가가 France 혹은 Spain 사는 고객 조회
SELECT *
FROM Customers
WHERE Country IN ('France', 'Spain');

--가격이 15에서 20사이인 상품(Products) 조회
SELECT *
FROM Products
WHERE Price BETWEEN 15 AND 20;

--가격이 15에서 20사이인 상품(Products)의 생산자 목록 조회
SELECT *
FROM Suppliers
WHERE SupplierID IN (SELECT SupplierID
					 FROM Products
					 WHERE Price BETWEEN 15 AND 20);
					 
--ProductName이 Chais인 생산자 목록 조회
SELECT *
FROM Suppliers
WHERE SupplierID = (SELECT SupplierID
                    FROM Products
                    WHERE ProductNAME = 'Chais');
```

```sql
--NULL값 조회
SELECT * FROM Shippers
WHERE Phone IS NULL;

--오름차순 조회
--내림 차순은 `ProductName DESC`
SELECT *
FROM Products
ORDER BY ProductName;

--CategoryID 오름차순, SupplierID 내림차순 정렬
SELECT *
FROM Products
ORDER BY CategoryID ASC, SupplierID DESC;
```

```sql
--국가가 UK 고객 중 이름순 3명 조회
SELECT *
FROM Customers
WHERE Country='UK'
ORDER BY customerName
LIMIT 3;

--상품 가격이 30 미만 ‘저', 30~50 ‘중', 50 초과는 ‘고'로 조회
SELECT *,
	CASE
    	WHEN Price<30 THEN '저'
        WHEN Price>=30 AND Price<50 THEN '중'
        ELSE '고'
    END
FROM PRODUCTS;

--프랑스 고객수 조회
SELECT COUNT(*)
FROM Customers
WHERE Country='France';
```

### GROUP BY

```sql
--Q. 국가 별 고객수 조회(고객수 기준 오름차순)
--: 국가명, 고객수 
SELECT COUNT(*), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(*);

--Q. 국가별 고객수를 조회하고 그 중 5명 초과인 국가만 조회 (고객수 내림차순)
--: 국가명, 고객수
SELECT COUNT(*), Country
FROM Customers
Group BY Country
HAVING COUNT(*) > 5
ORDER BY COUNT(*);
```

```sql
--Q. 상품을 조회하는데, 카테고리 이름과 함께 보이도록 조회
SELECT *
FROM Products, Categories
WHERE Products.CategoryID = Categories.CategoryID;

--Q.Londona에 위치한 공급자(Supplier)가 생산한 상품 목록 조회
--: 도시명, 공급자명, 상품명, 상품가격
SELECT City SupplierName, ProductName, Price
From Suppliers AS S
JOIN Products AS P
ON S.SupplierID = P.SupplierID;
WHERE City='Londona';

--Q. 분류가 Seafood인 상품 목록(모든 컬럼 조회): 분류, 상품 모든 컬럼
SELECT *
FROM Products AS P
JOIN Categories AS C
ON P.CategoryID = C.CategoryID
WHERE CategoryName='Seafood'

--Q. 공급자(Supplier) 국가별, 카테고리 별 상품 건수, 평균가격: 국가명, 카테고리명, 상품건수, 평균가격
SELECT Country, CategoryName, count(*), AVG(price)
FROM Suppliers
JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
JOIN Categories
ON Categories.CategoryID = Products.CategoryID
GROUP BY Country, CategoryName

--Q. 상품 카테고리별, (공급자)국가별, 도시별 주문건수 2건 이상인 목록: 카테고리명, 국가명, 도시명, 주문건수
SELECT CategoryName, Country, City, Count(*)
FROM Products AS P
JOIN Categories AS C
ON P.CategoryID = C.CategoryID
JOIN Suppliers AS S
ON P.SupplierID = S.SupplierID
JOIN OrderDetails AS OD
ON OD.ProductID = P.ProductID
GROUP BY CategoryName, Country, City
HAVING COUNT(*) >= 2;
```

### 과제

```sql
--Q. 주문자, 주문정보, 직원정보, 배송자정보 통합 조회: 고객컬럼 전체, 주문정보 컬럼 전체(order, orderDetail)

SELECT *
FROM Orders AS O
JOIN OrderDetails AS OD
ON O.OrderID = OD.OrderID
JOIN Customers AS C
ON O.CustomerID = C.CustomerID
JOIN Shippers AS S
ON S.ShipperID = O.ShipperID;

--Q. 판매량(Quantity) 상위 TOP3 공급자(Supplier) 목록: 공급자 명, 판매량, 판매금액

SELECT SupplierName, SUM(Quantity), SUM(Price*Quantity)
FROM Products
JOIN OrderDetails
On Products.ProductID = OrderDetails.ProductID
JOIN Suppliers
On Products.SupplierID = Suppliers.SupplierID
GROUP BY SupplierName
ORDER BY SUM(Quantity) DESC
LIMIT 3;

--Q. 상품(Product)분류(Category)별, 고객 지역별(City) 판매량 순위: 순위, 카테고리명, 고객지역명, 판매량
--RANK 안 먹힘
SELECT CategoryID, City, SUM(Quantity)
FROM Products
JOIN OrderDetails 
ON Products.ProductID = OrderDetails.ProductID
JOIN Orders
ON OrderDetails.OrderID = Orders.OrderID
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
GROUP BY CategoryID, City
ORDER BY SUM(Quantity) DESC;

--Q. 고객 국가가 USA이고, 상품별 판매량(Quantity 수량 합계) 순위: 국가명, 상품명, 판매량, 판매금액
SELECT Country, ProductName, SUM(Quantity), SUM(Quantity*Price)
FROM Customers
JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
JOIN OrderDetails
On Orders.OrderID = OrderDetails.OrderID
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
WHERE Country = 'USA'
GROUP BY ProductName
ORDER BY SUM(Quantity) DESC

--Supplier의 국가가 Germany인 상품 카테고리별 상품 수: 국가명, 카테고리명, 상품수
SELECT  Country, CategoryName, COUNT(ProductName)
FROM Suppliers
JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
JOIN Categories
ON Products.CategoryID = Categories.CategoryID
WHERE Country = 'Germany'
GROUP BY CategoryName;

--Q.월별 판매량 및 판매금액: 연도, 월, 판매량, 판매금액
--함수 사용 안 하고 어떻게 추출하지?
```



### INSERT

```sql
INSERT 

INSERT INTO Shippers(ShipperName) VALUES('Pantos');

```

### DELETE

```python
DELETE
FROM Shippers
WHERE ShipperID=6
```

### UPDATE

```sql
UPDATE Shippers
SET ShipperName = 'CJ'
WHERE ShipperID=3;
```

### VIEW TABLE

```sql
CREATE VIEW CUSTOMER_ORDER AS
SELECT *
FROM Customers
JOIN Orders
ON Orders.CustomerID = Customers.CustomerID;
```

### CREATE TABLE

```sql
CREATE TABLE Credits(
    -- Primary Key(주요키, 기본키, PK)
    -- Foriegn Key(외래키, 외부키, FK) : 관계를 맺기 위한 FIELD 값
	CreditID	INT		AUTO_INCREMENT PRIMARY KEY, -- 제약조건(Constraints)
    amount		INT		NOT NULL	DEFAULT 0,
    CustomerID	INT,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL;
    -- `CASCADE` 같이 삭제, linking 깨지면 NULL 넣기
);
```



### DROP TABLE

```sql
DROP TABLE table_name; -- 테이블 자체를 삭제

TRUNCATE TABLE table_name; -- 테이블 안에 있는 값을 전체 삭제
```

