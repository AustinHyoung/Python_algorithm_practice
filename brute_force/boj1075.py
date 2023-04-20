n = int(input())
f = int(input())

answer = ""
init = n - int(str(n)[-2:])

while True:
  if init % f == 0:
    break
  init += 1

print(str(init)[-2:])