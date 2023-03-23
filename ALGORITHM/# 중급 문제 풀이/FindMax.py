# 문제1) 9개의 서로 다른 자연수 중 최댓값과 그 위치 찾기

numbers = [input() for _ in range(9)]
max_num = max(numbers)

print(max_num)
print(numbers.index(max_num)+1)