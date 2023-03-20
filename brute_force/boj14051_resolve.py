# 퇴사
# 브루트 포스

n = int(input())

arr = [[]]

for _ in range(n):
  row = list(map(int, input().split()))
  arr.append(row)

i = 1
j = 0
days = 0

num = []

while i < (n+1):
  arr[i][j]