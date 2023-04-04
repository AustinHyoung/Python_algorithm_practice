# 행복 유치원
# 그리디

# 조에서 가장 키큰 사람 - 가장 키작은 사람 = 티셔츠 비용
# k개의 조의 티셔츠비용 최소비용

n, k = map(int, input().split())

heights = list(map(int, input().split()))
diff = []

for i in range(n-1):
  diff.append(heights[i+1] - heights[i])

diff.sort()

answer = sum(diff[:n-k])
print(answer)
