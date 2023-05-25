from collections import Counter

def solution(k, tangerine):
  ans = 0
  counter = Counter(tangerine)
  for i in sorted(counter.values(), reverse= True):
    if k <= 0:
      break
    
    k -= i 
    ans += 1

  return ans

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))