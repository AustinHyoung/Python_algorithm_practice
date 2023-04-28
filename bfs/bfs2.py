from collections import deque

lst = [[], [1,2], [5,7], [3], [6,5], [4], [3,7], [1,7]]
visited = [False] * 8

def bfs(lst, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
      x = queue.popleft()
      print(x, end=" ")

      for i in lst[x]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True

bfs(lst, 1, visited)