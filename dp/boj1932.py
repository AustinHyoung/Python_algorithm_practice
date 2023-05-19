n = int(input())
triangle = []
dp = [[0] * (i+1) for i in range(n)]

for _ in range(n):
  triangle.append(list(map(int, input().split())))

dp[0][0] = triangle[0][0]

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      dp[i][j] = dp[i-1][j] + triangle[i][j]
    elif j == i:
      dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    else:
      dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))


# for i in range(n*2):
#   dp[4][0] = dp[3][0] + triangle[4][0]
#   dp[4][1] = dp[3][0] + triangle[4][1]
#   dp[4][2] = dp[3][1] + triangle[4][1]
#   dp[4][3] = dp[3][1] + triangle[4][2]
#   dp[4][4] = dp[3][2] + triangle[4][2]
#   dp[4][5] = dp[3][2] + triangle[4][3]
#   dp[4][6] = dp[3][3] + triangle[4][3]
#   dp[4][7] = dp[3][3] + triangle[4][4]