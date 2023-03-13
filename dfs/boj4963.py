# 섬의 개수
# dfs
import sys
sys.setrecursionlimit(10000)

while True:
  # 크기 입력 받기
  m, n = map(int, sys.stdin.readline().split())
  if n == 0 and m == 0:
    break
  graph = []
  for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
  
  visited = [[False] * m for _ in range(n)]
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  
  def dfs(x, y):
    visited[x][y] = True

    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
        dfs(nx,ny)
  
  result = 0 

  for i in range(n):
    for j in range(m):
      if not visited[i][j] and graph[i][j]:
        dfs(i,j)
        result += 1
  
  print(result)