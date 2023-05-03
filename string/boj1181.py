import sys

n = int(sys.stdin.readline())

lst = set([sys.stdin.readline().rstrip() for _ in range(n)])
lst = list(lst)

lst.sort()
lst.sort(key = len)

for i in lst:
  print(i)
