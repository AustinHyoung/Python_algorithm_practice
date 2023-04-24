# 짝수번이면 짝수번 / 2 => 다음라운드 번호
# 홀수번이면 홀수번 / 2 +1 => 다음라운드 번호
# 대결구도: 홀수번호는 무조건 다음 번호인 짝수번호와 대결 +1, 짝수번호는 무조건 이전 번호인 홀수번호와 대결 -1
# 라운드 개수: 첫 n부터 1라운드, / 2를 한 후에 라운드 +1

n, kim, lim = map(int, input().split())
match_round = 1
while True:
  if (kim % 2 != 0 and (kim + 1) == lim) or (lim % 2 != 0 and (lim + 1) == kim):
    break
  # kim num
  if kim % 2 == 0:
    kim /= 2
  else:
    kim += 1
    kim /= 2
  
  # lim num
  if lim % 2 == 0:
    lim /= 2
  else:
    lim += 1
    lim /= 2
  
  match_round += 1
  

if (kim % 2 != 0 and (kim + 1) == lim) or (lim % 2 != 0 and (lim + 1) == kim):
  print(match_round)
else:
  print(-1)
