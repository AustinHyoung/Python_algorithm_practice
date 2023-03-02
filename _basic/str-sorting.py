s = input()
arr = sorted(s)

num = 0
str_result = ""
for i in arr:
  if 48 <= ord(i) <= 57:
    num += int(i)
  else:
    str_result += i

print(str_result+str(num))

