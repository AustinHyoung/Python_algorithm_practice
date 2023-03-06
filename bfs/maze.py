# 이코테 미로탈출
from collections import deque

n, m = map(int, input().split())

maze = []

for _ in range(n):
  row = list(map(int, input()))
  maze.append(row)


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  queue = deque()
  # 큐에 시작 좌표 삽입
  queue.append((x,y))
  # 큐가 빌 때까지 반복
  while queue:
    # 좌표 빼기
    x, y = queue.popleft()
    # 다음 좌표 반복
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      
      # 미로 크기에 벗어나면 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 벽이면 무시
      if maze[nx][ny] == 0:
        continue
      # 갈 수 있는길이면
      if maze[nx][ny] == 1:
        # 이동한 좌표의 값에 현재 좌표값 + 1 = 현재거리
        maze[nx][ny] = maze[x][y] + 1
        # 이동한 좌표를 큐에 삽입
        queue.append((nx, ny))
        # 이동한 좌표 방문처리
  return maze[n-1][m-1]

print(bfs(0,0))
