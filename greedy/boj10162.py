# 전자레인지
# 그리디
import sys

time = [300, 60, 10]

T = int(sys.stdin.readline())

cnt = []

for t in time:
  cnt.append(T // t)
  T -= (T // t) * t

if T > 0:
  print(-1)
else:
  for c in cnt:
    print(c, end=" ")

