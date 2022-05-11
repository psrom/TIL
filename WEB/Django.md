# Django

## 파이썬의 웹 프레임워크

__Flask__ : Micro Framework => 간단한 앱을 만들 때는 쉽다(DB X)

__Django__ : Battery Included => 모든 게 다 있다



## Database의 종류

#### RDB(Relational Database)-SQL(Structured Query Language)

: 전통적인 Database (1970~) SQL

- Oracle
- MySQL(MariaDB) - OpenSource
- MSSQL
- sqlite - 경량화된 RDB(OpenSource)



- User Table

| id   | name |      | phone         |
| ---- | ---- | ---- | ------------- |
| 1    | YS   |      | 010-0000-0000 |

- Board Table

| title | content | author |      |
| ----- | ------- | ------ | ---- |
| 제목1 | 본문1   | YS     |      |
| 제목2 | 본문2   | YS     |      |



#### NoSQL(Not Only SQL)

: Database를 구성 하는데 SQL만 있는 건 아니다. 다른 방법도 많다.

- Document Database(MongoDB): JSON 형태로 저장
- In memory Database: Redis
- Elastic Search
- 카산드라



__데이터 베이스를 바꾸려면__...

- settings.py에서 DATABASES 수정



### 

## 참고

### Asyncronous Gateway Interface :left_right_arrow: Syncronous

Async(비동기적) vs. sync(동기적)

```python
# Process
f = open("", r)
contents = f.read()
print(contents) # 10초

f2 = open("", r)
contents2 = f2.read()
print(contents2) # 3초

# Async(비동기): 10s (nodejs)
# sync(동기): 13s
```

__NIO__: Request/ Response도 파일로 Input, Output __file__ 관리

```python
for i in range(10):
    resp = requests.get(url) #3초
    
# sync(동기): 30s
# async(비동기): 4s
```

---





