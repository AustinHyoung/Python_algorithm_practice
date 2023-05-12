# n = 1
# 경우의 수 1 나머지 1
# n = 2
# 경우의 수 2 나머지 2
# n = 3
# 경우의 수 3 나머지 3
# n = 4
# 경우의 수 5 나머지 5

# n4 = n 점화식 nx = nx-1 + nx-2

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
