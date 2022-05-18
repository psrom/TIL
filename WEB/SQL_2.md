# 관계형 DB

1. One-To-One(1:1)
2. Many-To-One(N:1)
   - FK는 N쪽에 둔다.
3. Many-To-Many(N:N)
   - 중간 Table을 둔다.





## 과제

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
--RANK() 적용이 안 됨
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
--모르겠어요 ^^*..
```

