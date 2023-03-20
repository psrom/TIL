# push 알고리즘
s = []
def push(item):
    s.append(item)

# pop 알고리즘
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1)

# =====================================================================
# 리스트 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간 소요

# 해결방법
# 1. 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용
# 2. 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택 구현
