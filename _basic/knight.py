# 체스 나이트
s = input()

# 문자 자르기
row = int(s[1])
col = int(ord(s[0])) - int(ord('a')) + 1

direction = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

cnt = 0
for direct in direction:
  next_row = row + direct[0]
  next_col = col + direct[1]
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    cnt += 1

print(cnt)