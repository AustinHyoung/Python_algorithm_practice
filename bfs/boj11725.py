# 트리의 부모 찾기
# bfs
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

parents = [0] * (n+1)

queue = deque([1])
while queue:
  node = queue.popleft()
  for child in graph[node]:
    if parents[child] == 0:
      parents[child] = node
      queue.append(child)

for i in range(2, n+1):
  print(parents[i])

