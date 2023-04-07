# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42885
# ==========================================
# 1번 풀이
# ==========================================
def solution(people, limit):
    people.sort()

    ans = 0
    s = 0
    e = len(people) - 1

    while s < e:
        if people[s] + people[e] > limit:
            e -= 1
        else:
            s += 1
            e -= 1
        ans += 1
        if s == e:
            ans += 1

    return ans

# ==========================================
# 2번 풀이
# ==========================================
def solution2(people, limit):
    people.sort()
    ans = 0
    s = 0
    e = len(people) - 1
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            ans += 1
        e -= 1
    return len(people) - ans
