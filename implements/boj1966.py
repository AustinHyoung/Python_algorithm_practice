# 프린터 큐
# 구현

# 3 테스트케이스
# 1 0 문서의개수, queue에서 몇번째에 놓여잇는지 인덱스
# 5 문서의 개수만큼 문서의 '중요도'를 나타냄

from collections import deque

T = int(input())

for i in range(T):
  n, m = map(int, input().split())
  im = list(map(int, input().split()))

  queue = deque([(i, p) for i, p in enumerate(im)])
  cnt = 0

  while True:
    cur = queue.popleft()
    if any(cur[1] < x[1] for x in queue):
      queue.append(cur)
    else:
      cnt += 1
      if cur[0] == m:
        print(cnt)
        break
