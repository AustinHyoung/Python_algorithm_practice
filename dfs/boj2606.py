# 바이러스

def dfs(graph, v, visited):
  visited[v] = True
  cnt = 1
  for i in graph[v]:
    if not visited[i]:
      cnt += dfs(graph, i, visited)
  return cnt

computer = int(input())
connection = int(input())
graph = [[] for _ in range(computer+1)]

for _ in range(connection):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (computer+1)
cnt = dfs(graph, 1, visited)
print(cnt -1)
