# 최댓값
import sys

# 9x9 배열 생성
a = []

for i in range(9):
  row = list(map(int, sys.stdin.readline().split()))
  a.append(row)

# 최댓값 과 그에 맞는 행렬 초기값 설정
max_val = a[0][0]
row = 0
col = 0

# 반복문을 사용하여 행렬과 최대값 갱신
for i in range(len(a)):
  for j in range(len(a[i])):
    if max_val <= a[i][j]:
      max_val = a[i][j]
      row = i+1
      col = j+1

# 최종 출력
print(max_val)
print(row, col)

