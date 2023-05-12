# 기준값으로 다음으로 오는 값과 큰값을 비교
n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
  for j in range(i):
    if lst[j] > lst[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))