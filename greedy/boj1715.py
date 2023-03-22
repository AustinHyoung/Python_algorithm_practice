# 카드 정렬하기
# 그리디
import sys
from queue import PriorityQueue
queue = PriorityQueue()

N = int(sys.stdin.readline())
for i in range(N):
  queue.put(int(sys.stdin.readline()))

cnt = 0

while (1):
  if(queue.qsize() == 1):
    break
  a = queue.get()
  b = queue.get()
  cnt += (a + b)
  queue.put(a + b)

print(cnt)
