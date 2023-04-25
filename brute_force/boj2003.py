import sys

n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
left, right = 0, 1

while right <= n and left <= right:
  nums = lst[left:right]
  total = sum(nums)

  if total == m:
    cnt += 1
    right += 1
  elif total < m:
    right += 1
  else:
    left += 1

print(cnt)