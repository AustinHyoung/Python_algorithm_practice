lst = []

for i in range(10):
  lst.append(int(input()))

over_sum = 0
under_sum = 0
for num in lst:
  if over_sum >= 100:
    break
  over_sum += num

for num in lst:
  under_sum += num
  if under_sum > 100:
    under_sum -= num
    break

if (over_sum - 100) > (100 - under_sum):
  print(under_sum)
elif (over_sum - 100) == (100 - under_sum):
  print(over_sum)
else:
  print(over_sum)