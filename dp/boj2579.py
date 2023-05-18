n = int(input())
scores = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
  scores[i] = int(input())

dp[1] = scores[1]
if n >= 2:
  dp[2] = scores[1] + scores[2]

for i in range(3, n+1):
  # 한계단씩 가는것과 한계단을 띄어 가는것
  dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

print(dp[n])