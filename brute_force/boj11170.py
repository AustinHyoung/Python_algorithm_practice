t = int(input())

for i in range(t):
  n, m = map(int, input().split())

  zero_cnt = 0
  for i in range(n, m+1):
    zero_cnt += str(i).count('0')

  print(zero_cnt)
