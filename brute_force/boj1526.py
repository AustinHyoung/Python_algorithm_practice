n = int(input())

def func(n):
  for i in str(n):
    if i != '4' and i != '7':
      return False
  return True

while not func(n):
  n -= 1

print(n)