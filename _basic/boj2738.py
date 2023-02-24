# 행렬 덧셈

# 배열 초기화
A = []
B = []

n, m = map(int, input().split())

# A배열 row에 다 담아서 넣기
for i in range(n):
  row = list(map(int, input().split()))
  A.append(row)

# B배열 row에 다 담아서 넣기
for i in range(n):
  row = list(map(int, input().split()))
  B.append(row)

# 반복 출력
for i in range(n):
  for j in range(m):
    print(A[i][j] + B[i][j], end=" ")
  print()