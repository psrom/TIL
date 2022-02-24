# 입력 : 1 ~ 10번째 줄까지 숫자 하나씩 입력
# 출력 : 42로 나누었을 때 서로 다른 나머지가 몇 개 있는지 출력
from collections import Counter

num = [int(input()) for _ in range(10)]
calc = [i%42 for i in num]
cnt = Counter(calc)
print(len(cnt))

# Counter 함수 사용을 위해 'from collections import Counter'입력
# Counter 함수는 list 내의 원소 개수를 세기 위한 함수
# 서로 다른 나머지가 몇 개인지 알기 위해선 len(cnt)를 사용하면 된다.