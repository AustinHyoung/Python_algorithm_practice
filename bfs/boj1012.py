# 유기농 배추
# bfs
from collections import deque

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 테스트케이스
for i in range(t):
  n, m, k = map(int, input().split())
  # n * m 땅 생성
  land = [[0] * m for _ in range(n)]
  for _ in range(k):
    x,y = map(int, input().split())
    land[x][y] = 1
  
  # 방문 체크
  visited = [[False] * m for _ in range(n)]

  # bfs로 인접한 곳 추려내기
  def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    
    while queue:
      x,y = queue.popleft()

      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          continue
        if not visited[nx][ny] and land[nx][ny] == 1:
          queue.append([nx, ny])
          visited[nx][ny] = True

  # 지렁이 개수
  
  earthworm_cnt = 0
  # 인접한 곳을 확인하고 그지역만 count +1
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and land[i][j] == 1:
        earthworm_cnt += 1
        bfs(i, j)

  print(earthworm_cnt)
  
