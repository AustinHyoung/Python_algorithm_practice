# 토마토
# bfs
from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 벽
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()
for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      queue.append((i, j))

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    if box[nx][ny] == -1 or box[nx][ny] == 1:
        continue
    box[nx][ny] = box[x][y] + 1
    queue.append((nx, ny))

# 모든 토마토가 익지 못하는 경우 체크
is_possible = True
result = 0
for i in range(n):
  for j in range(m):
    if box[i][j] == 0:
      is_possible = False
    else:
      result = max(result, box[i][j])
if is_possible:
  print(result-1)
else:
  print(-1)