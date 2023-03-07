# 미로탐색
# bfs queue
from collections import deque

n, m = map(int, input().split())
maze = []

# 미로 맵에 길과 벽 넣기
for i in range(n):
  row = list(map(int, input()))
  maze.append(row)

# 방향 정의(동서남북)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  # 큐 초기 좌표
  queue = deque()
  queue.append([x,y])

  while queue:
    # 큐에 들어온 좌표를 가지고 제거함과 동시에 방향마다 비교
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if maze[nx][ny] == 0:
        continue
      if maze[nx][ny] == 1:
        # 이동할 수 있기에 이동한 좌표 맵에 전 좌표+1 해주면서 거리 추가
        maze[nx][ny] = maze[x][y] + 1
        # 다음 좌표를 큐에 넣고 반복 비교
        queue.append([nx, ny])
  # 최종 거리는 반복문이 종료된 후 n*m 크기의 가장 우측 아래 좌표
  return maze[n-1][m-1]

print(bfs(0,0))