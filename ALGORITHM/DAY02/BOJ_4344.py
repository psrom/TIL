for _ in range(int(input())):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    student = 0
    for score in scores[1:]:
        if score > avg:
            student += 1
    rate = student/scores[0]*100
    print(f'{rate:.3f}%')