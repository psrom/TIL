# =====================================
# math.ceil() => 반올림
# 배열 잡아서 계산하면 메모리 초과
# =====================================
import math

h, w, n, m = map(int, input().split())

y = math.ceil(h/(n+1))
x = math.ceil(w/(m+1))
ans = x*y
print(ans)
