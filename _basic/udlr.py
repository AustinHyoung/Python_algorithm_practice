n = int(input())
x,y = 1,1
plans = input().split()

# 동서남북
dx = [0,0,1,-1]
dy = [1,-1,0,0]
move_types = ['R', 'L', 'D', 'U']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 2차원 공간에 1,1이 첫번째 위치니까 그 이하는 없기 때문에 1보다 작은건 없다
  # 반대로 최대크기가 n*n의 크기이니까 위치가 n보다 클 수 없다.
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x,y)

