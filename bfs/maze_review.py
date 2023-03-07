# queue
from collections import deque

n, m = map(int, input().split())

map_arr = []

for i in range(5):
  row = list(map(int, input()))
  map_arr.append(row)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  queue = deque()
  queue.append([x,y])

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if map_arr[nx][ny] == 0:
        continue
      if map_arr[nx][ny] == 1:
        map_arr[nx][ny] = map_arr[x][y] + 1
        queue.append([nx, ny])
  return map_arr[n-1][m-1]

print(bfs(0,0))
