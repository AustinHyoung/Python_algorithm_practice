n = int(input())
lst = []

for _ in range(n):
  lst.append(input())

res = ""

for i in range(len(lst[0])):
  char = lst[0][i]
  for j in range(1, n):
    if lst[j][i] != char:
      char = "?"
      break
  res += char

print(res)