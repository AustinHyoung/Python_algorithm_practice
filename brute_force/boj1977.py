# n~m 모든 수중 제곱수, 제곱수들의 합, 그 중 최소값

n = int(input())
m = int(input())
lst = []

i = 1
while True:
  num = i * i
  if num > m:
    break
  if n <= num <= m:
    lst.append(num)
  i += 1

if len(lst) == 0:
  print(-1)
else:
  print(sum(lst))
  print(min(lst))

