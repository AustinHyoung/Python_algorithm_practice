# 최댓값

inputs = []

for _ in range(9):
  data = int(input())
  inputs.append(data)

print(max(inputs))
print(inputs.index(max(inputs))+1)