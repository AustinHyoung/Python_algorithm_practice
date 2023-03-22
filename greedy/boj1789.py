# 수들의 합
# 그리디

S = int(input())

N = 1
sum = 1

while sum <= S:
  N += 1
  sum += N

print(N-1)
