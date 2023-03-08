# 토마토
# bfs
from collections import deque

m, n = map(int, input().split())
box = []

for _ in range(n):
  row = list(map(int, input().split()))
  box.append(row)

# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 벽
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if box[nx][ny] == -1 or box[nx][ny] == 1:
        continue
      box[nx][ny] = box[x][y] + 1
      queue.append((nx, ny))

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      bfs(i, j)

not_tomato = True
result = 0

for i in range(n):
  for j in range(m):
    if box[i][j] == 0:
      not_tomato = False
    else:
      result = max(result, box[i][j])
if not_tomato:
  print(result - 1)
else:
  print(-1)