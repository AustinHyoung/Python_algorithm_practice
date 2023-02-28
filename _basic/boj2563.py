# 색종이
# 빈 배열에서 0을 1로 만들어서 접근
paper = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
  x, y = map(int, input().split())

  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j] = 1

area = 0

for i in range(100):
  for j in range(100):
    area += paper[i][j]

print(area)