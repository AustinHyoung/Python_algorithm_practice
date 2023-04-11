# 1. 직사각형의 최소변이 일단 최대 정사각형 크기
# 2. n >= m, mxm이 정사각형크기
# 3. x,y = 1~m까지
# 4. 크기는 변이 2부터 보면 넓이는 4,9 .. 순서
# 5. i,j 0부터 i는 i,j + 변의길이 - 1 

n, m = map(int, input().split())

answer = 0
lst = []

for i in range(n):
  lst.append(list(map(int, input())))

max_size = min(n, m)
answer = 1

for size in range(2, max_size+1):
  for i in range(n-size+1):
    for j in range(m-size+1):
      if lst[i][j] == lst[i+size-1][j] == lst[i][j+size-1] == lst[i+size-1][j+size-1]:
        answer = size * size

print(answer)

# 재풀이