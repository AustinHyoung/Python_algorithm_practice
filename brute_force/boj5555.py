# 찾고자 하는 문자열
# 반지 개수
# 이어져있음

s = input()
n = int(input())
cnt = 0

for i in range(n):
  ring = input()
  length = len(ring)
  if s in ring:
    cnt+= 1
  else:
    for i in range(1, length):
      new_ring = ring[i:length] + ring[0:i]
      if s in new_ring:
        cnt += 1
        break

print(cnt)