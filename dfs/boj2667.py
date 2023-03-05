#단지 번호붙이기

n = int(input())

map_arr = []

for i in range(n):
  row = list(map(int, input()))
  map_arr.append(row)

print(map_arr)

def dfs(map_arr, v, visited):
  visited[v] = True
  print(v, end=" ")
  for i in map_arr[v]:
    if not visited[i]:
      dfs(map_arr, i, visited)

