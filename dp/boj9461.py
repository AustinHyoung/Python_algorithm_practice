t = int(input())

for _ in range(t):
  n = int(input())
  dp = [0] * 101
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  dp[4] = 2
  dp[5] = 2

  for i in range(6, n+1):
    dp[i] = dp[i-5] + dp[i-1]

  print(dp[n])


# 5 7 9 12 16 21 28 37