import sys
input = sys.stdin.readline

n,m = map(int, input().split())
cnt = 0
s = set()
s_check = set()

for _ in range(n):
  s.add(input().strip())

for i in range(m):
  if input().strip() in s:
    cnt += 1

print(cnt)