# 세탁소 사장 동혁
# 그리디


T = int(input())
cent = [25, 10, 5, 1]
cnt = [0, 0, 0, 0]

for i in range(T):
  C = int(input())

  for i in range(len(cent)):
    cnt[i] = C // cent[i]
    C = C % cent[i]

  print(' '.join(map(str, cnt)))

