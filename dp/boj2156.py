n = int(input())
lst = [0]
for _ in range(n):
  lst.append(int(input()))

dp = [0] * 10001

dp[1] = lst[1]

if n > 1:
  dp[2] = lst[1] + lst[2]

for i in range(3, n+1):
  dp[i] = max(dp[i-1], lst[i] + dp[i-2], lst[i] + lst[i-1] + dp[i-3])

print(dp[n])


# dp[2] = max(lst[1] , dp[1]+lst[2])
