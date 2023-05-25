# 한번에 1칸 또는 2칸
# 4 5, 3 3, 2 2, 1 1
def solution(n):
  ans = 0
  dp = [0] * (n+1)

  dp[1] = 1
  dp[2] = 2

  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

  ans = dp[n] % 1234567

  return ans

print(solution(8))