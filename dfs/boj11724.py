# 연결 요소의 개수
# dfs
import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, n+1):
  if not visited[i]:
    dfs(graph, i, visited)
    cnt += 1

print(cnt)

