# 단지 번호붙이기
# 2차원 배열 dfs
n = int(input())

map_arr = []

for i in range(n):
  row = list(map(int, input()))
  map_arr.append(row)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False] * n for _ in range(n)]


def dfs(x,y):
  # 현재위치 방문 체크
  visited[x][y] = True
  cnt = 1

  # 다음위치 이동
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if not visited[nx][ny] and map_arr[nx][ny] == 1:
      cnt += dfs(nx, ny)
  return cnt

total_cnt = 0
home_cnt = []


for i in range(n):
  for j in range(n):
    if not visited[i][j] and map_arr[i][j] == 1:
      total_cnt += 1
      home_cnt.append(dfs(i,j))

print(total_cnt)
for count in sorted(home_cnt):
    print(count)