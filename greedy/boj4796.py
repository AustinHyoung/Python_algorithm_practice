# 캠핑
# 그리디
i = 1
while True:
  l, p, v = map(int, input().split())

  if l == 0 and p == 0 and v == 0:
    break

  a = v // p
  b = v % p
  answer = a * l + min(b, l)

  print(f"Case {i}: {answer}")
  i += 1