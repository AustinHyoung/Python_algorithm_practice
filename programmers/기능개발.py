def solution(progresses, speeds):
  ans = []
  stack = []

  for p, s in zip(progresses, speeds):
    day = (100 - p) // s
    if (100 - p) % s != 0:
      day += 1

    if not stack or stack[-1] < day:
      stack.append(day)
      ans.append(1)
    else:
      ans[-1] += 1

  return ans

print(solution([93, 30, 55], [1, 30, 5]))