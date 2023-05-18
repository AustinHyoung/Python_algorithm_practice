#재풀이
# 1번 빨강 2번 초록 3번 빨강 n번째 색상은 n-1과 n+1의 색상과 달라야함
n = int(input())
# 각 n번째 집의 색깔별 비용
lst = []
for i in range(n):
  lst.append(list(map(int, input().split())))
# 비용을 담을 배열
dp = [[0] * 3 for _ in range(n)]

dp[0] = lst[0]

for i in range(1, n):
  dp[i][0] = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = lst[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))
