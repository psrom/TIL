# [S/W 문제해결 기본] 1일차 숫자카드

T = int(input())

for test_case in range(1, T+1):
    card_num = int(input())  # 총 카드 개수
    num_lst = [0] * 10  # 0~9 리스트

    cards = list(map(int, input()))
    for i, card in enumerate(cards):
        num_lst[card] += 1

    # 최댓값이 단 1개일 때
    if num_lst.count(max(num_lst)) == 1:
        maximum = max(num_lst)
        max_idx = num_lst.index(max(num_lst))
        print(f"#{test_case} {max_idx} {maximum}")

    # 최댓값이 여러개일 때 ex. 9가 3개, 1이 3개 => 9출력
    else:
        same_idx = []
        maximum = max(num_lst)
        for i, card in enumerate(num_lst):
            if card == max(num_lst):
                same_idx.append(i)

        print(f"#{test_case} {max(same_idx)} {maximum}")




