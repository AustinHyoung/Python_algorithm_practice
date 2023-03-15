# 영역 구하기
# dfs
import sys

sys.setrecursionlimit(100000)

def dfs(x,y):
  visited[x][y] = True
  cnt = 1

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if not visited[nx][ny] and square[nx][ny] == 0:
      cnt += dfs(nx, ny)
  return cnt

n, m, k = map(int, input().split())

square = [[0] * m for _ in range(n)]

for i in range(k):
  # 직사각형의 시작점과 끝점
  sy, sx, ey, ex = map(int, input().split())

  # 시작점부터 끝점까지 직사각형이 있는곳은 1로 초기화
  for i in range(sx, ex):
    for j in range(sy, ey):
      square[i][j] = 1

visited = [[False] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

remain_zone_cnt = 0
remain_zone_size = []

for i in range(n):
  for j in range(m):
    if not visited[i][j] and square[i][j] == 0:
      remain_zone_size.append(dfs(i, j))
      remain_zone_cnt += 1

print(remain_zone_cnt)

for val in sorted(remain_zone_size):
  print(val, end=" ")