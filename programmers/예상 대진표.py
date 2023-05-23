def solution(n,a,b):
  answer = 0
  match_round = 1
  while True:
    if (a % 2 == 1 and b % 2 == 0 and a + 1 == b) or (a % 2 == 0 and b % 2 == 1 and b + 1 == a):
      break
    
    if a % 2 == 0:
      a = a // 2
    else:
      a = (a // 2) + 1

    if b % 2 == 0:
      b = b // 2
    else:
      b = (b // 2) + 1   
    
    match_round += 1
  answer = match_round
  return answer

print(solution(8,4,7))