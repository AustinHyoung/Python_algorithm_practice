s = input()
lst = []

for i in range(len(s)):
  lst.append(s[i:])

for data in sorted(lst):
  print(data)