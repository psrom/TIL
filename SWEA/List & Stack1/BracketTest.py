# 4866. [파이썬 S/W 문제해결 기본] 4일차-괄호 검사

T = int(input())
for test_case in range(1, T+1):
    bracket_input = input()
    bracket_lst = []
    result = 1
    # 괄호 추가
    for b in bracket_input:
        if (b == "(") or (b == "{"):
            bracket_lst.append(b)
        elif (b == ")") or (b == "}"):
            if len(bracket_lst) == 0:
                result = 0
                break
            # 괄호 짝 검사
            elif (b==")") and (bracket_lst.pop()=="{"):
                result = 0
                break
            elif (b == "}") and (bracket_lst.pop() == "("):
                result = 0
                break

    if len(bracket_lst):
        result = 0

    print("#{} {}".format(test_case, result))