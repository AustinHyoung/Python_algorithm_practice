# 날짜 계산
# 브루트포스

e,s,m = map(int,input().split())
a, b, c = 1, 1, 1

cnt = 1
while True:
  if a > 15:
    a = 1

  if b > 28:
    b = 1

  if c > 19:
    c = 1

  if a == e and b == s and c == m:
    break

  a += 1
  b += 1
  c += 1
  cnt += 1

print(cnt)
  