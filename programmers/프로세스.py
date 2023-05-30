from collections import deque
def solution(priorities, location):
  queue = deque([(p, i) for i, p in enumerate(priorities)])
  cnt = 0
  
  while True:
    x = queue.popleft()
    if any(x[0] < q[0] for q in queue):
      queue.append(x)
    else:
      cnt += 1
      if x[1] == location:
        return cnt


print(solution([1, 1, 9, 1, 1, 1], 0))
