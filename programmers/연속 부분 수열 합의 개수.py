def solution(elements):
  ans = 0
  numberSet = set()

  elementLen = len(elements)
  elements = elements * 2

  for i in range(elementLen):
    for j in range(elementLen):
      numberSet.add(sum(elements[j:j+i+1]))
  
  ans = len(numberSet)
  return ans

print(solution([7,9,1,1,4]))
