# 이코테 음료수 얼려먹기

n, m = map(int, input().split())

drink = []

for _ in range(n):
  row = list(map(int, input()))
  drink.append(row)

visited = [[False] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
  visited[x][y] = True
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if not visited[nx][ny] and drink[nx][ny] == 0:
      dfs(nx, ny)


total_cnt = 0

for i in range(n):
  for j in range(m):
    # 방문하지 않고 유효한 공간이면 => 거기서부터 방문 재귀함수 dfs
    if not visited[i][j] and drink[i][j] == 0:
      # 한개이건 몇개이건 공간이 있는것이기 때문에 총 개수를 추가
      total_cnt += 1
      dfs(i, j)

print(total_cnt)