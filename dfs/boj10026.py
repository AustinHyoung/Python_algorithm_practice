# 적록색약
# dfs
import sys
sys.setrecursionlimit(1000000)

n = int(input())
rgb = []

for _ in range(n):
  row = list(input())
  rgb.append(row)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
  visited[x][y] = True

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if not visited[nx][ny] and rgb[nx][ny] == rgb[x][y]:
      dfs(nx, ny)

visited = [[False] * n for _ in range(n)]
cnt = 0
blind_cnt = 0

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i, j)
      cnt += 1

for i in range(n):
  for j in range(n):
    if rgb[i][j] == 'R':
      rgb[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i, j)
      blind_cnt += 1

print(cnt, blind_cnt)
