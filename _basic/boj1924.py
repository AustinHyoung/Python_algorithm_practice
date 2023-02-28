# 2007년

x, y = map(int, input().split())

arr = [31, 28,31,30,31,30,31,31,30,31,30,31]
sum = 0

for i in range(x-1):
  sum += arr[i]

sum += y

if sum % 7 == 1:
  print("MON")
elif sum % 7 == 2:
  print("TUE")
elif sum % 7 == 3:
  print("WED")
elif sum % 7 == 4:
  print("THU")
elif sum % 7 == 5:
  print("FRI")
elif sum % 7 == 6:
  print("SAT")
elif sum % 7 == 0:
  print("SUN")
