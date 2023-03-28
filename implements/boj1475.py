# 방 번호
# 구현

num = int(input())
arr = [0] * 10

for i in str(num):
  if i == "9" or i == "6":
    if arr[6] == arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1
  else:
    arr[int(i)] += 1

print(max(arr))
