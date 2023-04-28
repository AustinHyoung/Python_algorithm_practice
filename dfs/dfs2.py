lst = [[], [1,2], [5,7], [3], [6,5], [4], [3,7], [1,7]]
visited = [False] * 8

def dfs(lst, v, visited):
  visited[v] = True
  print(v, end="")

  for i in lst[v]:
    if not visited[i]:
      dfs(lst, i, visited)

dfs(lst, 1, visited)