# 7개의 수의 합이 100이 되어야함, 주어지는 수는 100을 넘지않음

from itertools import combinations

lst = []

for i in range(9):
  lst.append(int(input()))

lst.sort()

def recursive(lst):
  def sum_recursive(comb):
    return sum(comb)
  
  for comb in combinations(lst, 7):
    if sum_recursive(comb) == 100:
      return comb
  
  return None

for n in recursive(lst):
  print(n)