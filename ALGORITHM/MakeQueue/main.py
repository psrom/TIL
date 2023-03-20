# python Queue 이용하기
import queue

que = queue.Queue()
que.put(1)
que.put(2)
que.put(3)

print(que.get())  # 1
print(que.get())  # 2

