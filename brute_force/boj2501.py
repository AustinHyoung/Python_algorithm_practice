# n의 약수, 오름차순+1 = k, k번째가 없으면 0

n, k = map(int, input().split())
lst = []

for i in range(1, n+1):
  if n % i == 0:
    lst.append(i)

lst.sort()

if len(lst) < k:
  print(0)
else:
  print(lst[k-1])