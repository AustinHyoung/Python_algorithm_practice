import sys
input = sys.stdin.readline

n,m = map(int, input().split())
n_set = set()
m_set = set()
for _ in range(n):
  n_set.add(input().strip())

for _ in range(m):
  m_set.add(input().strip())

lst = sorted(list(n_set & m_set))

print(len(lst))
for data in lst:
  print(data)
