# 연산자 끼워넣기
# 브루트 포스

n = int(input())
numbers = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

# 초기값
min_val = 1e9
max_val = -1e9

# 재귀
def dfs(i, res, add, sub, mul, div):
  global max_val, min_val
  # i증가 시켜서 결과 추출
  if i == n:
    max_val = max(max_val, res)
    min_val = min(min_val, res)
    return
  if add:
    dfs(i+1, res+numbers[i], add-1, sub, mul, div)
  if sub:
    dfs(i+1, res-numbers[i], add, sub-1, mul, div)
  if mul:
    dfs(i+1, res*numbers[i], add, sub, mul-1, div)
  if div:
    # 현재까지의 결과가 0보다 작으면 양수로 바꿔서 나눈 몫을 다시 음수로
    if res < 0:
      dfs(i+1, -(-res // numbers[i]), add, sub, mul, div-1)
    else:
      dfs(i+1, res // numbers[i], add, sub, mul, div-1)

dfs(1, numbers[0], add, sub, mul, div)

print(max_val)
print(min_val)
