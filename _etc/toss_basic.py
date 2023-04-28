# 중복되지 않는 숫자 6자리
# 1부터 45의 숫자
# 오름차순
# 주어진 숫자들이 위의 규칙에 맞으면 true 틀리면 false 출력

lst = list(map(int, input().split()))
index = 1

def solve():
  global index
  for i in lst:
    if lst.count(i) > 1:
      return "false"
    elif i <= 0 or i > 45:
      return "false"
    elif index < len(lst):
      if i > lst[index]:
        return "false"
      
      index += 1
      if index > len(lst):
        return "true"
    
  return "true"

print(solve())