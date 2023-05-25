# k칸 만큼 이동 또는 현재이동거리 *2 로 이동
# *2는 배터리가 안듦, k칸 이동은 배터리가 k만큼 소모
# 1 624 = 312 = 156 = 78 = 39 = 1 38 = 19 = 1 18 = 9 = 1 8 = 4 = 2 = 1 = 1 0
# 그리디?
def solution(n):
  ans = 0
  
  while n > 0:
    if n % 2 == 1:
      n -= 1
      ans += 1
    else:
      n //= 2
    

  return ans

print(solution(5000))