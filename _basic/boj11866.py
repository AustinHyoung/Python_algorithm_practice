# 요세푸스 문제 0

# 1. 1~n 까지의 값 입력
# 2. k만큼 이동해서 해당하는 값 삭제
# 2. 
# 3. 삭제 후 새로운 리스트로 생성

n, k = map(int, input().split())
arr = list(range(1, n+1))
i = 0

print(arr)

result = []

while len(arr) > 1:
  i = (i + k-1) % len(arr)
  arr.pop(i)
  result.append(i)

answer = str(result)[1:-1]

print("<"+answer+">")