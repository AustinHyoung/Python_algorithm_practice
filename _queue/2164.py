# 카드2
# 큐

# n장의 카드 => 5장의 카드
# 카드는 차례로 1부터 n까지 숫자로 적혀있다 1,2,3,4,5,
# 1번이 제일위에 n이 바닥에
# 카드가 한장 남을때가지 반복
# 제일 위에있는 카드 버리기
# 그 다음 제일 위에있는 카드를 바닥으로
# <<<제일 마지막에 남는 카드 구하기>>>

from collections import deque

N = int(input())

queue = deque()

for i in range(1, N+1):
  queue.append(i)

while len(queue) > 1:
  queue.popleft()
  top = queue.popleft()
  queue.append(top)

print(queue[0])
