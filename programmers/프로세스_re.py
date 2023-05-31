from collections import deque
def solution(priorities, location):
  cnt = 0
  queue = deque([(idx, pri) for (idx, pri) in enumerate(priorities)])

  while True:
    x = queue.popleft()
    if any(x[1] < q[1] for q in queue):
      queue.append(x)
    else:
      cnt += 1
      if x[0] == location:
        return cnt
  

print(solution([2,1,3,2], 2))