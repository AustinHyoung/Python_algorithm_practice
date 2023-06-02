n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
dp[0] = lst[0]

for i in range(1, n):
  dp[i] = max(lst[i], dp[i-1] + lst[i])

max_val = max(dp)

print(max_val)

# 10
# 6
# 9
# 10
# 15
# 21
# -14
# 12
# 33
# 32