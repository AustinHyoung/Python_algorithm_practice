

n, m = map(int, input().split())

lst = []

for i in range(n):
  lst.append(list(map(int, input())))

answer = 1

max_size = min(n, m)

for size in range(2, max_size+1):
  for i in range(n-size+1):
    for j in range(m-size+1):
      if lst[i][j] == lst[i][j+size-1] == lst[i+size-1][j] == lst[i+size-1][j+size-1]:
        answer = size * size

print(answer)
