# 공 넣기

# n, m 입력
n, m = map(int, input().split())

# 리스트 모든 값 0으로 초기화
arr = [0] * n

# 4번 입력 + i j k 입력, 인덱스만큼 반복해서 배열에 덮어쓰기
for _ in range(m):
  i, j, k = map(int, input().split())
  for idx in range(i-1, j):
    arr[idx] = k

# 띄어쓰기 반복 출력
for x in range (n) :
    print(arr[x],'',end='')
