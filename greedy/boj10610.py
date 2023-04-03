# 30
# 그리디

n = int(input())

max_num = int(''.join(sorted(str(n), reverse=True)))

if max_num % 30 == 0:
  print(max_num)
else:
  print(-1)
