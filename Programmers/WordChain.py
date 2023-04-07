# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 한번에 두 가지를 구현할 수는 없을까?
# 같은 단어가 나왔는지 확인 => 통과한 단어만 끝말잇기가 제대로 됐는지 확인

def solution(n, words):
    answer = []
    fl_words = [[i[0], i[-1]] for i in words]
    stack = []
    tf_answer = True

    # 끝말잇기가 제대로 됐는지 확인
    for i in range(len(fl_words)):
        if not stack:
            stack.append(fl_words[i][1])
        else:
            p = stack.pop()
            if p == fl_words[i][0]:
                stack.append(fl_words[i][1])

            else:
                answer = [i % n + 1, i // n + 1]
                tf_answer = False
                break

    # 같은 단어가 나왔는지 확인
    dict = {}
    cnt = 0
    for w in words:
        if w in dict:
            answer = [cnt % n + 1, cnt // n + 1]
            tf_answer = False
            break
        else:
            dict[w] = 1
            cnt += 1

    if tf_answer == True:
        answer = [0, 0]

    # 인덱스번호//n + 1 <= 차례
    return answer