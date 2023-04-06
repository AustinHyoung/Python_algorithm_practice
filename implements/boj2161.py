# 카드 1
# 구현

from collections import deque

queue = deque()

n = int(input())

for i in range(1, n+1):
  queue.append(i)

while True:
  print(queue.popleft(), end=" ")
  if not queue:
    break
  tmp = queue.popleft()
  queue.append(tmp)
  

