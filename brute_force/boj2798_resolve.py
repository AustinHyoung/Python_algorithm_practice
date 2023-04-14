# 3장의 카드를 고른 합이 M 보다 작거나 같으면서 최대한 가까운 수

n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0

for i in range(len(lst)):
  for j in range(i+1, len(lst)):
    for k in range(j+1, len(lst)):
      sum = lst[i]+lst[j]+lst[k]
      if sum <= m:
        answer = max(answer, sum)

print(answer)

