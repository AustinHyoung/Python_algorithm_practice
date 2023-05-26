def solution(citations):
  ans = 0
  citations.sort(reverse=True)

  for i in range(len(citations)):
    if citations[i] >= i + 1:
      ans = i + 1
    else:
      break

  return ans

print(solution([3,0,6,1,5]))