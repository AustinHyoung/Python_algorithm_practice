# 참외밭

# 남,북 = x
# 동, 서 = y
# 동 = 1, 서 = 2, 남 = 3, 북 = 4

# 3,4 = max 50
# 1,2 = max 160

n = int(input())
square = []

for i in range(6):
  row = list(map(int, input().split()))
  square.append(row)

w = 0
w_index = 0
h = 0
h_index = 0

for i in range(6):
  if square[i][0] == 4 or square[i][0] == 3:
    if h < square[i][1]:
      h < square[i][1]
      h_index = i
  elif square[i][0] == 2 or square[i][0] == 1:
    if w < square[i][1]:
      w = square[i][1]
      w_index = i

empty_w = abs(square[(w_index - 1) % 6][1] - square[(w_index + 1) % 6][1])
empty_h = abs(square[(h_index - 1) % 6][1] - square[(h_index + 1) % 6][1])

print((w * h) - (empty_w * empty_h) * n)