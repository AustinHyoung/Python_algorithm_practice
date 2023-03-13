# 안전 영역
# dfs
import sys

sys.setrecursionlimit(10000000)

def dfs(x,y,depth):
  visited[x][y] = True
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if not visited[nx][ny] and space[nx][ny] > depth:
      dfs(nx, ny, depth)

n = int(input())
space = []
for _ in range(n):
  row = list(map(int, input().split()))
  space.append(row)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

max_safezone = []
max_height = max(map(max, space))

for depth in range(max_height):
  cnt = 0
  visited = [[False] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if not visited[i][j] and space[i][j] > depth:
        dfs(i, j, depth)
        cnt += 1
  max_safezone.append(cnt)

print(max(max_safezone))