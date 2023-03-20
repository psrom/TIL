# 공 바꾸기
# N: 바구니 수, M번 바꿈
# 처음에는 바구니와 공 번호가 같음
# 한 개의 바구니에는 한 개의 공만

N, M = map(int, input().split())
basket = [n for n in range(0, N+1)]

for test_case in range(1, M+1):
    i, j = map(int, input().split())
    reverse_num = [basket[i], basket[j]] # 기존 값 저장
    basket[i] = reverse_num[1] # 값 덮어씌우기
    basket[j] = reverse_num[0] # 값 덮어씌우기

for num in basket[1::]:
    print(num, end = " ")
